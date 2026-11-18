"""CEO/HR-oriented profile sections. Every claim is taken from the repos' READMEs or from the user."""
import sys
from px import *

OUT = sys.argv[1]
ARABIC_FONT = "'Segoe UI', Tahoma, Arial, 'DejaVu Sans', sans-serif"
MUTED = "#9b92c4"

def save(name, w, h, body, css=""):
    open(f"{OUT}/{name}.svg", "w").write(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><style>{css}'
        f'.blink{{animation:bl 1.1s steps(1) infinite}}@keyframes bl{{50%{{opacity:0}}}}</style>{body}</svg>')

def chip(x, y, label, col, sc=2, filled=False):
    w = tw(label, sc) + 8 * sc
    h = 7 * sc + 8 * sc // 2 * 1 + 4
    h = 7 * sc + 10
    if filled:
        return rect(x, y, w, h, col) + ptext(x + 4 * sc, y + 5, label, sc, INK), w
    return rect(x, y, w, h, col) + rect(x + 2, y + 2, w - 4, h - 4, INK) + ptext(x + 4 * sc, y + 5, label, sc, col), w

# ------------------------------------------------------------------ banners
def banner(name, label, col):
    w = 1200
    b = rect(0, 0, w, 64, NIGHT) + rect(0, 56, w, 8, col) + rect(0, 52, w, 4, PURPLE)
    b += ptext(24, 14, label, 5, col, shadow=PLUM)
    save(name, w, 64, b)

banner("b-built", "> WHAT I'VE BUILT", AMBER)
banner("b-more", "> MORE WORK", BLUE)
banner("b-know", "> WHAT I KNOW", GREEN)
banner("b-contact", "> CONTACT", ROSE)

# ------------------------------------------------------------------ character sheet
def sheet():
    W, H = 1200, 400
    o = [frame(0, 0, W, H, NIGHT, PLUM)]
    o.append(frame(30, 30, 300, 340, INK, TEAL))
    for i, c in enumerate(["#321a58", "#6b2a72", "#b8426a", "#ee7a4b"]):
        o.append(rect(42, 42 + i * 52, 276, 52, c))
    o.append(sprite(PLAYER[:16], PLAYER_LEG, 56, 112, 11))
    o.append(rect(42, 290, 276, 68, INK))
    o.append(ptext(180, 296, "RANIM", 6, YELLOW, anchor="middle", shadow=ORANGE))
    o.append(ptext(180, 340, "CHARACTER SHEET", 2, CREAM, anchor="middle"))
    x0 = 370
    rows = [("CLASS", "SOFTWARE ENGINEER", AMBER), ("SIDE", "VIDEO EDITOR + GRAPHIC DESIGNER", ROSE),
            ("YEAR", "SOFTWARE ENGINEERING, FINAL YEAR", TEAL), ("UNI", "ISTINYE UNIVERSITY, ISTANBUL", BLUE)]
    for i, (k, v, c) in enumerate(rows):
        y = 36 + i * 36
        o.append(ptext(x0, y, k, 3, MUTED) + ptext(x0 + 120, y, v, 3, c))
    o.append(rect(x0, 190, 800, 4, PLUM))
    o.append(ptext(x0, 214, "LANGUAGES", 3, CREAM))
    chips = [("ENGLISH", TEAL, "HELLO"), ("ARABIC", ORANGE, None), ("TURKISH", ROSE, "MERHABA")]
    cx = x0
    for name, col, hello in chips:
        w = tw(name, 3) + 36
        o.append(frame(cx, 254, w, 48, INK, col) + ptext(cx + 18, 268, name, 3, col))
        mid = cx + w // 2
        if hello:
            o.append(ptext(mid, 322, hello, 2, CREAM, anchor="middle"))
        else:
            o.append(f'<text x="{mid}" y="342" text-anchor="middle" direction="rtl" font-family="{ARABIC_FONT}" font-size="26" fill="{CREAM}">مرحبا</text>')
        cx += w + 18
    # two honest counters
    cx0 = 930
    for i, (num, lab, col) in enumerate([("6", "PROJECTS", GREEN), ("3", "LANGUAGES", AMBER)]):
        y = 222 + i * 70
        o.append(frame(cx0, y, 240, 56, INK, col))
        o.append(ptext(cx0 + 18, y + 14, num, 4, col) + ptext(cx0 + 222, y + 21, lab, 2, CREAM, anchor="end"))
    save("sheet", W, H, "".join(o))
sheet()

# ------------------------------------------------------------------ featured case cards
CASES = [
    ("01", "ORCHA", "LIVE DEMO", GREEN, TEAL,
     [("WHAT", "AI AGENT CONTROL PLANE FOR BUSINESS TEAMS"),
      ("COVERS", "WHATSAPP, VOICE, WEB CHAT, EMAIL + REVIEW QUEUE"),
      ("BUILT", "MULTI-TENANT, JWT AUTH, ROLE-BASED ACCESS"),
      ("SHIPPED", "LIVE ON RAILWAY, DOCKER, 7 PLAYWRIGHT E2E SPECS")],
     ["REACT", "NODE", "PRISMA", "POSTGRES", "DOCKER"]),
    ("02", "MEDICAL ABSTRACT CLASSIFIER", "TEAM PROJECT", BLUE, BLUE,
     [("WHAT", "FIVE-CLASS DISEASE CLASSIFIER FOR MEDICAL ABSTRACTS"),
      ("MY ROLE", "MODEL TRAINING, BIOMEDBERT FINE-TUNING, EVALUATION"),
      ("RESULT", "BIOMEDBERT: 0.8603 MACRO F1 ON A LOCKED TEST SET"),
      ("CAUGHT", "988 TRAIN/TEST OVERLAPS IN THE DATASET, REBUILT SPLITS")],
     ["PYTHON", "PYTORCH", "TRANSFORMERS", "TEAM OF 5"]),
    ("03", "TOURISM CRM DATABASE", "UNIVERSITY PROJECT", AMBER, AMBER,
     [("WHAT", "MYSQL DATABASE LAYER FOR A TOURISM CRM"),
      ("BUILT", "9 TABLES, 3 VIEWS, 2 FUNCTIONS, 6 TRIGGERS"),
      ("GUARDS", "BLOCKS OVERPAYMENT AND MISMATCHED REVIEWS"),
      ("TESTED", "SQL SUITE PLUS CONCURRENCY TESTS")],
     ["MYSQL 8", "SQL", "POWERSHELL"]),
]
for n, title_, status, scol, col, rows, tags in CASES:
    W, H = 1200, 296
    o = [frame(0, 0, W, H, NIGHT, col, hi="#ffffff22")]
    o.append(ptext(28, 28, n, 5, col))
    o.append(ptext(100, 32, title_, 4, CREAM, shadow=PURPLE))
    sw = tw(status, 2) + 24
    o.append(rect(W - 28 - sw, 30, sw, 28, scol) + ptext(W - 28 - sw + 12, 38, status, 2, INK))
    o.append(rect(28, 84, W - 56, 4, PURPLE))
    for i, (k, v) in enumerate(rows):
        y = 104 + i * 36
        o.append(ptext(28, y + 2, k, 2, MUTED) + ptext(190, y, v, 3, CREAM))
    tx = 28
    for t in tags:
        c, w = chip(tx, 252, t, col)
        o.append(c); tx += w + 10
    save(f"case-{n}", W, H, "".join(o))

# ------------------------------------------------------------------ more-work rows
MORE = [
    ("04", "CASIE EVENT EXTRACTION", "TEAM NLP PROJECT. MY PART: MODELING + EVALUATION. 26 ROLES.", "0.6196 ARG-C F1", ROSE),
    ("05", "ICELANDIC ASR DATA PREP", "TEAM PROJECT. 20H SAMROMUR SUBSET FOR WHISPER + WAV2VEC 2.0.", "0 SHARED SPEAKERS", GREEN),
    ("06", "BOOK RATING PREDICTION", "REPRODUCIBLE ML EXPERIMENT, GROUP-AWARE SPLITS, STREAMLIT DEMO.", "NO EDGE OVER BASELINE", YELLOW),
]
for n, title_, line, metric, col in MORE:
    W, H = 1200, 104
    o = [frame(0, 0, W, H, NIGHT, col)]
    o.append(ptext(24, 22, n, 3, col) + ptext(84, 22, title_, 3, CREAM))
    o.append(ptext(24, 64, line, 2, "#d9d2ee"))
    c, w = chip(W - 24 - (tw(metric, 2) + 16), 20, metric, col, filled=True)
    o.append(c)
    save(f"more-{n}", W, H, "".join(o))

# ------------------------------------------------------------------ skills panel
SKILLS = [
    ("PROGRAMMING", TEAL, ["JAVASCRIPT", "PYTHON", "SQL"]),
    ("WEB", AMBER, ["REACT", "VITE", "NODE", "EXPRESS", "PRISMA", "REST APIS"]),
    ("DATA", ORANGE, ["POSTGRESQL", "MYSQL", "SQLITE"]),
    ("ML + NLP", "#ff7eb6", ["PYTORCH", "TRANSFORMERS", "SCIKIT-LEARN", "PANDAS"]),
    ("DELIVERY", GREEN, ["DOCKER", "NGINX", "RAILWAY", "GIT", "PLAYWRIGHT", "PYTEST"]),
    ("CREATIVE", YELLOW, ["GRAPHIC DESIGN", "VIDEO EDITING"]),
    ("SPOKEN", BLUE, ["ENGLISH", "ARABIC", "TURKISH"]),
]
def skills():
    W, rh = 1200, 62
    H = rh * len(SKILLS) + 20
    o = [frame(0, 0, W, H, NIGHT, PLUM)]
    for i, (lab, col, items) in enumerate(SKILLS):
        y = 12 + i * rh
        if i:
            o.append(rect(28, y - 4, W - 56, 2, PURPLE))
        o.append(rect(28, y + 10, 8, 34, col))
        o.append(ptext(52, y + 18, lab, 3, col))
        x = 272
        for it in items:
            c, w = chip(x, y + 8, it, col, sc=3)
            o.append(c); x += w + 12
    save("skills", W, H, "".join(o))
skills()

# ------------------------------------------------------------------ contact buttons
def button(name, label, col):
    w, h = 270, 70
    o = frame(0, 0, w, h, NIGHT, col, hi="#ffffff22") + rect(8, h - 14, w - 16, 6, "#00000055")
    o += ptext(24, 24, ">", 3, col) + ptext(56, 24, label, 3, CREAM)
    save(name, w, h, o)
button("btn-github", "GITHUB", TEAL)
button("btn-linkedin", "LINKEDIN", BLUE)
button("btn-research", "RESEARCH", ROSE)
print("profile4 ok")
