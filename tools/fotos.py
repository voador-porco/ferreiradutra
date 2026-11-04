#!/usr/bin/env python3
"""Retratos dos sócios, recortes do topo e ícone da aba (a imagem de compartilhamento sai do tools/og.py).

    python3 tools/fotos.py

Originais em assets/src/fotos/ (vieram pelo WhatsApp do cliente, 1000x1500 e 960x1280).
"""
import asyncio, os, sys
from pathlib import Path
from PIL import Image, ImageFilter

RAIZ = Path(__file__).resolve().parent.parent
SRC, OUT, IMG = RAIZ / "assets/src/fotos", RAIZ / "assets/img/fotos", RAIZ / "assets/img"
CH = os.path.expanduser("~/Library/Caches/ms-playwright/chromium_headless_shell-1234/chrome-headless-shell-mac-arm64/chrome-headless-shell")
sys.path.insert(0, str(RAIZ / "tools"))

# (arquivo, nome, topo do recorte 4:5 em fração da altura que sobra)
# A foto da Ludmilla veio cortada na testa e nos braços: o Firefly completou (ludmilla-expandida.jpg).
RETRATOS = [("luiz.jpg", "luiz", .32), ("ludmilla-expandida.jpg", "ludmilla", .05)]
# Recortes sem fundo para o topo (Vision da Apple: swift ~/dev/cazetv-conceito/tools/lift.swift entrada saida.png)
# (arquivo, nome, altura do busto em fração do recorte, contração da borda em px, como "contrair seleção" do Photoshop)
# O Luiz vem cortado no tórax para ficar na mesma proporção da Ludmilla (os dois em busto).
RECORTES = [("luiz-recorte.png", "luiz-recorte", .62, 9), ("ludmilla-recorte.png", "ludmilla-recorte", 1, 5)]


def salvar(im, nome, larguras, q=80):
    for w in larguras:
        alvo, w = w, min(w, im.width)
        im.resize((w, round(im.height * w / im.width)), Image.LANCZOS).save(OUT / f"{nome}-{alvo}.webp", "WEBP", quality=q, method=6)


def retratos():
    OUT.mkdir(parents=True, exist_ok=True)
    for arq, nome, ancora in RETRATOS:
        im = Image.open(SRC / arq).convert("RGB")
        W, H = im.size
        if W * 1.25 <= H:
            w, h = W, round(W * 1.25)
        else:
            w, h = round(H * .8), H
        x0, y0 = (W - w) // 2, round((H - h) * ancora)
        salvar(im.crop((x0, y0, x0 + w, y0 + h)), nome, (480, 720, 960))
    for arq, nome, busto, contrai in RECORTES:
        im = Image.open(SRC / arq).convert("RGBA")
        # contrai a borda (some a franja branca do fundo antigo) e suaviza 1 px
        a = im.getchannel("A").filter(ImageFilter.MinFilter(contrai)).filter(ImageFilter.GaussianBlur(1.1))
        im.putalpha(a)
        # borda semitransparente puxada para o escuro: o que restou do fundo claro não vira halo sobre o grafite
        import numpy as np
        px = np.asarray(im).astype(np.float32)
        k = .7 + .3 * (px[..., 3:4] / 255)
        px[..., :3] *= k
        im = Image.fromarray(px.clip(0, 255).astype(np.uint8))
        im = im.crop(im.getbbox())
        im = im.crop((0, 0, im.width, round(im.height * busto)))
        for alvo in (560, 900):                    # o nome segue o pedido; o tamanho real não passa do original
            alt = min(alvo, im.height)
            w = round(im.width * alt / im.height)
            im.resize((w, alt), Image.LANCZOS).save(OUT / f"{nome}-{alvo}.webp", "WEBP", quality=82, method=6)


async def icones():
    from letreiro import svg as letra
    fd = letra("F&D", peso=600)
    ic = fd.replace('<svg class=""', '<svg xmlns="http://www.w3.org/2000/svg"').replace('<path pathLength="1" ', '<path fill="#9C7448" ')
    (IMG / "favicon-v1.svg").write_text(ic)
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=CH)
        pg = await b.new_page()
        for lado, arq in ((64, "favicon-v1.png"), (180, "apple-touch-icon.png")):
            await pg.set_viewport_size({"width": lado, "height": lado})
            pad = 0 if lado == 64 else round(lado * .16)
            fundo = "transparent" if lado == 64 else "#F3EEE6"   # o iOS pinta transparência de preto
            icone = ic.replace("<svg ", '<svg style="width:%dpx" ' % (lado - 2 * pad), 1)
            await pg.set_content(f'<html><body style="margin:0;background:{fundo};display:grid;place-items:center;width:{lado}px;height:{lado}px">'
                                 f'{icone}</body></html>')
            await pg.screenshot(path=str(IMG / arq), omit_background=(lado == 64))
        await b.close()


if __name__ == "__main__":
    retratos()
    asyncio.run(icones())
    print("ok:", sorted(p.name for p in OUT.glob("*.webp")))
