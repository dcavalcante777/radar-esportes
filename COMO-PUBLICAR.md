# Radar Esportes — guia do projeto

## Os arquivos

| Arquivo | Para que serve | Vai para o repositório? |
|---|---|---|
| `index.html` | A página em si. É o que fica no ar. | Sim |
| `noticias.json` | O conteúdo do momento. A página lê este arquivo a cada 30 min. | Sim (a rotina cria sozinha) |
| `atualizar_noticias.py` | A rotina que busca manchetes e vídeos e grava os dois arquivos acima. | Sim |
| `fontes.py` | A lista de sites, canais e as regras de classificação por esporte. | Sim |
| `workflow-atualizar.yml` | O agendamento. Vai para `.github/workflows/atualizar.yml`. | Sim, com esse caminho |

---

## Como colocar no ar (primeira vez)

1. Em **github.com**, crie um repositório **público** chamado `radar-esportes`.
2. **Add file → Upload files**: suba `index.html`, `atualizar_noticias.py` e `fontes.py`. **Commit changes**.
3. **Settings → Pages** → *Source*: **Deploy from a branch** → **main** / **(root)** → **Save**.
   Em 1 a 2 minutos aparece o endereço `https://SEU-USUARIO.github.io/radar-esportes/`.
4. **Add file → Create new file**, nome exatamente `.github/workflows/atualizar.yml`, cole o conteúdo do `workflow-atualizar.yml` e **Commit changes**.
5. Aba **Actions → Atualizar Radar Esportes → Run workflow**. Isso cria o `noticias.json` e enche a página pela primeira vez.

---

## Como a atualização funciona

São duas engrenagens que se completam:

**No servidor (GitHub Actions), a cada 30 minutos.** A rotina visita cerca de 60 sites e 11 canais do YouTube, classifica cada notícia por esporte e grava o `noticias.json`.

**No navegador, a cada 30 minutos.** A página busca o `noticias.json` sozinha e troca os cards na tela — **sem F5, sem recarregar**. Também busca ao voltar para a aba do navegador e ao clicar em "Atualizar agora". A bolinha amarela pisca enquanto está buscando.

Por isso a página pode ficar aberta o dia todo numa tela que ela se mantém viva.

---

## As abas

FUTEBOL BRASIL · FUT EUROPEU · FUT SUL-AMERICANO · BASQUETE · F1 · LUTAS · ESPORTE OLÍMPICO · OUTROS ESPORTES · FOFOCAS · TUDO

O número ao lado de cada aba mostra quantos itens ela tem no momento. A busca funciona junto com as abas: digite "Flamengo" e os números mudam, mostrando onde há resultado.

A classificação é feita por assunto do título. Sites específicos (ge Basquete, BBC F1) já entram direto na aba certa; sites gerais (ge, UOL, CNN) são separados por palavra-chave.

---

## Ajustes do dia a dia

Quase tudo se resolve editando **`fontes.py`** no próprio GitHub (abrir o arquivo → ícone de lápis → editar → *Commit changes*).

**Incluir um site.** Na lista `FEEDS`, acrescente uma linha:
```python
("Nome do site", "FUTEBOL BRASIL", "https://site.com.br/feed"),
```
A categoria pode ser qualquer uma das abas, ou `"AUTO"` para deixar o assunto decidir.

**Incluir um canal do YouTube.** Na lista `CANAIS`:
```python
("Nome do canal", "FUTEBOL BRASIL", "arrobadocanal"),
```
Use só o @ do canal, sem o arroba. A rotina descobre o código interno sozinha.

**Mudar a ordem das abas.** Reordene a lista `CATEGORIAS`. A primeira é a que abre.

**Afinar a classificação.** As listas `MAPA` e `FOFOCA` guardam as palavras-chave. Se algo estiver caindo na aba errada, acrescente a palavra na lista certa.

**Trocar as contas do X.** No `index.html`, procure por `X_ACCOUNTS`.

**Mudar a frequência.** No `atualizar.yml`:

| Quero que rode... | Escreva |
|---|---|
| A cada 30 minutos (padrão) | `"*/30 * * * *"` |
| De hora em hora | `"0 * * * *"` |
| A cada 2 horas | `"0 */2 * * *"` |
| Só às 9h, 15h e 21h de Brasília | `"0 0,12,18 * * *"` |

Horários fixos ficam em UTC — Brasília é UTC−3, então some 3 (9h daqui = 12 UTC).

Se mudar aqui, mude também a linha `var INTERVALO = 30 * 60 * 1000;` no `index.html`, para os dois lados ficarem no mesmo ritmo.

---

## Coisas boas de saber

**Nada quebra se uma fonte cair.** Se um site sair do ar, ele é pulado e os outros seguem. Se a coleta inteira falhar, a rotina não grava nada e o conteúdo anterior continua no ar. E se o `noticias.json` não puder ser lido, a página usa a cópia embutida dentro dela mesma.

**O horário da rotina varia um pouco.** O GitHub executa agendamentos por fila, então pode atrasar alguns minutos em horários de pico. Para notícias, é irrelevante.

**Custo zero.** Repositório público tem execução ilimitada no GitHub Actions.

**Miniaturas.** Vêm dos próprios portais. Alguns sites bloqueiam a exibição da foto fora do domínio deles — nesses casos entra um card colorido com o nome do veículo. Vídeos do YouTube sempre trazem miniatura.

**Endereço público.** Qualquer pessoa com o link vê a página. O conteúdo é só manchete pública, mas para usar logo ou identidade visual da TNT Sports, alinhe antes com o time de marca.
