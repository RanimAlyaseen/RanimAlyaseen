import random, math
from px import *

W, H, S = 1200, 420, 6

T = dict(
 en=dict(hi='HELLO, WORLD!', name='RANIM', badges=[('DEV',TEAL),('DESIGN',ORANGE),('VIDEO',ROSE)], line='> EN / AR / TR'),
 tr=dict(hi='HELLO, WORLD!', sub='MERHABA DÜNYA', name='RANIM', badges=[('YAZILIM',TEAL),('TASARIM',ORANGE),('KURGU',ROSE)], line='> EN / AR / TR'),
 ar=dict(hi='HELLO, WORLD!', sub='في عالم', name='رنيم', badges=[('برمجة',TEAL),('تصميم',ORANGE),('مونتاج',ROSE)], line='> EN / AR / TR'),
)

def build(lang='en'):
    random.seed(7)
    L = T[lang]; RTL = lang == 'ar'
    o = []
    css = f"""
    .tw {{ animation: tw 2.4s steps(2) infinite; }}
    @keyframes tw {{ 50% {{ opacity: .15; }} }}
    .blink {{ animation: bl 1.1s steps(1) infinite; }}
    @keyframes bl {{ 50% {{ opacity: 0; }} }}
    .cloud {{ animation: drift 60s linear infinite; }}
    @keyframes drift {{ from {{ transform: translateX(-200px); }} to {{ transform: translateX(1300px); }} }}
    .play {{ animation: play 6s linear infinite; }}
    @keyframes play {{ from {{ transform: translateX(0); }} to {{ transform: translateX(228px); }} }}
    .type {{ transform-box: fill-box; transform-origin: left; animation: type 5s steps(8) infinite alternate; }}
    @keyframes type {{ from {{ transform: scaleX(.2); }} to {{ transform: scaleX(1); }} }}
    .steam {{ animation: steam 2s steps(4) infinite; }}
    @keyframes steam {{ from {{ transform: translateY(0); opacity: 1; }} to {{ transform: translateY(-12px); opacity: 0; }} }}
    .bob {{ animation: bob .9s steps(1) infinite; }}
    @keyframes bob {{ 50% {{ transform: translateY(-3px); }} }}
    .sun {{ animation: sunb 8s steps(1) infinite alternate; }}
    @keyframes sunb {{ 50% {{ transform: translateY(-6px); }} }}
    .coin {{ animation: coin 1.6s steps(1) infinite; }}
    @keyframes coin {{ 0%{{opacity:1}} 25%{{opacity:.4}} 50%{{opacity:1}} 75%{{opacity:.4}} }}
    """
    o.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><style>{css}</style>')
    o.append('<clipPath id="cp"><rect width="1200" height="420" rx="0"/></clipPath><g clip-path="url(#cp)">')

    # banded sunset sky
    bands = ["#1b1033", "#241446", "#321a58", "#4a2269", "#6b2a72", "#8f3470", "#b8426a", "#d9575a", "#ee7a4b", "#f4a259", "#f8c27a"]
    bh = 40
    for i, c in enumerate(bands):
        o.append(rect(0, i * bh, W, bh + 1, c))
    # dithered seams between bands (checker rows)
    for i in range(1, len(bands)):
        y = i * bh
        d = "".join(f"M{x} {y - S}h{S}v{S}h-{S}z" for x in range(0, W, S * 2))
        d2 = "".join(f"M{x} {y}h{S}v{S}h-{S}z" for x in range(S, W, S * 2))
        o.append(f'<path fill="{bands[i]}" d="{d}"/><path fill="{bands[i-1]}" d="{d2}"/>')

    # stars
    for _ in range(46):
        x, y = random.randrange(0, W, 6), random.randrange(0, 200, 6)
        sz = random.choice([3, 3, 6])
        dl = random.random() * 2.4
        o.append(rect(x, y, sz, sz, CREAM, f'class="tw" style="animation-delay:-{dl:.1f}s"'))

    # sun (pixel disc, banded) sitting on the skyline
    cx, cy, r = 600, 372, 96
    sun = []
    for row in range(-r // S, 1):
        yy = row * S
        hw = int(math.sqrt(max(r * r - yy * yy, 0)) // S) * S
        col = YELLOW if row > -7 else AMBER if row > -10 else "#f6b160"
        if row % 3 == 0 and row < -2:
            continue  # scanline gaps = retro sun
        sun.append(rect(cx - hw, cy + yy, hw * 2, S, col))
    o.append(f'<g class="sun">{"".join(sun)}</g>')

    # low stepped hills (no clutter behind text)
    hx = 0
    while hx < W:
        w = random.choice([96, 144, 192]); h = random.choice([12, 18, 24])
        o.append(rect(hx, 372 - h, w, h, INK)); hx += w
    # ground
    o.append(rect(0, 372, W, 48, "#0e0720"))
    for x in range(0, W, 24):
        o.append(rect(x, 372, 12, 6, "#1d1038"))
    for x in range(0, W, 48):
        o.append(rect(x + 12, 396, 24, 6, "#1d1038"))

    # ---------------- title block
    tx = 1136 if RTL else 64
    anc = "end" if RTL else "start"
    sub = L.get('sub')
    hy = 20 if (RTL and sub) else 30 if sub else 66
    g, _ = txt(tx, hy, L['hi'], 4, CREAM, anc); o.append(g)
    if sub:
        if RTL:
            g, _, _ = apix(sub, 15, 2, AMBER, tx, 58, "end")
        else:
            g, _ = txt(tx, 72, sub, 2, AMBER, anc)
        o.append(g)
    if RTL:
        g, w, h = apix(L['name'], 62, 3, YELLOW, tx, 104, "end", shadow=ORANGE); o.append(g)
    else:
        o.append(ptext(60, 108, L['name'], 18, YELLOW, shadow=ORANGE))
    widths = [tw(l.upper(), 3) + 28 if not AR_RE.search(l) else apix(l, 17, 2, INK, 0, 0)[1] + 28 for l, _ in L['badges']]
    bx2 = tx - sum(widths) - 12 * (len(widths) - 1) if RTL else tx
    order = list(zip(L['badges'], widths))
    for (label, col), w in order:
        o.append(frame(bx2, 262, w, 44, NIGHT, col))
        if AR_RE.search(label):
            g, aw, ah = apix(label, 17, 2, col, bx2 + w // 2, 262 + (44 - 0) // 2, "middle"); 
            g, aw, ah = apix(label, 17, 2, col, bx2 + w // 2, 262 + (44 - ah) // 2, "middle")
        else:
            g, _ = txt(bx2 + 14, 276, label, 3, col)
        o.append(g)
        bx2 += w + 12
    g, _ = txt(tx, 322, L['line'], 3, CREAM, anc, shadow=INK); o.append(g)

    # ---------------- desk scene
    scene_start = len(o)
    deskx, deskt = 790, 316
    # desk
    o.append(rect(deskx, deskt, 380, 12, "#8a4b2d") + rect(deskx, deskt + 12, 380, 6, "#5e311c"))
    o.append(rect(deskx + 14, deskt + 18, 12, 38, "#5e311c") + rect(deskx + 354, deskt + 18, 12, 38, "#5e311c"))
    # monitor
    o.append(rect(960, 296, 24, 20, "#2b2d4e") + rect(930, 310, 84, 8, "#2b2d4e"))
    o.append(rect(876, 148, 262, 150, "#2b2d4e") + rect(880, 152, 254, 142, INK))
    sx, sy = 888, 160
    o.append(rect(sx, sy, 234, 128, "#0d1224"))
    # code panel
    cols = [TEAL, AMBER, ROSE, BLUE, GREEN, CREAM]
    widths = [90, 60, 76, 44, 84, 52, 66, 38]
    for i, wd in enumerate(widths):
        o.append(rect(sx + 8 + (i % 3) * 8, sy + 10 + i * 12, wd, 6, cols[i % len(cols)],
                      f'class="type" style="animation-delay:-{i*0.6:.1f}s"'))
    o.append(rect(sx + 8 + 50, sy + 10 + 8 * 12, 6, 8, CREAM, 'class="blink"'))
    # video preview
    px0, py0 = sx + 112, sy + 8
    o.append(rect(px0, py0, 114, 76, "#321a58"))
    o.append(rect(px0, py0 + 40, 114, 36, "#b8426a") + rect(px0, py0 + 58, 114, 18, "#ee7a4b"))
    o.append(rect(px0 + 78, py0 + 36, 20, 20, YELLOW))
    o.append(sprite(["....##....", "...####...", "..######..", ".########.", "##########"], {"#": INK}, px0 + 16, py0 + 40, 6))
    o.append(rect(px0 + 6, py0 + 6, 6, 6, RED, 'class="blink"'))
    rec_x = px0 + 16
    # timeline
    ty = sy + 92
    o.append(rect(sx, ty - 4, 234, 40, "#121833"))
    tracks = [
        [(6, 60, TEAL), (70, 46, ORANGE), (120, 70, TEAL), (194, 34, ROSE)],
        [(14, 84, ROSE), (102, 56, YELLOW), (162, 62, BLUE)],
    ]
    for i, tr in enumerate(tracks):
        for (a, wd, c) in tr:
            o.append(rect(sx + a, ty + i * 16, wd, 12, c))
    o.append(f'<g class="play"><rect x="{sx + 4}" y="{ty - 6}" width="3" height="44" fill="{RED}"/><rect x="{sx + 1}" y="{ty - 8}" width="9" height="5" fill="{RED}"/></g>')
    # keyboard
    o.append(rect(deskx + 10, deskt - 6, 84, 6, "#cfd3e8") + rect(deskx + 10, deskt - 2, 84, 2, "#8c90b0"))
    # mug + steam
    o.append(rect(1100, deskt - 24, 24, 24, CREAM) + rect(1124, deskt - 18, 8, 12, CREAM) + rect(1127, deskt - 15, 3, 6, "#0e0720"))
    o.append(rect(1100, deskt - 24, 24, 6, "#6b4226"))
    for i, dx in enumerate((1104, 1112, 1118)):
        o.append(rect(dx, deskt - 36, 4, 8, "#ffffff88", f'class="steam" style="animation-delay:-{i*0.5}s"'))
    # character (bob = tiny head nod)
    o.append(f'<g class="bob">{sprite(PLAYER, PLAYER_LEG, 690, 222, 6)}</g>')
    scene = o[scene_start:]; del o[scene_start:]
    if RTL:
        o.append('<g transform="translate(1200,0) scale(-1,1)">' + "".join(scene) + '</g>')
        o.append(ptext(1200 - rec_x - 17, py0 + 6, "REC", 1, CREAM))
    else:
        o.append("".join(scene)); o.append(ptext(rec_x, py0 + 6, "REC", 1, CREAM))
    o.append("</g></svg>")
    return "".join(o)

if __name__ == "__main__":
    import sys
    for l in ("en","tr","ar"):
        import os; os.makedirs(f"{sys.argv[1]}/{l}", exist_ok=True)
        open(f"{sys.argv[1]}/{l}/hero.svg", "w").write(build(l))
