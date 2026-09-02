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

A página busca conteúdo por **três caminhos, em ordem**. Se o primeiro falhar, ela tenta o seguinte sozinha — por isso ela nunca fica vazia:

1. **O arquivo `noticias.json`**, gerado pela rotina do GitHub a cada 30 minutos. É o caminho principal: traz mais fontes e os vídeos do YouTube.
2. **Busca direta nos sites**, feita pelo próprio navegador em 23 fontes. Entra em ação quando o `noticias.json` não existe ou não pode ser lido — inclusive se a rotina do GitHub nunca tiver rodado.
3. **A cópia embutida na página**, usada só se os dois primeiros falharem (rede bloqueando tudo).

A linha de status embaixo do cabeçalho diz qual caminho está em uso no momento.

### As duas engrenagens

São duas engrenagens que se completam:

**No servidor (GitHub Actions), a cada 30 minutos.** A rotina visita cerca de 60 sites e 11 canais do YouTube, classifica cada notícia por esporte e grava o `noticias.json`.

**No navegador, a cada 30 minutos.** A página busca o `noticias.json` sozinha e troca os cards na tela — **sem F5, sem recarregar**. Também busca ao voltar para a aba do navegador e ao clicar em "Atualizar agora". A bolinha amarela pisca enquanto está buscando.

Por isso a página pode ficar aberta o dia todo numa tela que ela se mantém viva.

---

## O carrossel de placares

A faixa no topo mostra os jogos **de hoje** de 14 competições: Brasileirão, Copa do Brasil, Série B, Libertadores, Sul-Americana, Champions, Europa League, Premier League, LaLiga, Serie A italiana, Bundesliga, Ligue 1, Argentina e jogos de seleções.

- **Jogo em andamento** aparece primeiro, com borda vermelha e o minuto correndo.
- **Jogo que ainda vai começar** mostra o horário.
- **Jogo encerrado** mostra "FIM", com o time perdedor em cinza.
- Atualiza **a cada 60 segundos**, sozinho.
- O carrossel anda sozinho a cada 5 segundos e **pausa quando o mouse está em cima**. Também dá para arrastar com o dedo no celular ou usar as setas laterais.
- Se não houver jogo nenhum no dia, a faixa some sozinha.

Clicando num jogo, abre a página da partida na ESPN.

**Para incluir ou tirar uma competição:** no `index.html`, procure por `COMPETICOES` e edite a lista. Cada linha é `{ nome: "Como aparece", liga: "código" }`. Alguns códigos úteis: `por.1` (Português), `ned.1` (Holandês), `mex.1` (México), `usa.1` (MLS), `uefa.euro` (Eurocopa), `fifa.world` (Copa do Mundo), `bra.copa_do_brazil` (Copa do Brasil).

**Para mudar o ritmo:** `PLACAR_INTERVALO` é de quanto em quanto tempo os placares são buscados (60 segundos) e `GIRO` é a velocidade do carrossel (5 segundos).

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

**Miniaturas.** A foto de cada notícia é buscada em quatro tentativas, nesta ordem: um serviço espelho que também redimensiona a imagem (images.weserv.nl), um endereço alternativo do mesmo serviço (wsrv.nl), o endereço original do portal e, por último, o card colorido com o nome do veículo. Isso existe porque vários portais bloqueiam a exibição da foto fora do site deles — o espelho contorna esse bloqueio e ainda entrega a imagem já no tamanho certo, o que deixa a página mais leve. Vídeos do YouTube vão direto, sem espelho.

**Os placares vêm da ESPN.** É um endereço público e gratuito, que não exige cadastro nem chave. Como não é um serviço contratado, pode mudar sem aviso — se um dia a faixa sumir, é isso. As notícias e os vídeos continuam funcionando normalmente, porque não dependem dela.

**Endereço público.** Qualquer pessoa com o link vê a página. O conteúdo é só manchete pública, mas para usar logo ou identidade visual da TNT Sports, alinhe antes com o time de marca.
