# LEIA-ME: copie este site idêntico

Este arquivo é para o Matheus e para o Claude dele. Claude, siga as instruções abaixo ao pé da letra.

## A regra principal

**Copie tudo idêntico.** Layout, animações, cores, fontes, tamanhos, pastas, nomes de arquivo e scripts ficam exatamente como estão. Não redesenhe, não reorganize e não "melhore" nada por conta própria.

O projeto foi revisado seção por seção e cada detalhe foi aprovado. Só mude o que o Matheus pedir, e só depois de a cópia estar rodando igual à original.

## Passo 1: fazer a cópia

```bash
git clone https://github.com/leonardoferreirr/ferreiradutra.git novo-site
cd novo-site
git remote remove origin
pip3 install pillow fonttools
python3 build.py
python3 tools/serve.py 4235
```

Abra http://localhost:4235 e confira a página central e uma página de área, como `/criminal`.

**Como saber que ficou idêntico:** depois do `build.py`, o `git status` não pode mostrar nenhum arquivo alterado. Em outro dia, só o `sitemap.xml` pode mudar, porque ele traz a data. Qualquer outra diferença indica que algo saiu errado: resolva antes de continuar.

Este repositório é só leitura: não dá para enviar alterações para ele. Quando quiser publicar, crie um repositório próprio com `git remote add origin <url-do-seu-repositório>` e faça o push. Depois é só importar na Vercel.

## Passo 2: trocar só o que muda de cliente

Faça isso apenas quando o Matheus pedir, e sempre rode `python3 build.py` depois.

| O que muda | Onde |
|---|---|
| Domínio, WhatsApp, nome, cidade, sócios e OAB | início do `build.py` |
| Título do topo da página central | `HERO_H1` no `build.py` |
| Todos os textos e as áreas de atuação | `conteudo.py` |
| Fotos dos sócios | `assets/src/fotos/`, depois `python3 tools/fotos.py` |
| Imagens de fundo | `assets/src/geradas/`, depois `python3 tools/fundos.py` |
| Letras grandes a traço (F e D) | funções `capa()` e `equipe()` no `build.py` |
| Nome no cabeçalho | constante `_NOME` no `build.py` |

Para regerar fotos e a imagem de compartilhamento, instale também: `pip3 install playwright numpy` e `playwright install chromium`. O recorte sem fundo (`tools/lift.swift`) só roda no Mac.

Antes de ir ao ar, procure `[A PREENCHER]` nos textos e substitua pelos dados reais. Com `WHATSAPP` vazio no `build.py`, os botões abrem o WhatsApp sem destinatário. Quando o domínio estiver ligado, troque `DOMINIO` e passe `INDEXAR` para `True`.

## Decisões que devem continuar valendo

Elas foram pedidas na revisão. Não desfaça:

- **Topo:** nome no centro e título abaixo. Cada sócio fica em um lado, sobre a inicial do próprio sobrenome.
- **Botões de ação:** verdes, a única quebra de cor na paleta. O botão fixo é só a bolinha com o ícone do WhatsApp.
- **Celular:** botões empilhados sempre com a mesma largura.
- **Cabeçalho:** logo à esquerda, botão à direita e links no centro do espaço entre os dois.
- **Títulos:** Poppins, sem etiqueta ou texto pequeno acima. A serifa fica só no nome e nas letras a traço.
- **Dúvidas frequentes:** é a única seção sem botão de ação.
- **Imagens de fundo:** cada uma precisa fazer sentido com a frase da seção, e não só ser bonita.
- **Textos:** sem travessão e sem jargão.
- **Ponte do WhatsApp:** todo botão passa pela página `/obrigado`, que registra a conversão antes de abrir a conversa.

## Se o próximo site também for de advocacia

Os textos seguem o Provimento 205/2021 da OAB: sem promessa de resultado, sem preço, sem consulta grátis e sem depoimento de cliente. Mantenha isso. Os prazos legais citados em `conteudo.py` precisam ser revisados pelo advogado do novo cliente antes de publicar.

Mais detalhes técnicos estão no `README.md`.
