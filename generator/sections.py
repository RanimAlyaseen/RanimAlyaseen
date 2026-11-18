import sys
from px import *

OUT = sys.argv[1]

def save(name, w, h, body, css=""):
    open(f"{OUT}/{name}.svg", "w").write(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><style>{css}'
        f'.blink{{animation:bl 1.1s steps(1) infinite}}@keyframes bl{{50%{{opacity:0}}}}'
        f'.tw{{animation:tw 2.4s steps(2) infinite}}@keyframes tw{{50%{{opacity:.2}}}}</style>{body}</svg>')

def star(x, y, c, s=4):
    return sprite(["..#..", ".###.", "#####", ".###.", "..#.."], {"#": c}, x, y, s)

def heart(x, y, c, s=4):
    return sprite([".##.##.", "#######", "#######", ".#####.", "..###..", "...#..."], {"#": c}, x, y, s)

# ------------------------------------------------------------ section banners
def banner(name, label, col):
    w = 1200
    b = rect(0, 0, w, 64, NIGHT) + rect(0, 56, w, 8, col) + rect(0, 52, w, 4, PURPLE)
    b += ptext(24, 14, label, 5, col, shadow=PLUM)
    b += f'<g class="blink">{ptext(w - 24, 22, "1UP", 3, CREAM, anchor="end")}</g>'
    b += heart(w - 110, 20, RED, 3) + heart(w - 140, 20, RED, 3) + heart(w - 170, 20, "#5b2a6e", 3)
    save(name, w, 64, b)

banner("b-sheet", "> CHARACTER SHEET", TEAL)
banner("b-quests", "> QUEST LOG", AMBER)
banner("b-inv", "> INVENTORY", "#ff7eb6")
banner("b-map", "> WORLD MAP", GREEN)

# ------------------------------------------------------------ character sheet
def sheet():
    W, H = 1200, 400
    o = [rect(0, 0, W, H, NIGHT)]
    # dot grid
    o.append(frame(0, 0, W, H, NIGHT, PLUM))
    o.append("".join(rect(x, y, 2, 2, PURPLE) for x in range(14, W - 8, 24) for y in range(14, H - 8, 24)))
    # portrait
    o.append(frame(30, 30, 300, 340, INK, TEAL))
    for i, c in enumerate(["#321a58", "#6b2a72", "#b8426a", "#ee7a4b"]):
        o.append(rect(42, 42 + i * 52, 276, 52, c))
    o.append(rect(42, 250, 276, 6, "#0e0720") )
    o.append(sprite(PLAYER[:16], PLAYER_LEG, 56, 112, 11))
    o.append(rect(42, 290, 276, 68, INK))
    o.append(ptext(180, 298, "RANIM", 6, YELLOW, anchor="middle", shadow=ORANGE))
    o.append(ptext(180, 342, "PLAYER 1", 2, CREAM, anchor="middle"))
    # info
    x0 = 370
    o.append(ptext(x0, 34, "NAME  : RANIM ALYASEEN", 3, CREAM))
    o.append(ptext(x0, 66, "CLASS : SWE / DESIGNER / EDITOR", 3, AMBER))
    o.append(rect(x0, 100, 800, 4, PLUM))
    stats = [("CODE", 9, TEAL, "9"), ("ARCHITECT", 8, BLUE, "8"), ("ML / NLP", 7, GREEN, "7"), ("DESIGN", 9, ORANGE, "9"), ("VIDEO EDIT", 9, ROSE, "9"),
             ("COFFEE", 10, YELLOW, "MAX"), ("SLEEP", 2, RED, "LOW")]
    for i, (lab, v, col, txt) in enumerate(stats):
        y = 116 + i * 31
        o.append(ptext(x0, y + 2, lab, 3, CREAM))
        for k in range(10):
            on = k < v
            sx = x0 + 240 + k * 36
            o.append(rect(sx, y, 30, 22, col if on else "#2d1b4e",
                          f'style="animation:seg .01s backwards;animation-delay:{(i*10+k)*0.015:.2f}s"'))
            if on:
                o.append(rect(sx, y, 30, 6, "#ffffff44"))
        o.append(ptext(x0 + 240 + 360 + 20, y + 2, txt, 3, col))
    o.append(rect(x0, 354, 800, 4, PLUM))
    o.append(ptext(x0, 368, "MOVES: SHIP IT / PIXEL PERFECT / CUT TO BEAT", 2, AMBER))
    css = "@keyframes seg{from{opacity:0}to{opacity:1}}"
    save("sheet", W, H, "".join(o), css)

sheet()

# ------------------------------------------------------------ quest cards
QUESTS = [
    ("01", "ORCHA", "FULL-STACK", GREEN, ["AI AGENT MANAGEMENT PLATFORM.", "MULTI-TENANT, JWT, DOCKER."], ["REACT", "NODE", "POSTGRES"], TEAL),
    ("02", "TOURISM CRM", "DATABASE", AMBER, ["MYSQL CRM DATA LAYER WITH", "TRIGGERS AND SAFE PAYMENTS."], ["MYSQL", "SQL", "TESTS"], ORANGE),
    ("03", "MEDICAL NLP", "0.86 MACRO F1", BLUE, ["BIOMEDBERT CLASSIFIES MEDICAL", "ABSTRACTS. LOCKED TEST SET."], ["PYTORCH", "NLP"], BLUE),
    ("04", "NEXT QUEST", "OPEN SLOT", RED, ["YOUR PROJECT HERE. LET'S", "BUILD SOMETHING GOOD."], ["COLLAB"], ROSE),
]
for n, title_, status, scol, desc, tags, col in QUESTS:
    w, h = 590, 220
    o = [frame(0, 0, w, h, NIGHT, col, hi="#ffffff22")]
    o.append(rect(8, 8, w - 16, 4, "#ffffff11"))
    o.append(f'<g class="blink">{ptext(24, 20, "!", 3, YELLOW)}</g>')
    o.append(ptext(50, 26, f"QUEST {n}", 2, col))
    o.append(ptext(22, 62, title_, 4, CREAM, shadow=PURPLE))
    sw = tw(status, 2) + 20
    o.append(rect(w - 22 - sw, 22, sw, 24, scol) + ptext(w - 22 - sw + 10, 28, status, 2, INK))
    for i, line in enumerate(desc):
        o.append(ptext(22, 104 + i * 22, line, 2, "#d9d2ee"))
    tx = 22
    o.append(ptext(22, 160, "REWARD:", 2, YELLOW))
    tx = 22 + tw("REWARD: ", 2) + 6
    for t in tags:
        tgw = tw(t, 2) + 16
        o.append(rect(tx, 154, tgw, 28, col) + rect(tx + 2, 156, tgw - 4, 24, INK) + ptext(tx + 8, 162, t, 2, col))
        tx += tgw + 8
    o.append(rect(22, 192, w - 44, 4, PURPLE))
    o.append(rect(22, 192, int((w - 44) * {"01": .92, "02": .55, "03": .8, "04": .3}[n]), 4, col))
    save(f"quest-{n}", w, h, "".join(o))

# ------------------------------------------------------------ inventory
ICON = {
 "brush": (["..........kk", ".........kyk", "........kyk.", ".......kyk..", "......kyk...", ".....kyk....", "....kcck....", "...kcck.....", "..kttk......", ".kttttk.....", ".kttttk.....", "..kkkk......"], dict(k=INK, y=YELLOW, c="#cfd3e8", t=TEAL)),
 "clap":  (["kkkkkkkkkkkk", "kowowowowowk", "kkkkkkkkkkkk", "kcccccccccck", "kccocccccccck", "kccooccccccck", "kcccoooccccck", "kcccooocccck", "kccooccccccck", "kccocccccccck", "kcccccccccck", "kkkkkkkkkkkk"], dict(k=INK, o=ORANGE, w="#ffffff", c="#4a4f78")),
 "layers": (["...kkkkkk...", "..kyyyyyyk..", ".kyyyyyyyyk.", "..kkkkkkkk..", "..kttttttk..", ".kttttttttk.", "..kkkkkkkk..", "..koooooook.", ".koooooooook", "..kkkkkkkk.."], dict(k=INK, y=YELLOW, t=TEAL, o=ORANGE)),
 "robot": ([".....kk.....", ".....rk.....", "..kkkkkkkk..", ".kccccccccck", ".kcbbccbbck.", ".kcbbccbbck.", ".kccccccccck", ".kcckkkkcck.", "..kkkkkkkk..", ".kk.kccc.kk.", ".kk.kccc.kk.", "....kkkk...."], dict(k=INK, c="#8c90b0", b=TEAL, r=RED)),
 "chat":  (["..kkkkkkkk..", ".kwwwwwwwwk.", "kwwwwwwwwwwk", "kwwkwwkwwkwk", "kwwwwwwwwwwk", ".kwwwwwwwwk.", "..kkwkkkkk..", "....kwk.....", ".....k......"], dict(k=INK, w=CREAM)),
}
ITEMS = [("CODE", None, TEAL, "FRONT + BACK"), ("DESIGN", "brush", ORANGE, "UI + BRAND"), ("VIDEO", "clap", ROSE, "EDIT+MOTION"),
         ("SYSTEMS", "layers", YELLOW, "ARCHITECTURE"), ("ML / NLP", "robot", BLUE, "APPLIED ML"), ("AR + EN", "chat", GREEN, "BILINGUAL")]
o = [rect(0, 0, 1200, 250, NIGHT)]
o.append("".join(rect(x, y, 2, 2, PURPLE) for x in range(10, 1200, 24) for y in range(10, 250, 24)))
for i, (name, ic, col, sub) in enumerate(ITEMS):
    x = 22 + i * 190
    o.append(frame(x, 16, 176, 220, INK, col))
    o.append(rect(x + 12, 28, 152, 4, "#ffffff22"))
    cx = x + 88
    if ic is None:
        o.append(ptext(cx, 70, "</>", 6, col, anchor="middle"))
    else:
        grid, leg = ICON[ic]
        o.append(f'<g class="tw" style="animation-delay:-{i*.4:.1f}s">' + sprite(grid, leg, cx - 36, 54, 6) + "</g>" if False else sprite(grid, leg, cx - 36, 54, 6))
    o.append(rect(x + 12, 140, 152, 4, PURPLE))
    o.append(ptext(cx, 158, name, 2 if len(name) > 7 else 3, CREAM, anchor="middle"))
    o.append(ptext(cx, 192, sub, 2, col, anchor="middle"))
    o.append(ptext(x + 160, 214, "X1", 1, YELLOW, anchor="end"))
save("inventory", 1200, 250, "".join(o))

# ------------------------------------------------------------ CTA + buttons
def cta():
    W, H = 1200, 300
    o = [rect(0, 0, W, H, INK)]
    for i, c in enumerate(["#1b1033", "#241446", "#321a58"]):
        o.append(rect(0, i * 100, W, 100, c))
    for x in range(0, W, 48):
        o.append(rect(x, 276, 24, 24, "#1d1038"))
    o.append(ptext(600, 30, "CONTINUE?", 12, YELLOW, anchor="middle", shadow=ORANGE))
    css = ""
    digits = ""
    for i, d in enumerate("9876543210"):
        css += f".d{i}{{animation:dd 10s steps(1) infinite;animation-delay:{i}s;opacity:0}}"
        digits += f'<g class="d{i}">{ptext(600, 130, d, 14, CREAM, anchor="middle", shadow=ROSE)}</g>'
    css += "@keyframes dd{0%{opacity:1}10%{opacity:0}100%{opacity:0}}"
    o.append(digits)
    o.append(f'<g class="blink">{ptext(600, 236, "INSERT COIN TO COLLAB", 3, AMBER, anchor="middle")}</g>')
    for x in (330, 850):
        o.append(sprite(["..##..", ".####.", "######", "######", ".####.", "..##.."], {"#": YELLOW}, x, 232, 5))
    save("cta", W, H, "".join(o), css)
cta()

def button(name, label, col):
    w, h = 270, 70
    o = frame(0, 0, w, h, NIGHT, col, hi="#ffffff22")
    o += rect(8, h - 14, w - 16, 6, "#00000055")
    o += f'<g class="blink" style="animation-duration:1.6s">{ptext(20, 24, ">", 3, col)}</g>'
    o += ptext(52, 24, label, 3, CREAM)
    save(name, w, h, o)
button("btn-github", "GITHUB", TEAL)
button("btn-research", "RESEARCH", ROSE)
button("btn-linkedin", "LINKEDIN", BLUE)
button("btn-portfolio", "PORTFOLIO", ORANGE)

# footer
o = rect(0, 0, 1200, 90, INK) + rect(0, 0, 1200, 4, PLUM)
o += "".join(rect(x, 4, 24, 12, "#2d1b4e") for x in range(0, 1200, 48))
o += ptext(600, 40, "MADE WITH PIXELS + STUBBORNNESS", 3, CREAM, anchor="middle")
o += star(300, 36, YELLOW, 3) + star(884, 36, YELLOW, 3)
save("footer", 1200, 90, o)
print("sections ok")
