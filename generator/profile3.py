"""Fact-based profile sections. Every number/label here comes from the repos' own READMEs or from the user."""
import sys
from px import *

OUT = sys.argv[1]
ARABIC_FONT = "'Segoe UI', Tahoma, Arial, 'DejaVu Sans', sans-serif"

def save(name, w, h, body, css=""):
    open(f"{OUT}/{name}.svg", "w").write(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><style>{css}'
        f'.blink{{animation:bl 1.1s steps(1) infinite}}@keyframes bl{{50%{{opacity:0}}}}'
        f'.tw{{animation:tw 2.4s steps(2) infinite}}@keyframes tw{{50%{{opacity:.25}}}}</style>{body}</svg>')

def heart(x, y, c, s=4):
    return sprite([".##.##.", "#######", "#######", ".#####.", "..###..", "...#..."], {"#": c}, x, y, s)

def dots(w, h, step=24):
    return "".join(rect(x, y, 2, 2, PURPLE) for x in range(14, w - 8, step) for y in range(14, h - 8, step))

# ------------------------------------------------------------------ banners
def banner(name, label, col):
    w = 1200
    b = rect(0, 0, w, 64, NIGHT) + rect(0, 56, w, 8, col) + rect(0, 52, w, 4, PURPLE)
    b += ptext(24, 14, label, 5, col, shadow=PLUM)
    b += heart(w - 110, 20, RED, 3) + heart(w - 140, 20, RED, 3) + heart(w - 170, 20, RED, 3)
    save(name, w, 64, b)

banner("b-sheet", "> CHARACTER SHEET", TEAL)
banner("b-quests", "> QUEST LOG", AMBER)
banner("b-tree", "> SKILL TREE", GREEN)
banner("b-ach", "> ACHIEVEMENTS", "#ff7eb6")
banner("b-tips", "> LOADING TIPS", BLUE)

# ------------------------------------------------------------------ character sheet
def sheet():
    W, H = 1200, 400
    o = [frame(0, 0, W, H, NIGHT, PLUM), dots(W, H)]
    o.append(frame(30, 30, 300, 340, INK, TEAL))
    for i, c in enumerate(["#321a58", "#6b2a72", "#b8426a", "#ee7a4b"]):
        o.append(rect(42, 42 + i * 52, 276, 52, c))
    o.append(sprite(PLAYER[:16], PLAYER_LEG, 56, 112, 11))
    o.append(rect(42, 290, 276, 68, INK))
    o.append(ptext(180, 298, "RANIM", 6, YELLOW, anchor="middle", shadow=ORANGE))
    o.append(ptext(180, 342, "PLAYER 1", 2, CREAM, anchor="middle"))
    x0 = 370
    rows = [("CLASS ", "SOFTWARE ENGINEER", AMBER), ("SIDE  ", "VIDEO EDITOR + GRAPHIC DESIGNER", ROSE),
            ("YEAR  ", "FINAL-YEAR SE STUDENT", TEAL), ("GUILD ", "TEAM ULTRON (NLP)", BLUE)]
    for i, (k, v, c) in enumerate(rows):
        y = 32 + i * 32
        o.append(ptext(x0, y, k + ":", 3, "#9b92c4") + ptext(x0 + 130, y, v, 3, c))
    o.append(rect(x0, 170, 800, 4, PLUM))
    o.append(ptext(x0, 192, "LANGUAGES", 3, CREAM))
    chips = [("ENGLISH", TEAL, "HELLO"), ("ARABIC", ORANGE, None), ("TURKISH", ROSE, "MERHABA")]
    cx = x0
    for name, col, hello in chips:
        w = tw(name, 3) + 36
        o.append(frame(cx, 232, w, 48, INK, col) + ptext(cx + 18, 246, name, 3, col))
        mid = cx + w // 2
        if hello:
            o.append(ptext(mid, 300, hello, 2, CREAM, anchor="middle"))
        else:
            o.append(f'<text x="{mid}" y="320" text-anchor="middle" direction="rtl" font-family="{ARABIC_FONT}" font-size="26" fill="{CREAM}">مرحبا</text>')
        cx += w + 18
    # counters
    cx0 = 930
    for i, (num, lab, col) in enumerate([("6", "PROJECTS", GREEN), ("3", "LANGUAGES", AMBER), ("0.86", "BEST F1", ROSE)]):
        y = 190 + i * 62
        o.append(frame(cx0, y, 240, 52, INK, col))
        o.append(ptext(cx0 + 16, y + 12, num, 4, col) + ptext(cx0 + 224, y + 19, lab, 2, CREAM, anchor="end"))
    save("sheet", W, H, "".join(o))
sheet()

# ------------------------------------------------------------------ quests (real repos)
QUESTS = [
    ("01", "ORCHA", "LIVE DEMO", GREEN, ["AI AGENT CONTROL PLANE WITH", "A HUMAN REVIEW QUEUE."], ["REACT", "NODE", "POSTGRES", "DOCKER"], TEAL),
    ("02", "TOURISM CRM", "MYSQL", AMBER, ["9 TABLES, 3 VIEWS, 6 TRIGGERS", "GUARDING BOOKINGS + PAYMENTS."], ["SQL", "TRIGGERS", "TESTS"], ORANGE),
    ("03", "MEDICAL NLP", "0.8603 F1", BLUE, ["BIOMEDBERT ON MEDICAL ABSTRACTS.", "I TRAINED, COMPARED, EVALUATED."], ["PYTORCH", "NLP", "TEAM"], BLUE),
    ("04", "CASIE EVENTS", "0.6196 F1", ROSE, ["CYBERSECURITY EVENT ARGUMENTS,", "26 ROLES, ROBERTA SELECTED."], ["NLP", "ROBERTA", "TEAM"], ROSE),
    ("05", "ICELANDIC ASR", "20H AUDIO", GREEN, ["SPEAKER-SEPARATED SPLITS FOR", "WHISPER AND WAV2VEC 2.0."], ["SPEECH", "DATA", "TEAM"], GREEN),
    ("06", "BOOK RATINGS", "HONEST RESULT", YELLOW, ["ML THAT DID NOT BEAT THE", "BASELINE. REPORTED ANYWAY."], ["SKLEARN", "STREAMLIT"], YELLOW),
]
for n, title_, status, scol, desc, tags, col in QUESTS:
    w, h = 590, 200
    o = [frame(0, 0, w, h, NIGHT, col, hi="#ffffff22"), rect(8, 8, w - 16, 4, "#ffffff11")]
    o.append(ptext(24, 24, f"QUEST {n}", 2, col))
    o.append(ptext(22, 54, title_, 4, CREAM, shadow=PURPLE))
    sw = tw(status, 2) + 20
    o.append(rect(w - 22 - sw, 22, sw, 24, scol) + ptext(w - 22 - sw + 10, 28, status, 2, INK))
    for i, line in enumerate(desc):
        o.append(ptext(22, 98 + i * 22, line, 2, "#d9d2ee"))
    tx = 22
    for t in tags:
        tgw = tw(t, 2) + 16
        o.append(rect(tx, 152, tgw, 28, col) + rect(tx + 2, 154, tgw - 4, 24, INK) + ptext(tx + 8, 160, t, 2, col))
        tx += tgw + 8
    save(f"quest-{n}", w, h, "".join(o))

# ------------------------------------------------------------------ skill tree
def tree():
    W, H = 1200, 470
    o = [rect(0, 0, W, H, NIGHT), dots(W, H)]
    branches = [
        ("BUILD", TEAL, ["REACT 18", "VITE", "NODE + EXPRESS", "PRISMA", "RECHARTS"]),
        ("DATA", AMBER, ["POSTGRESQL", "MYSQL 8", "SQLITE", "SQL TRIGGERS", "SCHEMA DESIGN"]),
        ("ML + NLP", ROSE, ["PYTHON", "PYTORCH", "TRANSFORMERS", "SCIKIT-LEARN", "PANDAS"]),
        ("SHIP + TEST", GREEN, ["DOCKER + NGINX", "RAILWAY", "PLAYWRIGHT", "PYTEST", "GIT + LFS"]),
    ]
    colw = 300
    # root
    rw = tw("RANIM", 4) + 40
    rx = W // 2 - rw // 2
    o.append(frame(rx, 14, rw, 52, INK, YELLOW) + ptext(W // 2, 28, "RANIM", 4, YELLOW, anchor="middle"))
    o.append(rect(W // 2 - 3, 66, 6, 22, PLUM))
    o.append(rect(150 - 3, 88, 900 + 6, 6, PLUM))
    for i, (name, col, items) in enumerate(branches):
        cx = 150 + i * colw
        o.append(rect(cx - 3, 88, 6, 22, PLUM))
        bw = 232
        o.append(frame(cx - bw // 2, 110, bw, 48, INK, col) + ptext(cx, 124, name, 3, col, anchor="middle"))
        o.append(rect(cx - 3, 158, 6, 16, PLUM))
        for j, it in enumerate(items):
            y = 174 + j * 56
            o.append(rect(cx - 3, y - 6, 6, 8, PLUM))
            o.append(rect(cx - bw // 2 + 6, y, bw - 12, 44, col) + rect(cx - bw // 2 + 10, y + 4, bw - 20, 36, INK))
            o.append(rect(cx - bw // 2 + 16, y + 14, 14, 14, col, f'class="tw" style="animation-delay:-{(i*5+j)*0.37:.2f}s"'))
            o.append(ptext(cx - bw // 2 + 40, y + 15, it, 2, CREAM))
        # chain connector between chips drawn above (6px posts)
    save("tree", W, H, "".join(o))
tree()

# ------------------------------------------------------------------ achievements
TROPHY = ["..######..", "#.######.#", "#.######.#", ".########.", "..######..", "...####...", "....##....", "....##....", "...####...", "..######.."]
ACH = [
    ("0.8603", "MACRO F1 ON LOCKED TEST", "BIOMEDBERT, 5 DISEASES", BLUE),
    ("988", "TRAIN-TEST LEAKS FOUND", "IN THE ORIGINAL CORPUS", ROSE),
    ("26", "EVENT ROLES TO EXTRACT", "ROBERTA, 0.6196 ARG-C F1", AMBER),
    ("0", "SHARED SPEAKERS", "ACROSS ICELANDIC SPLITS", GREEN),
    ("7", "PLAYWRIGHT E2E SPECS", "TESTING THE ORCHA APP", TEAL),
    ("6", "DATABASE TRIGGERS", "GUARD BOOKINGS + PAYMENTS", ORANGE),
]
def ach():
    W, H = 1200, 320
    o = [rect(0, 0, W, H, NIGHT), dots(W, H)]
    for i, (num, l1, l2, col) in enumerate(ACH):
        x = (i % 3) * 410
        y = 10 + (i // 3) * 150
        o.append(frame(x, y, 380, 130, INK, col, hi="#ffffff22"))
        o.append(sprite(TROPHY, {"#": col}, x + 308, y + 18, 6) if False else "")
        o.append(ptext(x + 20, y + 18, num, 6, col, shadow=PURPLE))
        o.append(sprite(["..#..", ".###.", "#####", ".###.", "..#.."], {"#": YELLOW}, x + 336, y + 14, 5))
        o.append(ptext(x + 20, y + 74, l1, 2, CREAM))
        o.append(ptext(x + 20, y + 98, l2, 2, "#9b92c4"))
    save("ach", W, H, "".join(o))
ach()

# ------------------------------------------------------------------ loading tips (how I work)
def tips():
    W, H = 1200, 170
    TIPS = ["START WITH THE SYSTEM BOUNDARY", "MAKE RESULTS REPRODUCIBLE", "SEPARATE MEASURED FROM ASSUMED", "DOCUMENT LIMITS AS RESULTS"]
    css = ""
    o = [frame(0, 0, W, H, INK, BLUE), dots(W, H)]
    for i, t in enumerate(TIPS):
        css += f".t{i}{{opacity:0;animation:tp 16s steps(1) infinite;animation-delay:{i*4}s}}"
        o.append(f'<g class="t{i}">{ptext(40, 40, f"TIP {i+1}/4", 2, BLUE)}{ptext(40, 76, t, 4, CREAM, shadow=PURPLE)}</g>')
    css += "@keyframes tp{0%{opacity:1}25%{opacity:0}100%{opacity:0}}"
    o.append(rect(40, 130, 1120, 14, PURPLE) + rect(40, 130, 1120, 4, "#ffffff22"))
    o.append(f'<rect x="40" y="130" height="14" fill="{BLUE}" style="animation:bar 16s steps(40) infinite" width="1120"/>')
    css += "@keyframes bar{from{transform:scaleX(0)}to{transform:scaleX(1)}}rect[style*='bar']{transform-box:fill-box;transform-origin:left}"
    save("tips", W, H, "".join(o), css)
tips()

# ------------------------------------------------------------------ next level + buttons + footer
def nextlevel():
    W, H = 1200, 200
    o = [rect(0, 0, W, H, INK), rect(0, 0, W, 4, PLUM)]
    o.append(ptext(600, 26, "NEXT LEVEL LOADING...", 5, YELLOW, anchor="middle", shadow=ORANGE))
    o.append(rect(100, 84, 1000, 28, PURPLE) + rect(104, 88, 992, 20, INK))
    css = "@keyframes ld{from{transform:scaleX(.08)}to{transform:scaleX(1)}}.ld{transform-box:fill-box;transform-origin:left;animation:ld 6s steps(24) infinite alternate}"
    o.append(f'<rect class="ld" x="104" y="88" width="992" height="20" fill="{GREEN}"/>')
    o.append(ptext(600, 136, "SPEECH + BIOMEDICAL NLP + EVALUATION DESIGN", 3, CREAM, anchor="middle"))
    o.append(ptext(600, 168, "APPLIED NLP, BIOMEDICAL LANGUAGE MODELS, SPEECH PROCESSING", 1, "#9b92c4", anchor="middle"))
    save("next", W, H, "".join(o), css)
nextlevel()

def button(name, label, col):
    w, h = 270, 70
    o = frame(0, 0, w, h, NIGHT, col, hi="#ffffff22") + rect(8, h - 14, w - 16, 6, "#00000055")
    o += f'<g class="blink" style="animation-duration:1.6s">{ptext(20, 24, ">", 3, col)}</g>' + ptext(52, 24, label, 3, CREAM)
    save(name, w, h, o)
button("btn-github", "GITHUB", TEAL)
button("btn-linkedin", "LINKEDIN", BLUE)
button("btn-research", "RESEARCH", ROSE)
button("btn-demo", "ORCHA DEMO", GREEN)
print("profile3 ok")
