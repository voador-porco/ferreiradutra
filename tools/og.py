#!/usr/bin/env python3
"""Imagem de compartilhamento (assets/img/og-v1.jpg) tirada do próprio topo do site.

    python3 tools/serve.py 4235   (em outro terminal)
    python3 tools/og.py
"""
import asyncio, os
from pathlib import Path
from playwright.async_api import async_playwright

RAIZ = Path(__file__).resolve().parent.parent
CH = os.path.expanduser("~/Library/Caches/ms-playwright/chromium_headless_shell-1234/chrome-headless-shell-mac-arm64/chrome-headless-shell")
CH = CH if os.path.exists(CH) else None   # sem esse caminho, usa o Chromium padrão do Playwright


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=CH)
        pg = await b.new_page(viewport={"width": 1200, "height": 630})
        await pg.goto("http://localhost:4235/", wait_until="networkidle")
        await pg.add_style_tag(content=".top,.zap{display:none!important}.capa{min-height:630px!important}.capa__txt{padding-block:4.6rem 11rem!important}.capa__marca{margin-bottom:2.6rem!important}.capa .ctas{display:none!important}")
        await pg.wait_for_timeout(4200)                     # as letras F e D terminam de se desenhar
        await pg.screenshot(path=str(RAIZ / "assets/img/og-v1.jpg"), type="jpeg", quality=86, clip={"x": 0, "y": 0, "width": 1200, "height": 630})
        await b.close()
    print("ok: og-v1.jpg")

if __name__ == "__main__":
    asyncio.run(main())
