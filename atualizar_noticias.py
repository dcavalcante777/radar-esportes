"""Radar Esportes - rotina de atualizacao.

Busca as manchetes dos sites e os videos dos canais do YouTube, classifica
tudo por esporte e grava dois arquivos:

  noticias.json  - lido pela pagina a cada 30 minutos, sem precisar de F5
  index.html     - recebe o mesmo conteudo embutido, como reserva

Roda sozinho no GitHub Actions. Usa so a biblioteca padrao do Python.
Para incluir ou tirar um site ou canal, editar o arquivo fontes.py.
"""

import html
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime

try:
    from fontes import CANAIS, CATEGORIAS, FEEDS, classificar
except ImportError:
    print("=" * 70)
    print("ERRO: o arquivo fontes.py nao esta no repositorio.")
    print("Ele fica na mesma pasta do atualizar_noticias.py.")
    print("Suba o fontes.py em Add file > Upload files e rode de novo.")
    print("=" * 70)
    raise SystemExit(1)

POR_FONTE = 8
POR_CANAL = 4
LIMITE_POR_CATEGORIA = 60
JANELA_HORAS = 24
BRASILIA = timezone(timedelta(hours=-3))
UA = {"User-Agent": "Mozilla/5.0 (compatible; RadarEsportes/2.0)"}

TAG = re.compile(r"<[^>]+>")
IMG_SRC = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.I)
EXT_IMG = re.compile(r"\.(jpe?g|png|webp|avif)", re.I)
URL_IMG = re.compile(r"https?://[^\s\"'<>]+\.(?:jpe?g|png|webp|avif)", re.I)
CAMINHO_IMG = re.compile(r"/(img|image|fotos?|media|thumb)", re.I)
ID_CANAL = re.compile(r'"(?:channelId|externalId)":"(UC[\w-]{20,})"')


def baixar(url, tempo=25):
    pedido = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(pedido, timeout=tempo) as resposta:
        return resposta.read()


def limpar(texto):
    if not texto:
        return ""
    return re.sub(r"\s+", " ", html.unescape(TAG.sub(" ", texto))).strip()


def achar(item, nomes):
    for filho in item.iter():
        if filho.tag.split("}")[-1] in nomes and (filho.text or "").strip():
            return filho.text.strip()
    return ""


def eh_imagem(url, tipo=""):
    if not url or not url.startswith("http"):
        return False
    if tipo and tipo.startswith("image"):
        return True
    return bool(EXT_IMG.search(url) or CAMINHO_IMG.search(url))


def achar_imagem(item):
    for elemento in item.iter():
        for atributo in ("url", "href", "src"):
            valor = elemento.get(atributo)
            if eh_imagem(valor, elemento.get("type") or ""):
                return valor
    for elemento in item.iter():
        if elemento.tag.split("}")[-1].lower() in ("url", "image", "thumbnail"):
            texto = (elemento.text or "").strip()
            if eh_imagem(texto):
                return texto
    for elemento in item.iter():
        if elemento.tag.split("}")[-1] in ("encoded", "description", "summary", "content"):
            corpo = elemento.text or ""
            achado = IMG_SRC.search(corpo)
            if achado:
                return achado.group(1)
            achado = URL_IMG.search(html.unescape(corpo))
            if achado:
                return achado.group(0)
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


def ler_feed(fonte):
    nome, categoria_padrao, url = fonte
    try:
        raiz = ET.fromstring(baixar(url))
    except Exception as erro:
        return nome, [], str(erro)[:60]

    itens = list(raiz.iter("item"))
    if not itens:
        itens = list(raiz.iter("{http://www.w3.org/2005/Atom}entry"))

    resultado = []
    for item in itens[:POR_FONTE]:
        titulo = limpar(achar(item, ("title",)))
        link = achar(item, ("link",))
        if not link:
            for filho in item.iter():
                if filho.tag.split("}")[-1] == "link" and filho.get("href"):
                    link = filho.get("href")
                    break
        if not titulo or not link:
            continue
        resumo = limpar(achar(item, ("description", "summary", "content")))[:170]
        resultado.append(
            {
                "title": titulo,
                "link": link,
                "desc": resumo,
                "img": achar_imagem(item),
                "src": nome,
                "cat": classificar(titulo, resumo, categoria_padrao),
                "when": quando(item),
                "tipo": "noticia",
            }
        )
    return nome, resultado, ""


def id_do_canal(handle):
    enderecos = (
        "https://www.youtube.com/@%s" % handle,
        "https://www.youtube.com/c/%s" % handle,
        "https://www.youtube.com/user/%s" % handle,
    )
    for endereco in enderecos:
        try:
            pagina = baixar(endereco, 20).decode("utf-8", "ignore")
        except Exception:
            continue
        achado = ID_CANAL.search(pagina)
        if achado:
            return achado.group(1)
    return ""


def ler_canal(canal):
    nome, categoria, handle = canal
    identificador = id_do_canal(handle)
    if not identificador:
        return nome, [], "canal nao localizado"

    url = "https://www.youtube.com/feeds/videos.xml?channel_id=" + identificador
    try:
        raiz = ET.fromstring(baixar(url))
    except Exception as erro:
        return nome, [], str(erro)[:60]

    resultado = []
    entradas = list(raiz.iter("{http://www.w3.org/2005/Atom}entry"))
    for entrada in entradas[:POR_CANAL]:
        vid = achar(entrada, ("videoId",))
        titulo = limpar(achar(entrada, ("title",)))
        if not vid or not titulo:
            continue
        resultado.append(
            {
                "title": titulo,
                "link": "https://www.youtube.com/watch?v=" + vid,
                "desc": limpar(achar(entrada, ("description",)))[:150],
                "img": "https://i.ytimg.com/vi/%s/hqdefault.jpg" % vid,
                "src": nome,
                "cat": categoria,
                "when": quando(entrada),
                "tipo": "video",
            }
        )
    return nome, resultado, ""


def coletar(lista, funcao, rotulo):
    print("\n%s (%d):" % (rotulo, len(lista)))
    saida = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        for nome, itens, erro in executor.map(funcao, lista):
            marca = "x" if erro else "."
            print("  %s %-30s %s" % (marca, nome, erro or len(itens)))
            saida.extend(itens)
    return saida


def main():
    caminho_html = sys.argv[1] if len(sys.argv) > 1 else "index.html"
    caminho_json = sys.argv[2] if len(sys.argv) > 2 else "noticias.json"

    noticias = coletar(FEEDS, ler_feed, "Sites")
    videos = coletar(CANAIS, ler_canal, "Canais do YouTube")

    if len(noticias) < 10:
        print("\nPoucas manchetes (%d) - mantendo a versao anterior." % len(noticias))
        return 0

    anteriores = []
    try:
        with open(caminho_json, encoding="utf-8") as arquivo:
            anteriores = json.load(arquivo).get("itens", [])
        print("\nRecuperados %d itens da rodada anterior." % len(anteriores))
    except Exception:
        pass

    corte = (datetime.now(timezone.utc).timestamp() - JANELA_HORAS * 3600) * 1000
    anteriores = [i for i in anteriores if i.get("when", 0) >= corte]

    vistos = set()
    unicos = []
    for item in sorted(noticias + videos + anteriores, key=lambda n: -n["when"]):
        chave = item["title"].lower()[:70]
        if chave in vistos:
            continue
        vistos.add(chave)
        unicos.append(item)

    contagem = {}
    final = []
    for item in unicos:
        chave = (item["cat"], item["tipo"])
        contagem[chave] = contagem.get(chave, 0) + 1
        if contagem[chave] <= LIMITE_POR_CATEGORIA:
            final.append(item)

    agora = datetime.now(timezone.utc)
    carimbo = agora.astimezone(BRASILIA).strftime("%d/%m/%Y, %Hh%M")

    dados = {
        "atualizado_em": agora.isoformat(),
        "carimbo": carimbo,
        "categorias": CATEGORIAS,
        "itens": final,
    }

    with open(caminho_json, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, separators=(",", ":"))

    pagina = open(caminho_html, encoding="utf-8").read()
    bloco = "  var DADOS = " + json.dumps(dados, ensure_ascii=False, indent=1).replace("\n", "\n  ") + ";"
    nova = re.sub(
        r"/\* INICIO-NOTICIAS \*/.*?/\* FIM-NOTICIAS \*/",
        lambda _: "/* INICIO-NOTICIAS */\n" + bloco + "\n  /* FIM-NOTICIAS */",
        pagina,
        flags=re.S,
    )
    if nova == pagina:
        print("\nMarcadores INICIO-NOTICIAS / FIM-NOTICIAS nao encontrados.")
        return 1
    open(caminho_html, "w", encoding="utf-8").write(nova)

    print("\nResumo por aba:")
    for categoria in CATEGORIAS:
        n = sum(1 for i in final if i["cat"] == categoria and i["tipo"] == "noticia")
        v = sum(1 for i in final if i["cat"] == categoria and i["tipo"] == "video")
        print("  %-20s %3d noticias  %2d videos" % (categoria, n, v))
    print("\nPronto: %d itens gravados (%s), guardando as ultimas %dh."
          % (len(final), carimbo, JANELA_HORAS))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
