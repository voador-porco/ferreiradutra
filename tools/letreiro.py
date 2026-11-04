"""Texto -> contorno SVG (path), a partir de uma fonte instalada.

Serve para o nome do escritório no cabeçalho (sem carregar fonte serifada) e para as
palavras grandes desenhadas a traço no topo das páginas (F&D e o nome de cada área).
"""
import re
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.varLib.instancer import instantiateVariableFont

FONTES = Path.home() / "Library/Fonts"
_cache = {}


def fonte(arquivo="CormorantGaramond-VariableFont_wght.ttf", peso=500):
    chave = (arquivo, peso)
    if chave not in _cache:
        f = TTFont(FONTES / arquivo)
        if "fvar" in f:
            f = instantiateVariableFont(f, {"wght": peso})
        _cache[chave] = f
    return _cache[chave]


def contorno(texto, arquivo="CormorantGaramond-VariableFont_wght.ttf", peso=500, espaco=0):
    """Devolve (d, largura, ascendente, descendente) em unidades da fonte, linha de base em y=0 (y para baixo)."""
    f = fonte(arquivo, peso)
    gs, cmap, hmtx = f.getGlyphSet(), f.getBestCmap(), f["hmtx"]
    upm = f["head"].unitsPerEm
    x, partes = 0, []
    for ch in texto:
        nome = cmap.get(ord(ch))
        if nome is None:
            continue
        pen = SVGPathPen(gs)
        gs[nome].draw(TransformPen(pen, (1, 0, 0, -1, x, 0)))
        partes.append(re.sub(r"-?\d+\.\d+", lambda m: str(round(float(m.group()))), pen.getCommands()))
        x += hmtx[nome][0] + espaco * upm
    os2 = f["OS/2"]
    return " ".join(p for p in partes if p), x, os2.sTypoAscender, -os2.sTypoDescender


def svg(texto, classe="", **kw):
    d, w, asc, desc = contorno(texto, **kw)
    return (f'<svg class="{classe}" viewBox="0 {-asc} {w:.0f} {asc + desc}" aria-hidden="true">'
            f'<path pathLength="1" d="{d}"/></svg>')


if __name__ == "__main__":
    import sys
    print(svg(" ".join(sys.argv[1:]) or "F&D")[:300])
