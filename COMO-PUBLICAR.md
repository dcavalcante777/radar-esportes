# Radar Esportes — como colocar no ar no GitHub Pages

Tempo estimado: 15 minutos. Tudo pelo navegador, sem instalar nada.

## Os arquivos deste pacote

| Arquivo | Para que serve |
|---|---|
| `index.html` | A página em si. É o que fica no ar. |
| `atualizar_noticias.py` | A rotina que busca as manchetes e regrava o resumo dentro do `index.html`. |
| `workflow-atualizar.yml` | A programação que manda o GitHub rodar essa rotina sozinho, 3x por dia. |

---

## Passo 1 — Criar a conta e o repositório

1. Acesse **github.com** e crie uma conta gratuita (ou entre na sua).
2. Clique no **+** no canto superior direito → **New repository**.
3. Em *Repository name*, escreva: **radar-esportes**
4. Marque **Public**. (O Pages gratuito só funciona em repositório público.)
5. Clique em **Create repository**.

## Passo 2 — Subir os arquivos

1. Na tela do repositório recém-criado, clique em **uploading an existing file**.
2. Arraste o **`index.html`** e o **`atualizar_noticias.py`**.
3. Clique em **Commit changes**.

## Passo 3 — Ligar o GitHub Pages

1. No repositório, abra a aba **Settings** → menu lateral **Pages**.
2. Em *Source*, escolha **Deploy from a branch**.
3. Em *Branch*, escolha **main** e a pasta **/ (root)**. Clique em **Save**.
4. Espere 1 a 2 minutos e recarregue a página. Vai aparecer o endereço:

   `https://SEU-USUARIO.github.io/radar-esportes/`

Pronto — a página já está no ar e busca as notícias ao vivo toda vez que alguém abre.

## Passo 4 — Ligar a atualização automática

1. No repositório, clique em **Add file** → **Create new file**.
2. No campo do nome, escreva exatamente:

   `.github/workflows/atualizar.yml`

   (Ao digitar cada barra, o GitHub cria a pasta sozinho.)
3. Abra o arquivo **`workflow-atualizar.yml`** deste pacote, copie todo o conteúdo e cole na caixa de texto.
4. Clique em **Commit changes**.

A partir daí o GitHub roda a rotina sozinho às **9h, 15h e 21h** (horário de Brasília), busca as manchetes novas e regrava a página. Você não precisa fazer mais nada.

Para rodar na hora e testar: aba **Actions** → **Atualizar Radar Esportes** → botão **Run workflow**.

---

## Dicas e ajustes

**Mudar o horário.** No `atualizar.yml`, a linha `cron: "0 12,18 * * *"` está em UTC. Brasília é UTC−3, então 12 UTC = 9h daqui e 18 UTC = 15h. Para outro horário, some 3 ao horário desejado.

**Incluir ou tirar um site.** Os sites ficam listados em dois lugares: na lista `FEEDS` dentro do `atualizar_noticias.py` e na lista `FEEDS` dentro do `index.html`. Mantenha as duas iguais. Cada linha segue o padrão `("Nome do site", "Brasil|Europa|Outros", "endereço do feed")`.

**Trocar as contas do X.** No `index.html`, procure por `X_ACCOUNTS` e edite a lista — `n` é o nome que aparece e `h` é o @ da conta.

**Se uma atualização der errado.** A rotina é protegida: se ela não conseguir buscar pelo menos 5 manchetes, ela não mexe no arquivo e o resumo anterior continua no ar. Nada quebra.

**Endereço público.** Qualquer pessoa com o link consegue abrir. O conteúdo é só manchete pública de portais, mas se você quiser colocar logo ou identidade visual da TNT Sports na página, alinhe antes com o time de marca.

**Domínio próprio.** Se um dia quiser um endereço tipo `radar.seudominio.com.br`, dá pra apontar em Settings → Pages → Custom domain.
