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
    "OUTROS ESPORTES",
    "FOFOCAS",
]

# (nome exibido, categoria padrao, endereco do feed)
# categoria "AUTO" = decidir pelo assunto do titulo.
FEEDS = [
    # ---------------- FUTEBOL BRASILEIRO ----------------
    ("Globo Esporte Futebol", "FUTEBOL BRASIL", "https://ge.globo.com/rss/ge/futebol/"),
    ("Globo Esporte Brasileirão", "FUTEBOL BRASIL", "https://ge.globo.com/rss/ge/futebol/brasileirao-serie-a/"),
    ("Globo Esporte Copa do Brasil", "FUTEBOL BRASIL", "https://ge.globo.com/rss/ge/futebol/copa-do-brasil/"),
    # Notícias por clube: o ge não publica mais feed próprio de time,
    # então cada clube vem por uma busca do Google Notícias restrita ao ge.globo.com.
    ("Globo Esporte / Flamengo", "FUTEBOL BRASIL", "https://news.google.com/rss/search?q=site:ge.globo.com+Flamengo&hl=pt-BR&gl=BR&ceid=BR:pt-419"),
    ("Globo Esporte / Palmeiras", "FUTEBOL BRASIL", "https://news.google.com/rss/search?q=site:ge.globo.com+Palmeiras&hl=pt-BR&gl=BR&ceid=BR:pt-419"),
    ("Globo Esporte / Corinthians", "FUTEBOL BRASIL", "https://news.google.com/rss/search?q=site:ge.globo.com+Corinthians&hl=pt-BR&gl=BR&ceid=BR:pt-419"),
    ("Globo Esporte / São Paulo", "FUTEBOL BRASIL", "https://news.google.com/rss/search?q=site:ge.globo.com+%22S%C3%A3o+Paulo%22+futebol&hl=pt-BR&gl=BR&ceid=BR:pt-419"),
    ("Globo Esporte / Vasco", "FUTEBOL BRASIL", "https://news.google.com/rss/search?q=site:ge.globo.com+Vasco&hl=pt-BR&gl=BR&ceid=BR:pt-419"),
    ("Globo Esporte / Fluminense", "FUTEBOL BRASIL", "https://news.google.com/rss/search?q=site:ge.globo.com+Fluminense&hl=pt-BR&gl=BR&ceid=BR:pt-419"),
    ("Globo Esporte / Botafogo", "FUTEBOL BRASIL", "https://news.google.com/rss/search?q=site:ge.globo.com+Botafogo&hl=pt-BR&gl=BR&ceid=BR:pt-419"),
    ("Globo Esporte / Grêmio", "FUTEBOL BRASIL", "https://news.google.com/rss/search?q=site:ge.globo.com+Gr%C3%AAmio&hl=pt-BR&gl=BR&ceid=BR:pt-419"),
    ("Globo Esporte / Internacional", "FUTEBOL BRASIL", "https://news.google.com/rss/search?q=site:ge.globo.com+Internacional+futebol&hl=pt-BR&gl=BR&ceid=BR:pt-419"),
    ("Globo Esporte / Cruzeiro", "FUTEBOL BRASIL", "https://news.google.com/rss/search?q=site:ge.globo.com+Cruzeiro&hl=pt-BR&gl=BR&ceid=BR:pt-419"),
    ("Globo Esporte / Atlético-MG", "FUTEBOL BRASIL", "https://news.google.com/rss/search?q=site:ge.globo.com+%22Atl%C3%A9tico-MG%22&hl=pt-BR&gl=BR&ceid=BR:pt-419"),
    ("Globo Esporte / Santos", "FUTEBOL BRASIL", "https://news.google.com/rss/search?q=site:ge.globo.com+Santos+futebol&hl=pt-BR&gl=BR&ceid=BR:pt-419"),
    ("Globo Esporte Seleção", "FUTEBOL BRASIL", "https://ge.globo.com/rss/ge/futebol/selecao-brasileira/"),
    ("Lance!", "FUTEBOL BRASIL", "https://www.lance.com.br/feed"),
    # Reforço do noticiário nacional: vários feeds próprios saem do ar sem
    # aviso, então estas buscas garantem cobertura mesmo quando isso acontece.
    ("Brasileirão", "FUTEBOL BRASIL", "https://news.google.com/rss/search?q=Brasileir%C3%A3o+quando:1d&hl=pt-BR&gl=BR&ceid=BR:pt-419"),
    ("Copa do Brasil", "FUTEBOL BRASIL", "https://news.google.com/rss/search?q=%22Copa+do+Brasil%22+futebol+quando:1d&hl=pt-BR&gl=BR&ceid=BR:pt-419"),
    ("Seleção Brasileira", "FUTEBOL BRASIL", "https://news.google.com/rss/search?q=%22Sele%C3%A7%C3%A3o+Brasileira%22+quando:2d&hl=pt-BR&gl=BR&ceid=BR:pt-419"),
    ("UOL Esporte / Futebol", "FUTEBOL BRASIL", "https://news.google.com/rss/search?q=site:uol.com.br+futebol+quando:1d&hl=pt-BR&gl=BR&ceid=BR:pt-419"),
    ("Lance! / Busca", "FUTEBOL BRASIL", "https://news.google.com/rss/search?q=site:lance.com.br+quando:1d&hl=pt-BR&gl=BR&ceid=BR:pt-419"),
    ("Gazeta Esportiva / Busca", "FUTEBOL BRASIL", "https://news.google.com/rss/search?q=site:gazetaesportiva.com+quando:1d&hl=pt-BR&gl=BR&ceid=BR:pt-419"),
    ("Gazeta Esportiva", "FUTEBOL BRASIL", "https://www.gazetaesportiva.com/feed/"),
    ("Placar", "FUTEBOL BRASIL", "https://placar.abril.com.br/feed/"),
    ("Trivela", "AUTO", "https://trivela.com.br/feed/"),

    # ---------------- GERAIS (classificados pelo assunto) ----------------
    ("Globo Esporte", "AUTO", "https://ge.globo.com/rss/ge/"),
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
    ("MARCA Primeira", "FUT EUROPEU", "https://e00-marca.uecdn.es/rss/futbol/primera-division.xml"),
    ("MARCA Portada", "AUTO", "https://e00-marca.uecdn.es/rss/portada.xml"),
    ("AS", "FUT EUROPEU", "https://as.com/rss/futbol/primera.xml"),
    ("AS Portada", "AUTO", "https://as.com/rss/portada.xml"),
    ("ESPN FC", "FUT EUROPEU", "https://www.espn.com/espn/rss/soccer/news"),
    ("Goal", "FUT EUROPEU", "https://www.goal.com/feeds/en/news"),
    ("Globo Esporte Futebol Internacional", "FUT EUROPEU", "https://ge.globo.com/rss/ge/futebol/futebol-internacional/"),

    # ---------------- FUTEBOL SUL-AMERICANO ----------------
    ("Globo Esporte Libertadores", "FUT SUL-AMERICANO", "https://ge.globo.com/rss/ge/futebol/libertadores/"),
    ("Globo Esporte Sul-Americana", "FUT SUL-AMERICANO", "https://ge.globo.com/rss/ge/futebol/copa-sul-americana/"),
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

    # ---------------- ESPN / CBS / ENTIDADES ----------------
    ("ESPN", "AUTO", "https://www.espn.com/espn/rss/news"),
    ("ESPN Brasil", "AUTO", "https://news.google.com/rss/search?q=site:espn.com.br&hl=pt-BR&gl=BR&ceid=BR:pt-419"),
    ("CBS Sports Futebol", "FUT EUROPEU", "https://www.cbssports.com/rss/headlines/soccer/"),
    ("CBS Sports", "AUTO", "https://www.cbssports.com/rss/headlines/"),
    ("CBS Sports NBA", "OUTROS ESPORTES", "https://www.cbssports.com/rss/headlines/nba/"),
    # FIFA, CBF e Bleacher Report não publicam feed próprio: vêm por busca
    # do Google Notícias restrita ao domínio de cada um.
    ("FIFA", "AUTO", "https://news.google.com/rss/search?q=site:fifa.com&hl=pt-BR&gl=BR&ceid=BR:pt-419"),
    ("CBF", "FUTEBOL BRASIL", "https://news.google.com/rss/search?q=site:cbf.com.br&hl=pt-BR&gl=BR&ceid=BR:pt-419"),
    ("Bleacher Report", "AUTO", "https://news.google.com/rss/search?q=site:bleacherreport.com&hl=en-US&gl=US&ceid=US:en"),

    # ---------------- BASQUETE ----------------
    ("Globo Esporte Basquete", "OUTROS ESPORTES", "https://ge.globo.com/rss/ge/basquete/"),
    ("ESPN NBA", "OUTROS ESPORTES", "https://www.espn.com/espn/rss/nba/news"),
    ("NBA.com", "OUTROS ESPORTES", "https://www.nba.com/rss/nba_rss.xml"),

    # ---------------- FÓRMULA 1 ----------------
    ("Fórmula 1 Brasil", "OUTROS ESPORTES", "https://news.google.com/rss/search?q=%22F%C3%B3rmula+1%22&hl=pt-BR&gl=BR&ceid=BR:pt-419"),
    ("BBC F1", "OUTROS ESPORTES", "https://feeds.bbci.co.uk/sport/formula1/rss.xml"),
    ("Motorsport", "OUTROS ESPORTES", "https://www.motorsport.com/rss/f1/news/"),
    ("Autosport", "OUTROS ESPORTES", "https://www.autosport.com/rss/f1/news/"),

    # ---------------- LUTAS ----------------
    ("Lutas Brasil", "OUTROS ESPORTES", "https://news.google.com/rss/search?q=UFC+OR+MMA+OR+boxe&hl=pt-BR&gl=BR&ceid=BR:pt-419"),
    ("ESPN MMA", "OUTROS ESPORTES", "https://www.espn.com/espn/rss/mma/news"),
    ("BBC Boxe", "OUTROS ESPORTES", "https://feeds.bbci.co.uk/sport/boxing/rss.xml"),

    # ---------------- ESPORTE OLÍMPICO ----------------
    ("Globo Esporte Olimpíadas", "OUTROS ESPORTES", "https://ge.globo.com/rss/ge/olimpiadas/"),
    ("Olímpicos Brasil", "OUTROS ESPORTES", "https://news.google.com/rss/search?q=atletismo+OR+gin%C3%A1stica+OR+nata%C3%A7%C3%A3o+brasileiro&hl=pt-BR&gl=BR&ceid=BR:pt-419"),
    ("NBA Brasil", "OUTROS ESPORTES", "https://news.google.com/rss/search?q=NBA+OR+basquete&hl=pt-BR&gl=BR&ceid=BR:pt-419"),
    ("BBC Olimpíadas", "OUTROS ESPORTES", "https://feeds.bbci.co.uk/sport/olympics/rss.xml"),

    # ---------------- OUTROS ESPORTES ----------------
    ("Globo Esporte Vôlei", "OUTROS ESPORTES", "https://ge.globo.com/rss/ge/volei/"),
    ("Globo Esporte Tênis", "OUTROS ESPORTES", "https://ge.globo.com/rss/ge/tenis/"),
    ("Vôlei e Tênis Brasil", "OUTROS ESPORTES", "https://news.google.com/rss/search?q=v%C3%B4lei+OR+t%C3%AAnis+brasileiro&hl=pt-BR&gl=BR&ceid=BR:pt-419"),
    ("BBC Tênis", "OUTROS ESPORTES", "https://feeds.bbci.co.uk/sport/tennis/rss.xml"),
    ("BBC Sport", "AUTO", "https://feeds.bbci.co.uk/sport/rss.xml"),
]

# Canais do YouTube. O codigo do canal e descoberto sozinho pelo @.
CANAIS = [
    ("TNT Sports Brasil", "FUTEBOL BRASIL", "tntsportsbr"),
    ("Globo Esporte tv", "FUTEBOL BRASIL", "getv"),
    ("CazéTV", "FUTEBOL BRASIL", "CazeTV"),
    ("ESPN Brasil", "FUTEBOL BRASIL", "ESPNBrasil"),
    ("Lance!", "FUTEBOL BRASIL", "lancenet"),
    ("Desimpedidos", "FUTEBOL BRASIL", "desimpedidos"),
    ("UEFA Champions League", "FUT EUROPEU", "uefa"),
    ("NBA", "OUTROS ESPORTES", "NBA"),
    ("Fórmula 1", "OUTROS ESPORTES", "Formula1"),
    ("UFC", "OUTROS ESPORTES", "UFC"),
    ("Olympics", "OUTROS ESPORTES", "olympics"),
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
    ("OUTROS ESPORTES", [
        "fórmula 1", "formula 1", "f1", "verstappen", "hamilton", "leclerc",
        "norris", "piastri", "ferrari", "mclaren", "red bull racing", "gp de",
        "grande prêmio", "grande premio", "pole position", "mercedes", "fia",
        "interlagos", "stock car", "fórmula e", "formula e", "motogp",
    ]),
    ("OUTROS ESPORTES", [
        "nba", "basquete", "lebron", "curry", "doncic", "wembanyama", "nbb",
        "lakers", "celtics", "warriors", "knicks", "playoffs da nba",
    ]),
    ("OUTROS ESPORTES", [
        "ufc", "mma", "boxe", "nocaute", "octógono", "octogono", "jiu-jitsu",
        "jiu jitsu", "luta livre", "wwe", "peso pesado", "cinturão", "cinturao",
        "poatan", "pereira", "mcgregor", "canelo", "one championship",
    ]),
    ("OUTROS ESPORTES", [
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
