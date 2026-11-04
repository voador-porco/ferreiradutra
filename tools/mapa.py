"""Mapa do Brasil em traço, com Uberlândia em destaque e arcos até as capitais.

Contorno: Natural Earth (domínio público), via world.geo.json, em assets/src/mapa/brasil.geo.json.
Projeção equirretangular com correção de cos(15°), boa o bastante para um desenho.
"""
import json, math
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
K = math.cos(math.radians(15))
UBERLANDIA = (-48.277, -18.918)
CAPITAIS = [(-46.63, -23.55), (-43.17, -22.91), (-47.88, -15.79), (-43.94, -19.92), (-38.50, -12.97),
            (-34.88, -8.05), (-60.02, -3.12), (-51.23, -30.03), (-48.50, -1.46), (-56.10, -15.60)]


def _xy(lon, lat, caixa):
    x0, y0, esc = caixa
    return ((lon * K - x0) * esc, (-lat - y0) * esc)


def svg(largura=600):
    g = json.loads((RAIZ / "assets/src/mapa/brasil.geo.json").read_text())
    anel = g["features"][0]["geometry"]["coordinates"][0]
    xs = [lon * K for lon, _ in anel]; ys = [-lat for _, lat in anel]
    x0, y0 = min(xs), min(ys)
    esc = largura / (max(xs) - x0)
    altura = (max(ys) - y0) * esc
    caixa = (x0, y0, esc)
    pts = [_xy(lon, lat, caixa) for lon, lat in anel]
    contorno = "M" + "L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + "Z"
    ux, uy = _xy(*UBERLANDIA, caixa)
    arcos = []
    for i, (lon, lat) in enumerate(CAPITAIS):
        cx, cy = _xy(lon, lat, caixa)
        mx, my = (ux + cx) / 2, (uy + cy) / 2
        dx, dy = cx - ux, cy - uy
        dist = math.hypot(dx, dy) or 1
        curva = dist * .22                                    # o arco sobe para o lado de fora
        qx, qy = mx - dy / dist * curva, my + dx / dist * curva
        arcos.append(f'<path class="mapa__arco" pathLength="1" style="--d:{.6 + i * .18:.2f}s" d="M{ux:.1f} {uy:.1f}Q{qx:.1f} {qy:.1f} {cx:.1f} {cy:.1f}"/>'
                     f'<circle class="mapa__cap" style="--d:{1.4 + i * .18:.2f}s" cx="{cx:.1f}" cy="{cy:.1f}" r="2.6"/>')
    return (f'<svg class="mapa" viewBox="-12 -12 {largura + 24} {altura + 24:.0f}" role="img" '
            f'aria-label="Mapa do Brasil com Uberlândia em destaque e linhas até as capitais">'
            f'<path class="mapa__pais" pathLength="1" d="{contorno}"/>{"".join(arcos)}'
            f'<circle class="mapa__onda" cx="{ux:.1f}" cy="{uy:.1f}" r="7"/><circle class="mapa__onda mapa__onda--2" cx="{ux:.1f}" cy="{uy:.1f}" r="7"/>'
            f'<circle class="mapa__udi" cx="{ux:.1f}" cy="{uy:.1f}" r="5.5"/>'
            f'<text class="mapa__nome" x="{ux + 13:.1f}" y="{uy + 4:.1f}">Uberlândia</text></svg>')


if __name__ == "__main__":
    print(len(svg()))
