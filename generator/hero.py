import random, math
from px import *
from robot_lib import robot_group, robot_css

W, H, S = 1200, 530, 6

T = dict(
 en=dict(hi='HELLO, WORLD!', name='RANIM', badges=[('DEV',TEAL),('AI / NLP',ORANGE),('DESIGN',ROSE)], focus=('GROWING FOCUS:', 'LLM AGENTS')),
 tr=dict(hi='HELLO, WORLD!', sub='MERHABA DÜNYA', name='RANİM', badges=[('YAZILIM',TEAL),('YZ / NLP',ORANGE),('TASARIM',ROSE)], focus=('GELİŞEN ODAK:', 'LLM AJANLARI')),
 ar=dict(hi='HELLO, WORLD!', sub='مرحباً، أنا', name='رنيم', badges=[('برمجة',TEAL),('ذكاء اصطناعي',ORANGE),('تصميم',ROSE)], focus=('تركيز متزايد:', 'وكلاء أذكياء')),
)

import os
VAR = os.environ.get('VAR','O')
SHOW_FOCUS = False   # the 'growing focus' pill is built but switched off

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
    o.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><style>{css}{robot_css(960)}</style>')
    o.append('<clipPath id="cp"><rect width="1200" height="530" rx="0"/></clipPath><g clip-path="url(#cp)">')

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
    # street: far curb, sidewalk with two lamps, near curb, road with a lane line
    o.append(rect(0, 372, W, H - 372, "#0e0720"))
    for x in range(0, W, 24):
        o.append(rect(x, 372, 12, 6, "#1d1038"))
    o.append(rect(0, 378, W, 32, "#1b0f35"))
    for x in range(0, W, 60):
        o.append(rect(x, 378, 4, 32, "#150a2a"))
    o.append(rect(0, 410, W, 8, "#3a2266") + rect(0, 418, W, 4, "#120a22"))
    o.append(rect(0, 422, W, H - 422, "#0b0517"))
    for x in range(20, W, 120):
        o.append(rect(x, 468, 64, 6, "#f2c94c"))
    for x in range(0, W, 48):
        o.append(rect(x + 12, 506, 24, 6, "#1d1038"))
    o.append(rect(0, H - 10, W, 10, "#1d1038"))
    for k, x in enumerate((230, 1010)):                                   # sidewalk lamps
        o.append(rect(x - 8, 380, 24, 14, "#ffd23f22") + rect(x, 392, 8, 18, "#2a1650") + rect(x - 2, 384, 12, 8, "#ffd23f", f'class="blink" style="animation-delay:-{k*.5:.1f}s"'))

    # ---------------- title block
    tx = 1136 if RTL else 64
    anc = "end" if RTL else "start"
    sub = L.get('sub')
    if RTL and VAR == 'O':
        g, _, _ = apix('مرحباً يا عالم! هنا', 22, 2, CREAM, tx, 34, "end"); o.append(g)
        g, w, hh = apix(L['name'], 62, 3, YELLOW, tx, 104, "end", shadow=ORANGE); o.append(g)
    elif RTL and VAR == 'A':
        g, _ = txt(tx, 34, L['hi'], 4, CREAM, anc); o.append(g)
        g, w, hh = apix(L['name'], 62, 3, YELLOW, tx, 104, "end", shadow=ORANGE); o.append(g)
    elif RTL and VAR == 'B':
        g, _ = txt(tx, 16, L['hi'], 3, CREAM, anc); o.append(g)
        g, _, _ = apix(sub, 15, 3, AMBER, tx, 58, "end"); o.append(g)
        g, w, hh = apix(L['name'], 48, 3, YELLOW, tx, 130, "end", shadow=ORANGE); o.append(g)
    elif RTL:
        g, _ = txt(tx, 26, L['hi'], 4, CREAM, anc); o.append(g)
        _, sw, sh = apix(sub, 26, 2, AMBER, 0, 0)
        g, _, _ = apix(sub, 26, 2, AMBER, tx, 190 - sh, "end"); o.append(g)
        g, w, hh = apix(L['name'], 50, 3, YELLOW, tx - sw - 28, 112, "end", shadow=ORANGE); o.append(g)
    else:
        hy = 30 if sub else 66
        g, _ = txt(tx, hy, L['hi'], 4, CREAM, anc); o.append(g)
        if sub:
            g, _ = txt(tx, 72, sub, 2, AMBER, anc); o.append(g)
        o.append(ptext(60, 108, L['name'], 18, YELLOW, shadow=ORANGE))
    widths = [tw(l.upper(), 3) + 28 if not AR_RE.search(l) else apix(l, 17, 2, INK, 0, 0)[1] + 28 for l, _ in L['badges']]
    bx2 = tx - sum(widths) - 12 * (len(widths) - 1) if RTL else tx
    order = list(zip(L['badges'], widths))
    if RTL: order = order[::-1]   # read right to left: first badge on the right
    for (label, col), w in order:
        o.append(frame(bx2, 262, w, 44, NIGHT, col))
        if AR_RE.search(label):
            g, aw, ah = apix(label, 17, 2, col, bx2 + w // 2, 262 + (44 - 0) // 2, "middle"); 
            g, aw, ah = apix(label, 17, 2, col, bx2 + w // 2, 262 + (44 - ah) // 2, "middle")
        else:
            g, _ = txt(bx2 + 14, 276, label, 3, col)
        o.append(g)
        bx2 += w + 12
    # ---------------- growing-focus pill (drawn last so it sits on top of the sun / desk)
    lab, key = L['focus']
    FY, FH = 320, 40
    if RTL:
        _g, lw, lh = apix(lab, 17, 2, CREAM, 0, 0)
        _g, kw, kh = apix(key, 17, 2, YELLOW, 0, 0)
    else:
        lw = tw(lab.upper(), 3); kw = tw(key.upper(), 3); lh = kh = 21
    CP = 10                                           # padding inside the key-words chip
    FW = 16 + 36 + 14 + lw + 14 + (kw + 2 * CP) + 6
    fx = tx - FW if RTL else tx
    focus_o = [frame(fx, FY, FW, FH, NIGHT, GREEN)]
    ix0 = fx + FW - 16 - 32 if RTL else fx + 16       # rising bars icon
    for i, hgt in enumerate([8, 14, 22]):
        focus_o.append(rect(ix0 + i * 12, FY + FH - 9 - hgt, 8, hgt, GREEN))
        focus_o.append(rect(ix0 + i * 12, FY + FH - 9 - hgt, 8, 3, "#d4f7dc"))
    CH, CY = 30, FY + 5                                # solid yellow chip, dark text = easy to read
    if RTL:
        x1 = ix0 - 14
        g, _w, _h = apix(lab, 17, 2, CREAM, x1, FY + (FH - lh) // 2, "end"); focus_o.append(g)
        cx1 = x1 - lw - 14                             # chip's right edge
        focus_o.append(rect(cx1 - kw - 2 * CP, CY, kw + 2 * CP, CH, YELLOW))
        g, _w, _h = apix(key, 17, 2, INK, cx1 - CP, FY + (FH - kh) // 2, "end"); focus_o.append(g)
    else:
        x1 = ix0 + 36 + 14
        g, _ = txt(x1, FY + 10, lab, 3, CREAM); focus_o.append(g)
        cx0 = x1 + lw + 14
        focus_o.append(rect(cx0, CY, kw + 2 * CP, CH, YELLOW))
        g, _ = txt(cx0 + CP, FY + 10, key, 3, INK); focus_o.append(g)

    # ---------------- desk scene
    scene_start = len(o)
    deskx, deskt = 670, 316
    # character, drawn BEFORE the desk so the desk hides her lower body (she sits behind it)
    o.append(f'<g class="bob">{sprite(CHIBI[:25], CHIBI_LEG, 700, 190, 5)}</g>')
    STAR = ["..#..", "..#..", "#####", "..#..", "..#.."]
    for k, (sx, sy, sc_, col) in enumerate(((664, 214, 3, "#ff5fa8"), (822, 204, 3, "#b05cff"), (682, 292, 3, "#ffffff"), (824, 296, 3, "#ff9ad0"))):
        o.append(sprite(STAR, {"#": col}, sx, sy, sc_, f'class="pulse" style="animation-delay:-{k*0.4}s"'))
    # desk
    o.append(rect(deskx, deskt, 500, 12, "#8a4b2d") + rect(deskx, deskt + 12, 500, 6, "#5e311c"))
    o.append(rect(deskx + 14, deskt + 18, 12, 38, "#5e311c") + rect(deskx + 474, deskt + 18, 12, 38, "#5e311c"))
    o.append(rect(deskx + 26, deskt + 18, 448, 34, "#6e3b22") + rect(deskx + 26, deskt + 18, 448, 4, "#4a2615") + rect(deskx + 120, deskt + 28, 60, 8, "#4a2615") + rect(deskx + 320, deskt + 28, 60, 8, "#4a2615"))   # front panel with two drawers
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
    # neural network panel
    px0, py0 = sx + 116, sy + 6
    o.append(rect(px0 - 2, py0 - 2, 116, 80, "#101530"))
    layers = [(px0 + 12, [16, 38, 60], TEAL), (px0 + 42, [8, 28, 48, 68], AMBER), (px0 + 72, [8, 28, 48, 68], ROSE), (px0 + 100, [26, 50], GREEN)]
    lines = []
    for li in range(len(layers) - 1):
        x1, ys1, _ = layers[li]; x2, ys2, _ = layers[li + 1]
        for y1 in ys1:
            for y2 in ys2:
                lines.append(f'<line x1="{x1}" y1="{py0 + y1}" x2="{x2}" y2="{py0 + y2}"/>')
    o.append('<g stroke="#3a4088" stroke-width="2" shape-rendering="crispEdges">' + "".join(lines) + '</g>')
    k = 0
    for x, ys, c in layers:
        for y in ys:
            o.append(rect(x - 5, py0 + y - 5, 10, 10, INK) + rect(x - 4, py0 + y - 4, 8, 8, c, f'class="tw" style="animation-delay:-{(k * 0.37) % 2.4:.2f}s"'))
            k += 1
    # training loss curve
    ty = sy + 90
    o.append(rect(sx, ty, 234, 38, "#121833"))
    o.append(rect(sx + 6, ty + 4, 2, 30, "#3a4088") + rect(sx + 6, ty + 32, 222, 2, "#3a4088"))
    import math as _m
    cur = []; prev = None
    for i in range(36):
        h = int(24 * _m.exp(-i / 9.0)) + 3 + (i % 3) // 2
        top = ty + 32 - h - 2
        seg_h = 4 if prev is None else max(4, abs(prev - top) + 4)
        cur.append(rect(sx + 10 + i * 6, min(top, prev if prev is not None else top), 6, seg_h, GREEN))
        prev = top
    val = []; prev = None
    for i in range(36):
        h = int(22 * _m.exp(-i / 11.0)) + 5 + (i % 4) // 2
        top = ty + 32 - h - 2
        seg_h = 3 if prev is None else max(3, abs(prev - top) + 3)
        val.append(rect(sx + 10 + i * 6, min(top, prev if prev is not None else top), 6, seg_h, AMBER))
        prev = top
    o.append('<g class="type">' + "".join(val) + "".join(cur) + rect(sx + 10 + 35 * 6 + 2, prev - 2, 6, 6, CREAM, 'class="blink"') + '</g>')
    # keyboard
    o.append(rect(deskx + 60, deskt - 6, 84, 6, "#cfd3e8") + rect(deskx + 60, deskt - 2, 84, 2, "#8c90b0"))
    o.append(rect(deskx + 72, deskt - 12, 14, 8, "#f7e1d3") + rect(deskx + 118, deskt - 12, 14, 8, "#f7e1d3"))   # hands on the keyboard
    # mug + steam
    o.append(rect(1100, deskt - 24, 24, 24, CREAM) + rect(1124, deskt - 18, 8, 12, CREAM) + rect(1127, deskt - 15, 3, 6, "#0e0720"))
    o.append(rect(1100, deskt - 24, 24, 6, "#6b4226"))
    for i, dx in enumerate((1104, 1112, 1118)):
        o.append(rect(dx, deskt - 36, 4, 8, "#ffffff88", f'class="steam" style="animation-delay:-{i*0.5}s"'))
    scene = o[scene_start:]; del o[scene_start:]
    if RTL:
        o.append('<g transform="translate(1200,0) scale(-1,1)">' + "".join(scene) + '</g>')
    else:
        o.append("".join(scene))
    if SHOW_FOCUS: o.append("".join(focus_o))
    o.append(robot_group(lang, 70, 416))
    o.append("</g></svg>")
    return "".join(o)

if __name__ == "__main__":
    import sys
    for l in ("en","tr","ar"):
        import os; os.makedirs(f"{sys.argv[1]}/{l}", exist_ok=True)
        open(f"{sys.argv[1]}/{l}/hero.svg", "w").write(build(l))
