"""Fontes e regras de classificacao do Radar Esportes.

Editar este arquivo e a unica coisa necessaria para incluir ou tirar
um site, um canal do YouTube ou mudar como uma noticia e classificada.
"""

# Ordem das abas no site. A primeira e a que abre.
CATEGORIAS = [
    "FUTEBOL BRASIL",
    "MERCADO",
    "FUT EUROPEU",
    "FUT SUL-AMERICANO",
    "BASQUETE",
    "F1",
    "LUTAS",
    "ESPORTE OLÍMPICO",
    "OUTROS ESPORTES",
    "FOFOCAS",
]

# (nome exibido, categoria padrao, endereco do feed)
# categoria "AUTO" = decidir pelo assunto do titulo.
FEEDS = [
    # ---------------- FUTEBOL BRASILEIRO ----------------
    ("ge Futebol", "FUTEBOL BRASIL", "https://ge.globo.com/rss/ge/futebol/"),
    ("ge Brasileirão", "FUTEBOL BRASIL", "https://ge.globo.com/rss/ge/futebol/brasileirao-serie-a/"),
    ("ge Copa do Brasil", "FUTEBOL BRASIL", "https://ge.globo.com/rss/ge/futebol/copa-do-brasil/"),
    ("ge Flamengo", "FUTEBOL BRASIL", "https://ge.globo.com/rss/ge/futebol/times/flamengo/"),
    ("ge Palmeiras", "FUTEBOL BRASIL", "https://ge.globo.com/rss/ge/futebol/times/palmeiras/"),
    ("ge Corinthians", "FUTEBOL BRASIL", "https://ge.globo.com/rss/ge/futebol/times/corinthians/"),
    ("ge São Paulo", "FUTEBOL BRASIL", "https://ge.globo.com/rss/ge/futebol/times/sao-paulo/"),
    ("ge Vasco", "FUTEBOL BRASIL", "https://ge.globo.com/rss/ge/futebol/times/vasco/"),
    ("ge Fluminense", "FUTEBOL BRASIL", "https://ge.globo.com/rss/ge/futebol/times/fluminense/"),
    ("ge Botafogo", "FUTEBOL BRASIL", "https://ge.globo.com/rss/ge/futebol/times/botafogo/"),
    ("ge Grêmio", "FUTEBOL BRASIL", "https://ge.globo.com/rss/ge/futebol/times/gremio/"),
    ("ge Internacional", "FUTEBOL BRASIL", "https://ge.globo.com/rss/ge/futebol/times/internacional/"),
    ("ge Cruzeiro", "FUTEBOL BRASIL", "https://ge.globo.com/rss/ge/futebol/times/cruzeiro/"),
    ("ge Atlético-MG", "FUTEBOL BRASIL", "https://ge.globo.com/rss/ge/futebol/times/atletico-mg/"),
    ("ge Santos", "FUTEBOL BRASIL", "https://ge.globo.com/rss/ge/futebol/times/santos/"),
    ("ge Bahia", "FUTEBOL BRASIL", "https://ge.globo.com/rss/ge/futebol/times/bahia/"),
    ("ge Seleção", "FUTEBOL BRASIL", "https://ge.globo.com/rss/ge/futebol/selecao-brasileira/"),
    ("Lance!", "FUTEBOL BRASIL", "https://www.lance.com.br/feed"),
    ("Gazeta Esportiva", "FUTEBOL BRASIL", "https://www.gazetaesportiva.com/feed/"),
    ("Placar", "FUTEBOL BRASIL", "https://placar.abril.com.br/feed/"),
    ("Trivela", "AUTO", "https://trivela.com.br/feed/"),

    # ---------------- GERAIS (classificados pelo assunto) ----------------
    ("ge", "AUTO", "https://ge.globo.com/rss/ge/"),
    ("UOL Esporte", "AUTO", "https://rss.uol.com.br/feed/esporte.xml"),
    ("CNN Esportes", "AUTO", "https://www.cnnbrasil.com.br/esportes/feed/"),
    ("Terra Esportes", "AUTO", "https://www.terra.com.br/esportes/rss.xml"),
    ("R7 Esportes", "AUTO", "https://esportes.r7.com/feed.xml"),
    ("Metrópoles", "AUTO", "https://www.metropoles.com/feed"),

    # ---------------- FUTEBOL EUROPEU ----------------
    ("BBC Football", "FUT EUROPEU", "https://feeds.bbci.co.uk/sport/football/rss.xml"),
    ("Sky Sports", "FUT EUROPEU", "https://www.skysports.com/rss/12040"),
    ("Guardian Futebol", "FUT EUROPEU", "https://www.theguardian.com/football/rss"),
    ("MARCA", "FUT EUROPEU", "https://e00-marca.uecdn.es/rss/futbol/futbol-internacional.xml"),
    ("AS", "FUT EUROPEU", "https://as.com/rss/futbol/primera.xml"),
    ("ESPN FC", "FUT EUROPEU", "https://www.espn.com/espn/rss/soccer/news"),
    ("Goal", "FUT EUROPEU", "https://www.goal.com/feeds/en/news"),
    ("ge Futebol Internacional", "FUT EUROPEU", "https://ge.globo.com/rss/ge/futebol/futebol-internacional/"),

    # ---------------- FUTEBOL SUL-AMERICANO ----------------
    ("ge Libertadores", "FUT SUL-AMERICANO", "https://ge.globo.com/rss/ge/futebol/libertadores/"),
    ("ge Sul-Americana", "FUT SUL-AMERICANO", "https://ge.globo.com/rss/ge/futebol/copa-sul-americana/"),
    ("Olé", "FUT SUL-AMERICANO", "https://www.ole.com.ar/rss/futbol-primera/"),
    ("Depor", "FUT SUL-AMERICANO", "https://depor.com/arcio/rss/"),

    # ---------------- MERCADO / TRANSFERÊNCIAS ----------------
    ("Gazzetta Mercado", "MERCADO", "https://www.gazzetta.it/dynamic-feed/rss/section/Calciomercato.xml"),
    ("FussballTransfers", "MERCADO", "https://www.fussballtransfers.com/rss-feed"),
    ("Football España", "MERCADO", "https://www.football-espana.net/feed"),
    ("Sports Mole", "MERCADO", "https://www.sportsmole.co.uk/rss.xml"),

    # ---------------- ITÁLIA ----------------
    ("Gazzetta", "FUT EUROPEU", "https://www.gazzetta.it/dynamic-feed/rss/section/Calcio.xml"),
    ("Gazzetta Serie A", "FUT EUROPEU", "https://www.gazzetta.it/dynamic-feed/rss/section/Calcio/Serie-A.xml"),
    ("Gazzetta Copas", "FUT EUROPEU", "https://www.gazzetta.it/dynamic-feed/rss/section/Calcio/coppe.xml"),
    ("Corriere dello Sport", "FUT EUROPEU", "https://www.corrieredellosport.it/rss/calcio"),
    ("Tuttosport", "FUT EUROPEU", "https://www.tuttosport.com/rss/calcio"),

    # ---------------- FRANÇA ----------------
    ("RMC Sport", "FUT EUROPEU", "https://rmcsport.bfmtv.com/rss/football/"),
    ("RMC Ligue 1", "FUT EUROPEU", "https://rmcsport.bfmtv.com/rss/football/ligue-1/"),
    ("RMC Champions", "FUT EUROPEU", "https://rmcsport.bfmtv.com/rss/football/ligue-des-champions/"),
    ("SO FOOT", "FUT EUROPEU", "https://www.sofoot.com/rss"),

    # ---------------- ALEMANHA ----------------
    ("Kicker", "FUT EUROPEU", "https://newsfeed.kicker.de/news/bundesliga"),
    ("Sportschau", "AUTO", "https://www.sportschau.de/index~rss2.xml"),
    ("Bulinews", "FUT EUROPEU", "https://bulinews.com/rss.xml"),

    # ---------------- PORTUGAL ----------------
    ("A Bola", "FUT EUROPEU", "https://abola.pt/rss-articles.xml"),
    ("Maisfutebol", "FUT EUROPEU", "https://maisfutebol.iol.pt/rss.xml"),

    # ---------------- ESPANHA (extras) ----------------
    ("SPORT", "FUT EUROPEU", "https://www.sport.es/es/rss/last-news/news.xml"),
    ("AS Champions", "FUT EUROPEU", "https://as.com/rss/futbol/champions.xml"),

    # ---------------- INGLATERRA (extras) ----------------
    ("talkSPORT", "FUT EUROPEU", "https://talksport.com/football/feed"),
    ("BBC Premier League", "FUT EUROPEU", "https://feeds.bbci.co.uk/sport/football/premier-league/rss.xml"),
    ("FourFourTwo", "FUT EUROPEU", "https://www.fourfourtwo.com/feeds.xml"),

    # ---------------- ARGENTINA / SUL-AMÉRICA (extras) ----------------
    ("Olé Últimas", "FUT SUL-AMERICANO", "https://www.ole.com.ar/rss/ultimas-noticias/"),
    ("Clarín Deportes", "FUT SUL-AMERICANO", "https://www.clarin.com/deportes/rss"),
    ("Infobae Deportes", "AUTO", "https://www.infobae.com/deportes/rss"),

    # ---------------- BASQUETE ----------------
    ("ge Basquete", "BASQUETE", "https://ge.globo.com/rss/ge/basquete/"),
    ("ESPN NBA", "BASQUETE", "https://www.espn.com/espn/rss/nba/news"),
    ("NBA.com", "BASQUETE", "https://www.nba.com/rss/nba_rss.xml"),

    # ---------------- FÓRMULA 1 ----------------
    ("ge Fórmula 1", "F1", "https://ge.globo.com/rss/ge/motor/formula-1/"),
    ("BBC F1", "F1", "https://feeds.bbci.co.uk/sport/formula1/rss.xml"),
    ("Motorsport", "F1", "https://www.motorsport.com/rss/f1/news/"),
    ("Autosport", "F1", "https://www.autosport.com/rss/f1/news/"),

    # ---------------- LUTAS ----------------
    ("ge Lutas", "LUTAS", "https://ge.globo.com/rss/ge/lutas/"),
    ("ESPN MMA", "LUTAS", "https://www.espn.com/espn/rss/mma/news"),
    ("BBC Boxe", "LUTAS", "https://feeds.bbci.co.uk/sport/boxing/rss.xml"),

    # ---------------- ESPORTE OLÍMPICO ----------------
    ("ge Olimpíadas", "ESPORTE OLÍMPICO", "https://ge.globo.com/rss/ge/olimpiadas/"),
    ("ge Atletismo", "ESPORTE OLÍMPICO", "https://ge.globo.com/rss/ge/atletismo/"),
    ("ge Natação", "ESPORTE OLÍMPICO", "https://ge.globo.com/rss/ge/natacao/"),
    ("BBC Olimpíadas", "ESPORTE OLÍMPICO", "https://feeds.bbci.co.uk/sport/olympics/rss.xml"),

    # ---------------- OUTROS ESPORTES ----------------
    ("ge Vôlei", "OUTROS ESPORTES", "https://ge.globo.com/rss/ge/volei/"),
    ("ge Tênis", "OUTROS ESPORTES", "https://ge.globo.com/rss/ge/tenis/"),
    ("ge Surfe", "OUTROS ESPORTES", "https://ge.globo.com/rss/ge/surfe/"),
    ("BBC Tênis", "OUTROS ESPORTES", "https://feeds.bbci.co.uk/sport/tennis/rss.xml"),
    ("BBC Sport", "AUTO", "https://feeds.bbci.co.uk/sport/rss.xml"),
]

# Canais do YouTube. O codigo do canal e descoberto sozinho pelo @.
CANAIS = [
    ("TNT Sports Brasil", "FUTEBOL BRASIL", "tntsportsbr"),
    ("ge tv", "FUTEBOL BRASIL", "getv"),
    ("CazéTV", "FUTEBOL BRASIL", "CazeTV"),
    ("ESPN Brasil", "FUTEBOL BRASIL", "ESPNBrasil"),
    ("Lance!", "FUTEBOL BRASIL", "lancenet"),
    ("Desimpedidos", "FUTEBOL BRASIL", "desimpedidos"),
    ("UEFA Champions League", "FUT EUROPEU", "uefa"),
    ("NBA", "BASQUETE", "NBA"),
    ("Fórmula 1", "F1", "Formula1"),
    ("UFC", "LUTAS", "UFC"),
    ("Olympics", "ESPORTE OLÍMPICO", "olympics"),
]

# ---------------------------------------------------------------------------
# Palavras que decidem a categoria quando o feed e "AUTO".
# A ordem importa: a primeira lista que casar vence.
# ---------------------------------------------------------------------------

FOFOCA = [
    "namorad", "afair", "affair", "casamento", "noiv", "divórcio", "divorcio",
    "separação", "separacao", "romance", "beijo", "festa", "aniversário de",
    "mansão", "mansao", "carrão", "carrao", "vida pessoal", "look", "tatuagem",
    "influenciadora", "modelo", "reality", "big brother", "bbb", "instagram",
    "polêmica nas redes", "polemica nas redes", "post", "story", "wag",
    "bruna biancardi", "virginia", "ex-mulher", "ex-namorada", "filho de",
    "curte", "flagra", "climão", "climao", "treta",
]

MERCADO = [
    "transferência", "transferencia", "calciomercato", "mercato", "fichaje",
    "contrata", "contratação", "contratacao", "reforço", "reforco",
    "assina com", "é o novo", "e o novo", "acordo com o",
    "acerta com", "negociação por", "negociacao por", "proposta por",
    "sondagem", "empréstimo", "emprestimo", "renovação de contrato",
    "renovacao de contrato", "janela de transferências", "deadline day",
    "here we go", "cláusula",
    "clausula", "livre no mercado", "rescisão", "rescisao",
    "anuncia a contratação", "anuncia a contratacao", "novo reforço",
    "transfer", "signing", "signs ", "joins ", "deal agreed", "bid for",
    "loan move", "medical scheduled", "release clause", "free agent"
]

MAPA = [
    ("F1", [
        "fórmula 1", "formula 1", "f1", "verstappen", "hamilton", "leclerc",
        "norris", "piastri", "ferrari", "mclaren", "red bull racing", "gp de",
        "grande prêmio", "grande premio", "pole position", "mercedes", "fia",
        "interlagos", "stock car", "fórmula e", "formula e", "motogp",
    ]),
    ("BASQUETE", [
        "nba", "basquete", "lebron", "curry", "doncic", "wembanyama", "nbb",
        "lakers", "celtics", "warriors", "knicks", "playoffs da nba",
    ]),
    ("LUTAS", [
        "ufc", "mma", "boxe", "nocaute", "octógono", "octogono", "jiu-jitsu",
        "jiu jitsu", "luta livre", "wwe", "peso pesado", "cinturão", "cinturao",
        "poatan", "pereira", "mcgregor", "canelo", "one championship",
    ]),
    ("ESPORTE OLÍMPICO", [
        "olimpíada", "olimpiada", "olímpico", "olimpico", "coi", "atletismo",
        "natação", "natacao", "ginástica", "ginastica", "judô", "judo",
        "esgrima", "remo", "canoagem", "vela", "handebol", "pan-americano",
        "paralímpic", "paralimpic", "maratona", "salto com vara", "revezamento",
    ]),
    ("OUTROS ESPORTES", [
        "vôlei", "volei", "tênis", "tenis", "wimbledon", "roland garros",
        "us open", "australian open", "nfl", "futebol americano", "super bowl",
        "beisebol", "mlb", "nhl", "hóquei", "hoquei", "golfe", "surfe", "skate",
        "ciclismo", "tour de france", "rugby", "críquete", "criquete", "xadrez",
        "e-sports", "esports", "cs2", "league of legends",
    ]),
    ("FUT SUL-AMERICANO", [
        "libertadores", "sul-americana", "sudamericana", "conmebol",
        "river plate", "boca juniors", "racing", "independiente", "peñarol",
        "penarol", "nacional de montevidéu", "colo-colo", "olimpia",
        "argentina", "uruguai", "paraguai", "chile", "colômbia", "colombia",
        "equador", "bolívia", "bolivia", "peru", "venezuela",
    ]),
    ("FUT EUROPEU", [
        "champions league", "liga dos campeões", "liga dos campeoes",
        "premier league", "laliga", "la liga", "bundesliga", "serie a italiana",
        "ligue 1", "europa league", "real madrid", "barcelona", "manchester",
        "liverpool", "arsenal", "chelsea", "tottenham", "psg", "bayern",
        "juventus", "milan", "inter de milão", "inter de milao", "atlético de madrid",
        "atletico de madrid", "mbappé", "mbappe", "haaland", "yamal", "bellingham",
        "eurocopa", "uefa", "espanha", "inglaterra", "frança", "franca",
        "alemanha", "itália", "italia", "portugal", "holanda",
    ]),
    ("FUTEBOL BRASIL", [
        "brasileirão", "brasileirao", "copa do brasil", "série a", "serie a",
        "série b", "serie b", "flamengo", "palmeiras", "corinthians",
        "são paulo", "sao paulo", "santos", "vasco", "fluminense", "botafogo",
        "grêmio", "gremio", "internacional", "cruzeiro", "atlético-mg",
        "atletico-mg", "bahia", "vitória", "vitoria", "fortaleza", "ceará",
        "ceara", "sport", "náutico", "nautico", "goiás", "goias", "coritiba",
        "athletico", "bragantino", "mirassol", "juventude", "cbf", "seleção",
        "selecao", "ancelotti", "neymar", "vini jr", "vinícius júnior",
        "carioca", "paulistão", "paulistao", "mineiro", "gaúcho", "gaucho",
    ]),
]


def classificar(titulo, resumo, categoria_padrao):
    """Decide a categoria de uma noticia."""
    texto = (titulo + " " + resumo).lower()

    for palavra in FOFOCA:
        if palavra in texto:
            return "FOFOCAS"

    for palavra in MERCADO:
        if palavra in texto:
            return "MERCADO"

    if categoria_padrao != "AUTO":
        return categoria_padrao

    for categoria, palavras in MAPA:
        for palavra in palavras:
            if palavra in texto:
                return categoria

    return "OUTROS ESPORTES"
