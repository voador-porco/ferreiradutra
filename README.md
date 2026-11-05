# Ferreira e Dutra Advogados

> **Vai copiar este site?** Comece pelo [LEIA-ME.md](LEIA-ME.md).

Site do escritório Ferreira e Dutra Advogados (Uberlândia, MG): uma página central e uma página por área do direito, cada uma pronta para receber tráfego pago.
Estático, sem dependências: `python3 build.py` gera as páginas e a ponte `/obrigado`, que leva ao WhatsApp com a mensagem da área.

## Páginas
- `/` página central: o escritório, as áreas, os diferenciais, como funciona, o alcance e as dúvidas.
- `/criminal`, `/inventario`, `/familia`, `/civel`, `/transito`, `/administrativo`: uma landing por área.
- `/obrigado?c=<botão>&a=<área>`: registra a conversão no `dataLayer` (com o contexto e a área) e abre o WhatsApp com a mensagem daquela área.

## De onde veio cada coisa
- **Textos:** `conteudo.py`, a partir do formulário de público-alvo que o Luiz respondeu. Não há promessa de resultado, preço, consulta grátis nem depoimento, por causa do Provimento 205/2021 da OAB.
- **Fotos:** `python3 tools/fotos.py` gera os retratos, os recortes do topo e o ícone. Os originais ficam em `assets/src/fotos/`.
  - A foto da Ludmilla veio cortada na testa e nos braços. O Firefly completou a imagem (`ludmilla-expandida.jpg`) e depois o fundo foi tirado.
  - Nos recortes, a borda é contraída e escurecida para não sobrar a linha branca do fundo antigo.
- **Fundos:** gerados no ChatGPT (originais em `assets/src/geradas/`), em 16:9 e, na página central, também em 4:5 para o celular. `python3 tools/fundos.py` gera os WebP. Sempre com véu escuro por cima, para o texto ler bem.
- **Nome e letras a traço:** `tools/letreiro.py` transforma a Cormorant Garamond em contorno SVG. A página não carrega fonte serifada.
- **Mapa:** `tools/mapa.py`, contorno do Brasil da Natural Earth (domínio público).
- **Imagem de compartilhamento:** `python3 tools/og.py`, com o servidor local ligado.

## Falta o cliente mandar (aparece como [A PREENCHER])
- Número do WhatsApp (`WHATSAPP` e `TEL_VER` no `build.py`). Sem ele, os botões abrem o WhatsApp sem destinatário.
- Número da OAB dos dois (`SOCIOS` no `build.py`). Confirmar também se o nome completo da Ludmilla é só "Ludmilla Ferreira".
- Endereço do escritório, se quiserem mostrar.
- O advogado precisa ler as páginas e confirmar os prazos e regras citados, como os 2 meses do inventário, os 15 dias úteis do cível e a cassação da CNH por 2 anos.
- Domínio: depois de ligar, trocar `DOMINIO` e virar `INDEXAR = True`.

## Prévia local
`python3 tools/serve.py 4235`

## Para usar como base de outro site
1. `git clone https://github.com/voador-porco/ferreiradutra.git novo-site`, e aponte o `origin` para um repositório seu (`git remote set-url origin <url>`). Este repositório não aceita push de terceiros.
2. Dependências: `pip3 install pillow fonttools`. Para regerar fotos e a imagem de compartilhamento, também `pip3 install playwright numpy` e `playwright install chromium`. O recorte sem fundo (`tools/lift.swift`) só roda no Mac.
3. Textos: `conteudo.py`. Nome, WhatsApp, sócios e domínio: início do `build.py`. As letras F e D estão na função `capa()` e em `equipe()`; o nome no cabeçalho é a constante `_NOME`.
4. Fotos: troque os arquivos em `assets/src/fotos/` e rode `python3 tools/fotos.py`. Fundos: `assets/src/geradas/` e `python3 tools/fundos.py`.
5. `python3 build.py` gera as páginas. Publicar é só importar o repositório novo na Vercel (o `.vercelignore` deixa os originais e os scripts fora do ar).
