#!/usr/bin/env python3
"""Monta o site da Ferreira e Dutra Advogados: página central, uma página por área e a ponte /obrigado para o WhatsApp.

    python3 build.py

Textos em conteudo.py (escritos a partir do formulário de público-alvo que o Luiz respondeu, sem prometer resultado,
sem preço e sem consulta grátis, por causa do Provimento 205/2021 da OAB). Fotos: tools/fotos.py.
O nome do escritório e as letras grandes a traço saem da Cormorant Garamond como contorno SVG (tools/letreiro.py),
então a página não carrega fonte serifada. O CSS vai minificado no <head>; o site.js leva o hash do conteúdo no nome.
"""
import hashlib, json, re, sys
from datetime import date
from html import escape as e
from pathlib import Path

RAIZ = Path(__file__).parent
sys.path.insert(0, str(RAIZ / "tools"))
from conteudo import ESCRITORIO as ESC, AREAS            # noqa: E402
from letreiro import contorno                            # noqa: E402
from mapa import svg as mapa_svg                         # noqa: E402

DOMINIO = "https://ferreiradutra.vercel.app"
INDEXAR = False                  # True depois da aprovação e do domínio
WHATSAPP = ""                    # [A PREENCHER] número com DDI e DDD, só dígitos (ex.: 5534...)
TEL_VER = "[A PREENCHER]"        # o mesmo número, para leitura
NOME = "Ferreira e Dutra Advogados"
CIDADE = "Uberlândia, MG"
SOCIOS = [  # (nome, papel, OAB, foto)
    ("Luiz Fellipy Dutra e Sousa", "Advogado sócio", "OAB/MG [A PREENCHER]", "luiz"),
    ("Ludmilla", "Advogada sócia", "OAB/MG [A PREENCHER]", "ludmilla"),   # [A PREENCHER] sobrenome
]
HERO_H1 = "Criminal, família, sucessões e cível."
CSS, JS = RAIZ / "assets/css/site.css", RAIZ / "assets/js/site.js"
POR_SLUG = {a["slug"]: a for a in AREAS}

SETA = '<svg viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M2 8h11M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.5"/></svg>'
SETA_B = '<svg viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M2 4.5l4 4 4-4" stroke="currentColor" stroke-width="1.4"/></svg>'
ZAP = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.4.8 3.2.6a2.8 2.8 0 0 0 1.8-1.3 2.3 2.3 0 0 0 .2-1.3c-.1-.1-.3-.2-.6-.3z"/></svg>')


# ------------------------------------------------------------------ desenhos a traço
_NOME = contorno("Ferreira & Dutra", peso=500)


def nome_svg(classe="marca__nome"):
    d, w, asc, desc = _NOME
    return (f'<svg class="{classe}" viewBox="0 {-asc} {w:.0f} {asc + desc}" aria-hidden="true">'
            f'<use href="#fd-nome"/></svg>')


def defs_svg():
    d, *_ = _NOME
    return f'<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs><path id="fd-nome" d="{d}"/></defs></svg>'


def letra(texto, classe, peso=400):
    """Palavra desenhada a traço (o contorno da letra serifada aparece aos poucos)."""
    d, w, asc, desc = contorno(texto, peso=peso)
    return (f'<svg class="{classe}" viewBox="0 {-asc} {w:.0f} {asc + desc}" aria-hidden="true">'
            f'<path pathLength="1" d="{d}"/></svg>')


def numeral(n):
    d, w, asc, desc = contorno(f"{n:02d}", peso=400)
    alto = asc * .72                                       # algarismo sem a sobra do ascendente
    return f'<svg viewBox="0 {-alto:.0f} {w:.0f} {alto + 20:.0f}" aria-hidden="true"><path pathLength="1" d="{d}"/></svg>'


# ------------------------------------------------------------------ utilidades
def minificar(css):
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s*\n\s*", "\n", css)
    css = re.sub(r"\s*([{}:;,>])\s*", r"\1", css)
    css = re.sub(r";}", "}", css)
    return re.sub(r"\n+", "", css).replace("../fonts/", "/assets/fonts/").strip()


def hash_de(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:10] if p.exists() else "0"


def foto(nome, alt, sizes, lazy=True, larguras=(480, 720, 960), classe="", sufixo="w"):
    """<img> a partir de assets/img/fotos/<nome>-<tamanho>.webp, com as dimensões reais."""
    w, h = 800, 1000
    try:
        from PIL import Image
        with Image.open(RAIZ / f"assets/img/fotos/{nome}-{larguras[-1]}.webp") as im:
            w, h = im.size
    except Exception:
        print(f"  ! foto faltando: {nome}-{larguras[-1]}.webp")
    if sufixo == "w":
        srcset = ", ".join(f"/assets/img/fotos/{nome}-{x}.webp {x}w" for x in larguras)
    else:                                                  # recortes: o número é a altura; o srcset vai pela largura real
        from PIL import Image
        partes = []
        for x in larguras:
            with Image.open(RAIZ / f"assets/img/fotos/{nome}-{x}.webp") as im:
                partes.append(f"/assets/img/fotos/{nome}-{x}.webp {im.size[0]}w")
        srcset = ", ".join(partes)
    lz = ' loading="lazy"' if lazy else ' fetchpriority="high"'
    cl = f' class="{classe}"' if classe else ""
    return (f'<img{cl} src="/assets/img/fotos/{nome}-{larguras[-1]}.webp" srcset="{srcset}" sizes="{sizes}" alt="{e(alt)}" '
            f'width="{w}" height="{h}"{lz} decoding="async">')


def cta(rotulo="Falar com o escritório", c="cta", a="", tipo="pri"):
    q = f"c={c}" + (f"&amp;a={a}" if a else "")
    return f'<a class="btn btn--{tipo}" href="/obrigado?{q}">{ZAP if tipo == "pri" else ""}<span>{e(rotulo)}</span></a>'


def ld(obj):
    return f'<script type="application/ld+json">{json.dumps(obj, ensure_ascii=False, separators=(",", ":"))}</script>'


def faq_html(itens):
    return "".join(f'<details class="faq__item"><summary>{e(p)}<i aria-hidden="true"></i></summary><p>{e(r)}</p></details>' for p, r in itens)


def palavras(txt):
    return " ".join(f"<span>{e(p)}</span>" for p in txt.split())


# ------------------------------------------------------------------ casca
def pagina(titulo, desc, corpo, rota="/", preload="", robots=None, casca=True, extra="", classe=""):
    robots = robots or ("index,follow,max-image-preview:large" if INDEXAR else "noindex,nofollow")
    menu_areas = "".join(
        '<a href="/%s"%s>%s<i>%02d</i></a>' % (a["slug"], ' aria-current="page"' if rota == "/" + a["slug"] else "", e(a["nome"]), i + 1)
        for i, a in enumerate(AREAS))
    topo = f'''<header class="top"><div class="wrap top__in">
  <a class="marca" href="/" aria-label="{NOME}, início">{nome_svg()}<span>Advogados</span></a>
  <nav class="nav" aria-label="Principal">
    <div class="nav__areas"><button class="nav__bt" type="button" aria-expanded="false" aria-controls="menu-areas">Áreas{SETA_B}</button><div class="nav__menu" id="menu-areas">{menu_areas}</div></div>
    <a href="/#escritorio">O escritório</a><a href="/#como">Como funciona</a><a href="/#duvidas">Dúvidas</a>
  </nav>
  {cta("Falar com o escritório", "topo")}
  <button class="menu-bt" type="button" aria-expanded="false" aria-controls="menu" aria-label="Abrir o menu"><i></i></button>
</div></header>
<div class="menu" id="menu"><nav aria-label="Menu">{menu_areas}<a href="/#escritorio">O escritório<i></i></a><a href="/#duvidas">Dúvidas<i></i></a></nav>
  <div class="menu__extra">{cta("Falar com o escritório", "menu")}<span>{CIDADE} · atendimento em todo o Brasil</span></div></div>''' if casca else ""
    socios = "".join(f"<li>{e(n)} · {e(o)}</li>" for n, _, o, _ in SOCIOS)
    rodape = f'''<footer class="rod"><div class="wrap rod__in">
  <div class="rod__marca"><a class="marca" href="/" aria-label="{NOME}, início">{nome_svg()}<span>Advogados</span></a>
    <p>Criminal, família e sucessões, cível, trânsito e administrativo. {CIDADE}, com atendimento em todo o Brasil por processo eletrônico.</p>
    <ul>{socios}</ul></div>
  <div class="rod__col"><h2>Áreas</h2><ul>{"".join(f'<li><a href="/{a["slug"]}">{e(a["nome"])}</a></li>' for a in AREAS)}</ul></div>
  <div class="rod__col"><h2>Contato</h2><ul><li><a href="/obrigado?c=rodape">WhatsApp {e(TEL_VER)}</a></li><li>{CIDADE}</li><li><a href="/#duvidas">Dúvidas frequentes</a></li><li><a href="/privacidade">Política de privacidade</a></li></ul></div>
</div><div class="wrap rod__fim"><span>© {date.today().year} {NOME}.</span><span>Conteúdo informativo. Não substitui a análise do seu caso por um advogado.</span></div></footer>
<a class="zap" href="/obrigado?c=flutuante" aria-label="Falar com o escritório pelo WhatsApp">{ZAP}<span>Falar com o escritório</span></a>''' if casca else ""
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(titulo)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{DOMINIO}{rota}">
<meta name="theme-color" content="#14171A">
<meta property="og:type" content="website"><meta property="og:locale" content="pt_BR"><meta property="og:site_name" content="{NOME}">
<meta property="og:title" content="{e(titulo)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{DOMINIO}{rota}">
<meta property="og:image" content="{DOMINIO}/assets/img/og-v1.jpg"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/img/favicon-v1.svg" type="image/svg+xml"><link rel="icon" href="/assets/img/favicon-v1.png" type="image/png" sizes="64x64"><link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/poppins-300.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/poppins-500.woff2" as="font" type="font/woff2" crossorigin>
{preload}
<script>document.documentElement.classList.add('js')</script>
<style>{minificar(CSS.read_text())}</style>
{extra}
</head>
<body class="{classe}">
{defs_svg()}
{topo}
<main>
{corpo}
</main>
{rodape}
<script src="/assets/js/site.js?v={hash_de(JS)}" defer></script>
</body>
</html>'''


def capa(h1, p, ctas, marca=False, area=""):
    """Topo de todas as páginas: o texto no centro, o Luiz à esquerda sobre o F e a Ludmilla à direita sobre o D."""
    lockup = (f'<div class="capa__marca">{nome_svg("capa__nome")}<span>Advogados</span></div>' if marca else "")
    return f'''<section class="capa{" capa--area" if area else ""}" id="inicio">
  <div class="capa__palco" aria-hidden="true">
    <div class="lado lado--l">{letra("F", "letra")}<div class="lado__luz"></div>{foto("luiz-recorte", "", "(max-width:1000px) 54vw, 34vw", lazy=False, larguras=(560, 900), classe="lado__foto", sufixo="h")}</div>
    <div class="lado lado--r">{letra("D", "letra")}<div class="lado__luz"></div>{foto("ludmilla-recorte", "", "(max-width:1000px) 52vw, 30vw", lazy=False, larguras=(560, 900), classe="lado__foto", sufixo="h")}</div>
  </div>
  <div class="wrap capa__txt">
    {lockup}
    <h1>{h1}</h1>
    {f'<p>{e(p)}</p>' if p else ''}
    <div class="ctas">{ctas}</div>
  </div>
</section>'''


def schema_escritorio(extra=None):
    g = [{"@type": "LegalService", "@id": f"{DOMINIO}/#escritorio", "name": NOME, "url": f"{DOMINIO}/",
          "image": f"{DOMINIO}/assets/img/og-v1.jpg", "areaServed": "BR",
          "address": {"@type": "PostalAddress", "addressLocality": "Uberlândia", "addressRegion": "MG", "addressCountry": "BR"},
          "knowsAbout": [a["nome"] for a in AREAS],
          "employee": [{"@type": "Person", "name": n, "jobTitle": papel} for n, papel, _, _ in SOCIOS if "[" not in n]}]
    return ld({"@context": "https://schema.org", "@graph": g + (extra or [])})


def preload_recortes():
    return ('<link rel="preload" as="image" imagesrcset="/assets/img/fotos/luiz-recorte-560.webp 444w, /assets/img/fotos/luiz-recorte-900.webp 714w" '
            'imagesizes="(max-width:1000px) 54vw, 34vw" fetchpriority="high">')


def final_html(h2, p, c, a="", outras=""):
    return f'''<section class="sec escuro final" data-final>{letra("F&D", "letreiro")}<div class="wrap">
  <h2 class="rv">{e(h2)}</h2>{f'<p class="rv" data-d="1">{e(p)}</p>' if p else ""}
  <div class="ctas rv" data-d="2">{cta(POR_SLUG[a]["cta"] if a else "Falar com o escritório", c, a)}</div>{outras}
</div></section>'''


# ------------------------------------------------------------------ página central
def home():
    seletor = "".join(f'<a href="/{a["slug"]}"><span>{e(a["gatilho"])}</span>{SETA}</a>' for a in AREAS)
    indice = "".join(f'''<li class="rv"><a href="/{a["slug"]}"><span class="indice__n">{i + 1:02d}</span><span class="indice__nome">{e(a["nome"])}</span>
      <span class="indice__txt">{e(a["card"])}</span><span class="indice__seta">{SETA}</span></a></li>''' for i, a in enumerate(AREAS))
    difs = "".join(f'<li class="dif rv" data-d="{i % 5}">{numeral(i + 1)}<h3>{e(t)}</h3><p>{e(d)}</p></li>' for i, (t, d) in enumerate(ESC["diferenciais"]))
    socios = "".join(f'''<figure class="rv" data-d="{i + 1}"><div class="socio__foto">{foto(f, f"{n}, {papel.lower()}", "(max-width:760px) 45vw, 22vw")}</div>
      <figcaption><b>{e(n)}</b><span>{e(papel)} · {e(o)}</span></figcaption></figure>''' for i, (n, papel, o, f) in enumerate(SOCIOS))
    passos = "".join(f'<li class="passo rv" data-d="{i}"><b>{i + 1:02d}</b><h3>{e(t)}</h3><p>{e(d)}</p></li>' for i, (t, d) in enumerate(ESC["como"]))
    corpo = f'''
{capa(f'<span class="so-leitor">{NOME}: </span>{e(HERO_H1)}', '',
      cta("Falar com o escritório", "hero") + f'<a class="btn btn--linha" href="#areas"><span>Ver as áreas</span>{SETA}</a>', marca=True)}

<section class="seletor"><div class="wrap seletor__in">
  <h2 class="seletor__h">{e(ESC["seletor_h"])}</h2>
  <div class="seletor__grade">{seletor}</div>
</div></section>

<section class="sec areia" id="areas"><div class="wrap">
  <div class="indice-cab rv"><h2>{e(ESC["areas_h2"])}</h2>{cta("Falar com o escritório", "areas")}</div>
  <ol class="indice">{indice}</ol>
</div></section>

<section class="sec escuro manifesto-sec"><div class="wrap">
  <p class="manifesto" data-manifesto>{palavras(ESC["manifesto"])}</p>
  <div class="ctas">{cta("Contar o que está acontecendo", "manifesto")}</div>
  <ol class="difs">{difs}</ol>
</div></section>

<section class="sec" id="escritorio"><div class="wrap escr">
  <div class="escr__txt rv"><h2>{e(ESC["sobre_h2"])}</h2>{"".join(f"<p>{e(p)}</p>" for p in ESC["sobre"])}
    <div class="ctas">{cta("Falar com o escritório", "escritorio")}</div></div>
  <div class="socios">{socios}</div>
</div></section>

<section class="sec areia" id="como" data-passos><div class="wrap">
  <div class="passos-cab rv"><h2>{e(ESC["como_h2"])}</h2>{cta("Começar pelo WhatsApp", "como")}</div>
  <ol class="passos"><span class="passos__linha" aria-hidden="true"></span>{passos}</ol>
</div></section>

<section class="sec escuro"><div class="wrap alcance">
  <div class="alcance__txt rv"><h2>{e(ESC["alcance_h2"])}</h2><p>{e(ESC["alcance_p"])}</p>
    <div class="ctas">{cta("Falar com o escritório", "alcance")}</div></div>
  <div class="rv" data-d="1">{mapa_svg()}</div>
</div></section>

<section class="sec" id="duvidas"><div class="wrap faq">
  <div class="faq__cab rv"><h2>Dúvidas frequentes</h2>{cta("Tirar uma dúvida", "faq")}</div>
  <div class="faq__lista rv" data-d="1">{faq_html(ESC["faq"])}</div>
</div></section>

{final_html(ESC["final_h2"], ESC["final_p"], "final")}'''
    extra = schema_escritorio([{"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": p, "acceptedAnswer": {"@type": "Answer", "text": r}} for p, r in ESC["faq"]]}])
    return pagina(f"{NOME} | Advocacia criminal, família, sucessões e cível em Uberlândia",
                  "Ferreira e Dutra Advogados, em Uberlândia: direito criminal, família e sucessões, cível, trânsito e administrativo. Atendimento em todo o Brasil por processo eletrônico.",
                  corpo, "/", preload_recortes(), extra=extra, classe="home")


# ------------------------------------------------------------------ páginas de área
def area(a):
    s = a["slug"]
    cartoes = "".join(f'<li class="cartao" style="--i:{i}">{numeral(i + 1)}<h3>{e(t)}</h3><p>{e(d)}</p></li>' for i, (t, d) in enumerate(a["situacoes"]))
    passos = "".join(f'<li class="passo rv" data-d="{i}"><b>{i + 1:02d}</b><h3>{e(t)}</h3><p>{e(d)}</p></li>' for i, (t, d) in enumerate(a["atuacao"]))
    docs = (f'''<section class="sec"><div class="wrap docs">
  <div class="docs__cab rv"><h2>{e(a["documentos_h2"])}</h2><div class="ctas">{cta(a["cta"], "documentos", s)}</div></div>
  <ol class="docs__lista rv" data-d="1">{"".join(f"<li>{e(d)}</li>" for d in a["documentos"])}</ol>
</div></section>''' if a["documentos"] else "")
    socios = "".join(f'''<figure class="rv" data-d="{i + 1}"><div class="socio__foto">{foto(f, f"{n}, {papel.lower()}", "(max-width:760px) 45vw, 20vw")}</div>
      <figcaption><b>{e(n)}</b><span>{e(papel)} · {e(o)}</span></figcaption></figure>''' for i, (n, papel, o, f) in enumerate(SOCIOS))
    outras = "".join(f'<a href="/{o["slug"]}"><span>{e(o["nome"])}</span>{SETA}</a>' for o in AREAS if o["slug"] != s)
    corpo = f'''
{capa(e(a["hero_h1"]), a["hero_p"], cta(a["cta"], "hero", s) + f'<a class="btn btn--linha" href="/"><span>Conhecer o escritório</span>{SETA}</a>', area=s)}

<section class="sec areia"><div class="wrap sit">
  <div class="sit__cab rv"><h2>{e(a["situacoes_h2"])}</h2>{cta(a["cta"], "situacoes", s)}</div>
  <ol class="cartoes">{cartoes}</ol>
</div></section>

<section class="sec escuro" data-passos><div class="wrap">
  <div class="passos-cab rv"><h2>{e(a["atuacao_h2"])}</h2>{cta(a["cta"], "atuacao", s)}</div>
  <ol class="passos"><span class="passos__linha" aria-hidden="true"></span>{passos}</ol>
</div></section>

{docs}

<section class="sec areia"><div class="wrap cuida">
  <div class="cuida__txt rv"><h2>{e(ESC["sobre_h2"])}</h2>{"".join(f"<p>{e(p)}</p>" for p in ESC["sobre"])}
    <div class="ctas">{cta(a["cta"], "quem", s)}<a class="btn btn--linha" href="/#escritorio"><span>Conhecer o escritório</span>{SETA}</a></div></div>
  <div class="socios">{socios}</div>
</div></section>

<section class="sec"><div class="wrap faq">
  <div class="faq__cab rv"><h2>Dúvidas sobre {e(a["curto"].lower() if s not in ("inventario",) else "inventário")}</h2>{cta("Tirar uma dúvida", "faq", s)}</div>
  <div class="faq__lista rv" data-d="1">{faq_html(a["faq"])}</div>
</div></section>

{final_html(a["final_h2"], "", "final", s, f'<div class="outras"><h2>Outras áreas do escritório</h2><div class="outras__lista">{outras}</div></div>')}'''
    extra = schema_escritorio([
        {"@type": "Service", "name": a["nome"], "serviceType": a["nome"], "provider": {"@id": f"{DOMINIO}/#escritorio"},
         "areaServed": "BR", "url": f"{DOMINIO}/{s}", "description": a["seo_descricao"]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Início", "item": f"{DOMINIO}/"},
            {"@type": "ListItem", "position": 2, "name": a["nome"], "item": f"{DOMINIO}/{s}"}]},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": p, "acceptedAnswer": {"@type": "Answer", "text": r}} for p, r in a["faq"]]},
    ])
    return pagina(a["seo_titulo"], a["seo_descricao"], corpo, f"/{s}", preload_recortes(), extra=extra, classe=f"area area--{s}")


# ------------------------------------------------------------------ privacidade e ponte do WhatsApp
def privacidade():
    corpo = f'''<section class="sec texto-pag"><div class="wrap texto">
<h1>Política de Privacidade</h1>
<p>Como os seus dados são tratados neste site, conforme a LGPD (Lei 13.709/2018).</p>
<h2>Quem cuida dos seus dados</h2><p>Este site é da {NOME}, de {CIDADE}, responsável pelo tratamento dos dados enviados por meio dele.</p>
<h2>Que dados recebemos</h2><p>Este site não tem formulário. Ao tocar em um botão de contato, você é levado ao WhatsApp e só envia o que escrever lá.</p>
<h2>Sigilo</h2><p>O que você conta ao escritório é protegido pelo sigilo profissional da advocacia.</p>
<h2>Cookies</h2><p>Este site não usa cookies de publicidade nem de rastreamento. Se ferramentas de medição forem adicionadas, este texto será atualizado.</p>
<h2>Seus direitos</h2><p>Você pode pedir acesso, correção ou exclusão dos seus dados a qualquer momento pelo WhatsApp {e(TEL_VER)}.</p>
</div></section>'''
    return pagina(f"Política de Privacidade | {NOME}", f"Política de privacidade (LGPD) do site da {NOME}.", corpo, "/privacidade")


def obrigado():
    msgs = {a["slug"]: a["msg"] for a in AREAS}
    corpo = f'''<section class="obrigado"><div>
  {nome_svg()}
  <h1>Abrindo o WhatsApp.</h1>
  <p>Em instantes você fala com o escritório.</p>
  <div class="gira" aria-hidden="true"></div>
  <div class="ctas"><a class="btn btn--pri" id="vai" href="https://wa.me/{WHATSAPP}">{ZAP}<span>Abrir o WhatsApp</span></a><a class="btn btn--linha" href="/"><span>Voltar</span></a></div>
</div></section>
<script>
(function(){{
  var W='{WHATSAPP}', M={json.dumps(msgs, ensure_ascii=False)};
  var q=new URLSearchParams(location.search), a=(q.get('a')||'').replace(/[^a-z]/g,'');
  var msg=M[a]||'Olá! Vim pelo site da Ferreira e Dutra Advogados e quero falar sobre o meu caso.';
  var dest='https://wa.me/'+W+'?text='+encodeURIComponent(msg); document.getElementById('vai').href=dest;
  var c=(q.get('c')||'site').replace(/[^a-z0-9_-]/gi,'');
  var t0=Date.now(), partiu=false;
  function vai(){{ if(partiu) return; partiu=true; location.replace(dest); }}
  function talvez(){{ var f=900-(Date.now()-t0); setTimeout(vai, f>0?f:0); }}
  window.dataLayer=window.dataLayer||[]; window.dataLayer.push({{event:'conversao_whatsapp',contexto:c,area:a||'escritorio',eventCallback:talvez,eventTimeout:2000}});
  if(!window.google_tag_manager) talvez();
  setTimeout(vai,2600);
}})();
</script>'''
    return pagina(f"Abrindo o WhatsApp | {NOME}", f"Abrindo o WhatsApp da {NOME}.", corpo, "/obrigado", robots="noindex,nofollow", casca=False)


def main():
    paginas = {"index.html": home(), "privacidade.html": privacidade(), "obrigado.html": obrigado()}
    for a in AREAS:
        paginas[f'{a["slug"]}.html'] = area(a)
    for arq, html in paginas.items():
        (RAIZ / arq).write_text(html)
    hoje = date.today().isoformat()
    rotas = ["/"] + [f'/{a["slug"]}' for a in AREAS] + ["/privacidade"]
    (RAIZ / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
                                      + "".join(f"<url><loc>{DOMINIO}{r}</loc><lastmod>{hoje}</lastmod></url>" for r in rotas) + "</urlset>\n")
    (RAIZ / "robots.txt").write_text("User-agent: *\n" + ("Allow: /\n" if INDEXAR else "Disallow:\n") + f"\nSitemap: {DOMINIO}/sitemap.xml\n")
    (RAIZ / "llms.txt").write_text(
        f"# {NOME}\n\n> Escritório de advocacia em {CIDADE}, com atendimento em todo o Brasil por processo eletrônico.\n\n## Áreas\n"
        + "\n".join(f"- [{a['nome']}]({DOMINIO}/{a['slug']}): {a['card']}" for a in AREAS)
        + "\n\n## Perguntas frequentes\n" + "\n".join(f"- {p} {r}" for p, r in ESC["faq"])
        + f"\n\n## Contato\nWhatsApp: {TEL_VER}\nSite: {DOMINIO}/\n")
    print(f"  {len(paginas)} páginas  site.js v={hash_de(JS)}  indexar={INDEXAR}")


if __name__ == "__main__":
    main()
