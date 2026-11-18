import random, math
from px import *

W, H, S = 1200, 420, 6
random.seed(7)

def build():
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
    cx, cy, r = 560, 340, 84
    sun = []
    for row in range(-r // S, 1):
        yy = row * S
        hw = int(math.sqrt(max(r * r - yy * yy, 0)) // S) * S
        col = YELLOW if row > -7 else AMBER if row > -10 else "#f6b160"
        if row % 3 == 0 and row < -2:
            continue  # scanline gaps = retro sun
        sun.append(rect(cx - hw, cy + yy, hw * 2, S, col))
    o.append(f'<g class="sun">{"".join(sun)}</g>')

    # clouds
    cloud = ["...######.....", ".##########...", "##############.", ".############..", ]
    for i, (yy, dl) in enumerate([(70, 0), (130, -25), (100, -45)]):
        o.append(f'<g class="cloud" style="animation-delay:{dl}s">{sprite(cloud, {"#": "#ffffff22"}, 0, yy, 8)}</g>')

    # skyline: city silhouettes + mosque
    sky = INK
    bx = 0
    wins = []
    while bx < 770:
        w = random.choice([48, 60, 72, 84])
        h = random.choice([18, 24, 30]) if bx < 430 else random.choice([48, 60, 72]) if bx > 700 else random.choice([24, 30, 36])
        y = 372 - h
        o.append(rect(bx, y, w, h, sky))
        for wy in range(y + 12, 366, 18):
            for wx in range(bx + 9, bx + w - 9, 15):
                if random.random() < .32 and not (wx < 440 and wy > 296) and not (400 < bx < 720):
                    dl = random.random() * 2.4
                    wins.append(rect(wx, wy, 6, 6, AMBER, f'class="tw" style="animation-delay:-{dl:.1f}s"'))
        bx += w + random.choice([0, 6, 12])
    # tall needle tower
    pass
    # mosque: dome + two minarets
    mx = 560
    o.append(rect(mx - 120, 318, 240, 54, sky))
    for row in range(0, 11):
        hw = int(math.sqrt(max(11 * 11 - (11 - row) ** 2, 0)) * S)
        o.append(rect(mx - hw, 318 - (11 - row) * S + S * 0, hw * 2, S, sky)) if False else None
    dome = []
    R = 60
    for yy in range(0, R, S):
        hw = int(math.sqrt(R * R - (R - yy) ** 2) // S) * S
        dome.append(rect(mx - hw, 318 - R + yy, hw * 2, S, sky))
    o.append("".join(dome))
    o.append(rect(mx - 3, 244, 6, 14, sky) + rect(mx - 9, 238, 18, 6, sky))  # finial
    for dx in (-104, 94):
        o.append(rect(mx + dx, 276, 12, 96, sky) + rect(mx + dx - 6, 270, 24, 12, sky))
        o.append(rect(mx + dx + 0, 252, 12, 18, sky) + rect(mx + dx + 3, 240, 6, 12, sky))
        o.append(rect(mx + dx + 4, 300, 4, 8, AMBER, 'class="tw"'))
    o.append("".join(wins))
    # palms
    palm = [
        "..gg.....gg..",
        ".gggg...gggg.",
        "gg.ggg.ggg.gg",
        "g...gggggg..g",
        ".....gtg.....",
        ".....tt......",
        "......tt.....",
        "......tt.....",
        ".....tt......",
        ".....tt......",
        ".....tt......",
        "......tt.....",
        "......tt.....",
    ]
    o.append(sprite(palm, dict(g="#0f3d3a", t="#0b2b2a"), 1146, 240, 6))

    # ground
    o.append(rect(0, 372, W, 48, "#0e0720"))
    for x in range(0, W, 24):
        o.append(rect(x, 372, 12, 6, "#1d1038"))
    for x in range(0, W, 48):
        o.append(rect(x + 12, 396, 24, 6, "#1d1038"))

    # ---------------- title block
    o.append(ptext(64, 66, "HELLO, WORLD!", 4, CREAM))
    o.append(ptext(60, 108, "RANIM", 18, YELLOW, shadow=ORANGE))
    # class badges
    bx2 = 64
    for label, col in [("DEV", TEAL), ("DESIGN", ORANGE), ("VIDEO", ROSE)]:
        w = tw(label, 3) + 28
        o.append(frame(bx2, 262, w, 44, NIGHT, col))
        o.append(ptext(bx2 + 14, 276, label, 3, col))
        bx2 += w + 12
    o.append(ptext(64, 322, "PLAYER 1 + TRIPLE CLASS", 3, CREAM))
    o.append(f'<g class="blink">{ptext(64, 350, "> PRESS START", 3, AMBER)}</g>')

    # ---------------- desk scene
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
    o.append(rect(px0 + 6, py0 + 6, 6, 6, RED, 'class="blink"') + ptext(px0 + 16, py0 + 6, "REC", 1, CREAM))
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
    # floating coins / sparks
    for i, (x, y) in enumerate([(850, 120), (1160, 200), (760, 160)]):
        o.append(f'<g class="coin" style="animation-delay:-{i*.5}s">{sprite(["..##..", ".####.", "######", "######", ".####.", "..##.."], {"#": YELLOW}, x, y, 5)}</g>')

    o.append("</g></svg>")
    return "".join(o)

if __name__ == "__main__":
    import sys
    open(sys.argv[1] + "/hero.svg", "w").write(build())
