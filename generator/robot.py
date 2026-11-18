# Animated pixel-art strip: an original TV-head robot patrols a night street and greets you at each end.
import sys, os, random
from px import *
OUT = sys.argv[1]
W, H, S = 1200, 200, 5
GROUND = 164
LEG = dict(o="#12081f", w="#e6e1ff", g="#a99be0", s="#1b1033", t="#3ee6d0", p="#ff6fb3", r="#ff3d94", y="#ffd23f")
UPPER = [
 ".......r........",
 ".......o........",
 "..oooooooooooo..",
 "..owwwwwwwwwwo..",
 "..owssssssssswo.".replace("wo.", "wo")[:16].ljust(16, "."),
 "..owsttsstts.wo.",
 "..owsttsstts.wo.",
 "..owpsstttspwo..",
 "..owssssssssswo.",
 "..owwwwwwwwwwo..",
 "..oooooooooooo..",
 "......oggo......",
 "....oooooooo....",
 "...owwwwwwwwo...",
 "...owwgggwrwwo..",
 "...owwwwwwwwo...",
 "...owgggggggwo..",
 "....oooooooo....",
]
# clean, exact head rows (screen = 8 wide between the rims)
UPPER[4] = "..owssssssssswo."[:16]
UPPER[4] = "..ow" + "ssssssss" + "wo" + ".."
UPPER[5] = "..ow" + "sttsstts" + "wo" + ".."
UPPER[6] = "..ow" + "sttsstts" + "wo" + ".."
UPPER[7] = "..ow" + "pssttssp" + "wo" + ".."
UPPER[8] = "..ow" + "ssssssss" + "wo" + ".."
UPPER[14] = "...o" + "wgggwrww" + "o" + "..."
UPPER[16] = "...o" + "wgggggww" + "o" + "..."
ARM = ["ooo", "ogo", "ogo", "ooo"]
ARM_UP = ["oo", "go", "go", "oo"]
LEGS_A = ["....ogo..ogo....", "....ooo..ooo...."]
LEGS_B = ["....ogo..ogo....".replace("....o", ".....o")[:16], "....ooo..ooo...."]
LEGS_B = ["....ogoogo.....".ljust(16, "."), "....oooooo....."[:16].ljust(16, ".")]

T = {"en": "HELLO!", "tr": "MERHABA!", "ar": "مرحباً!"}
CSS = (
 ".mv{animation:patrol 22s steps(220) infinite}@keyframes patrol{0%{transform:translateX(0)}50%{transform:translateX(960px)}100%{transform:translateX(0)}}"
 ".fl{transform-box:fill-box;transform-origin:center;animation:flip 22s steps(1) infinite}@keyframes flip{0%{transform:scaleX(1)}50%{transform:scaleX(-1)}100%{transform:scaleX(-1)}}"
 ".la{animation:la .44s steps(1) infinite}.lb{animation:lb .44s steps(1) infinite}"
 "@keyframes la{0%{opacity:1}50%{opacity:0}}@keyframes lb{0%{opacity:0}50%{opacity:1}}"
 ".bod{animation:bod .44s steps(1) infinite}@keyframes bod{0%{transform:translateY(0)}50%{transform:translateY(-5px)}}"
 ".au{animation:au 1.76s steps(1) infinite}.ad{animation:ad 1.76s steps(1) infinite}"
 "@keyframes au{0%,50%{opacity:0}51%,100%{opacity:1}}@keyframes ad{0%,50%{opacity:1}51%,100%{opacity:0}}"
 ".eb{animation:eb 4s steps(1) infinite}@keyframes eb{0%,93%{opacity:0}94%,97%{opacity:1}98%,100%{opacity:0}}"
 ".bub{animation:bub 22s steps(1) infinite}@keyframes bub{0%{opacity:1}7%{opacity:0}43%{opacity:1}57%{opacity:0}93%{opacity:1}100%{opacity:1}}"
 ".tw{animation:tw 2.4s steps(1) infinite}@keyframes tw{0%{opacity:1}50%{opacity:.25}}"
 ".hop{animation:hop 1.2s steps(1) infinite}@keyframes hop{50%{transform:translateY(-6px)}}"
)

def build(lang):
    o = [frame(0, 0, W, H, NIGHT, PLUM)]
    rnd = random.Random(11)
    # sky: twinkling stars + a pixel moon
    for i in range(26):
        x, y = rnd.randrange(24, W - 24, 4), rnd.randrange(16, 120, 4)
        o.append(rect(x, y, 4, 4, rnd.choice(["#ffffff", "#c9b8ff", "#ff9ad0"]), f'class="tw" style="animation-delay:-{rnd.random()*2.4:.1f}s"'))
    MOON = ["..####..", ".###....", "###.....", "###.....", "###.....", ".###....", "..####.."]
    o.append(sprite(MOON, {"#": "#f6e8c8", ".": NIGHT}, 1096, 30, 5))
    # skyline silhouettes
    for (x, w, h) in ((60, 64, 52), (150, 48, 80), (230, 72, 60), (860, 56, 70), (940, 80, 48), (1030, 52, 84)):
        o.append(rect(x, GROUND - h, w, h, "#1d1238"))
        for wy in range(GROUND - h + 8, GROUND - 8, 16):
            for wx in range(x + 8, x + w - 8, 14):
                if rnd.random() < .45:
                    o.append(rect(wx, wy, 6, 6, rnd.choice(["#ffd23f", "#3ee6d0", "#ff6fb3"]), f'class="tw" style="animation-delay:-{rnd.random()*2.4:.1f}s"'))
    # street
    o.append(rect(8, GROUND, W - 16, 6, PURPLE) + rect(8, GROUND + 6, W - 16, H - GROUND - 14, "#120a22"))
    for x in range(8, W - 24, 40):
        o.append(rect(x, GROUND, 20, 6, "#7b3fd0"))
        o.append(rect(x + 14, GROUND + 18, 24, 4, "#2a1650"))
    # glowing data chips on the street
    for k, (x, col) in enumerate(((330, TEAL), (610, ROSE), (900, YELLOW))):
        o.append(f'<g class="hop" style="animation-delay:-{k*.4:.1f}s">' + rect(x, GROUND - 22, 14, 14, col) + rect(x + 3, GROUND - 19, 8, 8, INK) + rect(x + 5, GROUND - 17, 4, 4, col) + '</g>')
    # the robot
    X0 = 70; Y0 = GROUND - 20 * S
    rb = []
    rb.append(f'<g class="la">{sprite(LEGS_A, LEG, 0, 18 * S, S)}</g><g class="lb">{sprite(LEGS_B, LEG, 0, 18 * S, S)}</g>')
    up = [sprite(UPPER, LEG, 0, 0, S), sprite(ARM, LEG, 0, 13 * S, S),
          f'<g class="ad">{sprite(ARM, LEG, 13 * S, 13 * S, S)}</g><g class="au">{sprite(ARM_UP, LEG, 14 * S, 8 * S, S)}</g>',
          f'<g class="eb">{rect(4 * S, 5 * S, 8 * S, 2 * S, LEG["s"])}{rect(5 * S, 6 * S, 2 * S, S, LEG["t"])}{rect(9 * S, 6 * S, 2 * S, S, LEG["t"])}</g>',
          rect(7 * S, 0, S, S, LEG["r"], 'class="blink"')]
    rb.append(f'<g class="bod">{"".join(up)}</g>')
    o.append(f'<g transform="translate({X0},{Y0})"><g class="mv"><g class="fl">{"".join(rb)}</g>')
    # speech bubble (does not flip with the robot)
    if AR_RE.search(T[lang]):
        _, tw_, th_ = apix(T[lang], 14, 2, INK, 0, 0)
        bw = tw_ + 28; bh = max(38, th_ + 14); bx = 8 * S - bw // 2; by = -(bh + 6)
        g, _, _ = apix(T[lang], 14, 2, INK, bx + bw // 2, by + (bh - th_) // 2, "middle")
    else:
        _, tw_ = txt(0, 0, T[lang], 3, INK, "start")
        bw = tw_ + 28; bh = 38; bx = 8 * S - bw // 2; by = -54
        g, _ = txt(bx + bw // 2, by + 12, T[lang], 3, INK, "middle")
    o.append(f'<g class="bub">{frame(bx, by, bw, bh, CREAM, PLUM)}{rect(8 * S - 6, by + bh, 12, 4, PLUM)}{rect(8 * S - 4, by + bh, 8, 2, CREAM)}{g}</g>')
    o.append('</g></g>')
    os.makedirs(f"{OUT}/{lang}", exist_ok=True)
    open(f"{OUT}/{lang}/robot.svg", "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><style>.blink{{animation:bl 1.1s steps(1) infinite}}@keyframes bl{{50%{{opacity:0}}}}{CSS}</style>{"".join(o)}</svg>')

for l in ("en", "tr", "ar"):
    build(l)
print("ok")
