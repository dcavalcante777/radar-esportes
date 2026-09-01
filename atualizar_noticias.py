"""Atualiza o resumo de manchetes embutido no index.html do Radar Esportes.

Roda sozinho no GitHub Actions (ver workflow-atualizar.yml).
Nao precisa de nenhuma biblioteca externa: usa so a biblioteca padrao do Python.
"""

import html
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime

FEEDS = [
    ("ge", "Brasil", "https://ge.globo.com/rss/ge/"),
    ("ge Futebol", "Brasil", "https://ge.globo.com/rss/ge/futebol/"),
    ("UOL Esporte", "Brasil", "https://rss.uol.com.br/feed/esporte.xml"),
    ("Gazeta Esportiva", "Brasil", "https://www.gazetaesportiva.com/feed/"),
    ("CNN Esportes", "Brasil", "https://www.cnnbrasil.com.br/esportes/feed/"),
    ("Lance!", "Brasil", "https://www.lance.com.br/feed"),
    ("ESPN FC", "Europa", "https://www.espn.com/espn/rss/soccer/news"),
    ("BBC Football", "Europa", "https://feeds.bbci.co.uk/sport/football/rss.xml"),
    ("Sky Sports", "Europa", "https://www.skysports.com/rss/12040"),
    ("Guardian Futebol", "Europa", "https://www.theguardian.com/football/rss"),
    ("MARCA", "Europa", "https://e00-marca.uecdn.es/rss/futbol/futbol-internacional.xml"),
    ("BBC Sport", "Outros", "https://feeds.bbci.co.uk/sport/rss.xml"),
]

POR_FONTE = 8
LIMITE_TOTAL = 60
UA = {"User-Agent": "Mozilla/5.0 (compatible; RadarEsportes/1.0)"}

TAG = re.compile(r"<[^>]+>")
IMG_SRC = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.I)
EXT_IMG = re.compile(r"\.(jpe?g|png|webp|avif)", re.I)


def limpar(texto):
    if not texto:
        return ""
    return re.sub(r"\s+", " ", html.unescape(TAG.sub(" ", texto))).strip()


def achar(item, nomes):
    for filho in item:
        etiqueta = filho.tag.split("}")[-1]
        if etiqueta in nomes and (filho.text or "").strip():
            return filho.text.strip()
    return ""


def achar_imagem(item):
    for filho in item:
        etiqueta = filho.tag.split("}")[-1]
        if etiqueta in ("content", "thumbnail", "enclosure"):
            url = filho.get("url") or filho.get("href") or ""
            tipo = filho.get("type") or ""
            if url and (tipo.startswith("image") or EXT_IMG.search(url)):
                return url
    for filho in item:
        if filho.tag.split("}")[-1] in ("encoded", "description", "summary"):
            achado = IMG_SRC.search(filho.text or "")
            if achado:
                return achado.group(1)
    return ""


def quando(item):
    bruto = achar(item, ("pubDate", "published", "updated", "date"))
    if not bruto:
        return 0
    try:
        data = parsedate_to_datetime(bruto)
    except Exception:
        try:
            data = datetime.fromisoformat(bruto.replace("Z", "+00:00"))
        except Exception:
            return 0
    if data.tzinfo is None:
        data = data.replace(tzinfo=timezone.utc)
    return int(data.timestamp() * 1000)


def ler_feed(nome, categoria, url):
    try:
        pedido = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(pedido, timeout=25) as resposta:
            bruto = resposta.read()
        raiz = ET.fromstring(bruto)
    except Exception as erro:
        print("  falhou %s: %s" % (nome, erro))
        return []

    itens = raiz.iter("item")
    resultado = []
    for item in itens:
        titulo = limpar(achar(item, ("title",)))
        link = achar(item, ("link",))
        if not titulo or not link:
            continue
        resultado.append(
            {
                "title": titulo,
                "link": link,
                "desc": limpar(achar(item, ("description", "summary")))[:160],
                "img": achar_imagem(item),
                "src": nome,
                "cat": categoria,
                "when": quando(item),
            }
        )
        if len(resultado) >= POR_FONTE:
            break

    if not resultado:
        for entrada in raiz.iter("{http://www.w3.org/2005/Atom}entry"):
            titulo = limpar(achar(entrada, ("title",)))
            link = ""
            for filho in entrada:
                if filho.tag.split("}")[-1] == "link":
                    link = filho.get("href") or ""
                    break
            if not titulo or not link:
                continue
            resultado.append(
                {
                    "title": titulo,
                    "link": link,
                    "desc": limpar(achar(entrada, ("summary", "content")))[:160],
                    "img": achar_imagem(entrada),
                    "src": nome,
                    "cat": categoria,
                    "when": quando(entrada),
                }
            )
            if len(resultado) >= POR_FONTE:
                break

    print("  %s: %d manchetes" % (nome, len(resultado)))
    return resultado


def main():
    caminho = sys.argv[1] if len(sys.argv) > 1 else "index.html"
    print("Buscando manchetes...")

    manchetes = []
    vistos = set()
    for nome, categoria, url in FEEDS:
        for noticia in ler_feed(nome, categoria, url):
            chave = noticia["title"].lower()[:70]
            if chave in vistos:
                continue
            vistos.add(chave)
            manchetes.append(noticia)

    if len(manchetes) < 5:
        print("Poucas manchetes (%d) - mantendo o resumo anterior." % len(manchetes))
        return 0

    manchetes.sort(key=lambda n: -n["when"])
    manchetes = manchetes[:LIMITE_TOTAL]

    pagina = open(caminho, encoding="utf-8").read()
    bloco = "  var FALLBACK = " + json.dumps(manchetes, ensure_ascii=False, indent=2).replace("\n", "\n  ") + ";"
    novo = re.sub(
        r"/\* INICIO-NOTICIAS \*/.*?/\* FIM-NOTICIAS \*/",
        lambda _: "/* INICIO-NOTICIAS */\n" + bloco + "\n  /* FIM-NOTICIAS */",
        pagina,
        flags=re.S,
    )
    if novo == pagina:
        print("Marcadores INICIO-NOTICIAS / FIM-NOTICIAS nao encontrados no arquivo.")
        return 1

    agora = datetime.now(timezone.utc).astimezone()
    carimbo = agora.strftime("%d/%m/%Y, %Hh%M")
    novo = re.sub(
        r'var SNAPSHOT_NOTE = "[^"]*";',
        'var SNAPSHOT_NOTE = "Fontes ao vivo indisponiveis nesta rede - mostrando o resumo de %s.";' % carimbo,
        novo,
    )
    novo = re.sub(
        r"ao vivo \+ resumo de [^<]*<",
        "ao vivo + resumo de %s<" % carimbo,
        novo,
    )

    open(caminho, "w", encoding="utf-8").write(novo)
    print("Pronto: %d manchetes gravadas em %s." % (len(manchetes), caminho))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
