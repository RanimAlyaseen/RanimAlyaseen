"""Tiny pixel-art toolkit: 5x7 bitmap font + sprite renderer that emits compact SVG paths."""

INK, NIGHT, PURPLE, PLUM, ROSE = "#140a26", "#1b1033", "#2d1b4e", "#5b2a6e", "#a23e6c"
ORANGE, AMBER, CREAM, TEAL, YELLOW = "#e8683a", "#f4a259", "#f6e8c8", "#2ec4b6", "#f2c94c"
RED, GREEN, BLUE = "#e63946", "#7bd88f", "#4cc9f0"

FONT = {
"A": ".###.|#...#|#...#|#####|#...#|#...#|#...#",
"B": "####.|#...#|#...#|####.|#...#|#...#|####.",
"C": ".####|#....|#....|#....|#....|#....|.####",
"D": "####.|#...#|#...#|#...#|#...#|#...#|####.",
"E": "#####|#....|#....|####.|#....|#....|#####",
"F": "#####|#....|#....|####.|#....|#....|#....",
"G": ".####|#....|#....|#..##|#...#|#...#|.###.",
"H": "#...#|#...#|#...#|#####|#...#|#...#|#...#",
"I": "#####|..#..|..#..|..#..|..#..|..#..|#####",
"J": "..###|...#.|...#.|...#.|...#.|#..#.|.##..",
"K": "#...#|#..#.|#.#..|##...|#.#..|#..#.|#...#",
"L": "#....|#....|#....|#....|#....|#....|#####",
"M": "#...#|##.##|#.#.#|#.#.#|#...#|#...#|#...#",
"N": "#...#|##..#|#.#.#|#..##|#...#|#...#|#...#",
"O": ".###.|#...#|#...#|#...#|#...#|#...#|.###.",
"P": "####.|#...#|#...#|####.|#....|#....|#....",
"Q": ".###.|#...#|#...#|#...#|#.#.#|#..#.|.##.#",
"R": "####.|#...#|#...#|####.|#.#..|#..#.|#...#",
"S": ".####|#....|#....|.###.|....#|....#|####.",
"T": "#####|..#..|..#..|..#..|..#..|..#..|..#..",
"U": "#...#|#...#|#...#|#...#|#...#|#...#|.###.",
"V": "#...#|#...#|#...#|#...#|#...#|.#.#.|..#..",
"W": "#...#|#...#|#...#|#.#.#|#.#.#|##.##|#...#",
"X": "#...#|#...#|.#.#.|..#..|.#.#.|#...#|#...#",
"Y": "#...#|#...#|.#.#.|..#..|..#..|..#..|..#..",
"Z": "#####|....#|...#.|..#..|.#...|#....|#####",
"0": ".###.|#...#|#..##|#.#.#|##..#|#...#|.###.",
"1": "..#..|.##..|..#..|..#..|..#..|..#..|.###.",
"2": ".###.|#...#|....#|...#.|..#..|.#...|#####",
"3": "####.|....#|....#|.###.|....#|....#|####.",
"4": "...#.|..##.|.#.#.|#..#.|#####|...#.|...#.",
"5": "#####|#....|####.|....#|....#|#...#|.###.",
"6": ".###.|#....|#....|####.|#...#|#...#|.###.",
"7": "#####|....#|...#.|..#..|.#...|.#...|.#...",
"8": ".###.|#...#|#...#|.###.|#...#|#...#|.###.",
"9": ".###.|#...#|#...#|.####|....#|....#|.###.",
" ": ".....|.....|.....|.....|.....|.....|.....",
".": ".....|.....|.....|.....|.....|..##.|..##.",
",": ".....|.....|.....|.....|..##.|..#..|.#...",
":": ".....|..#..|..#..|.....|..#..|..#..|.....",
"-": ".....|.....|.....|#####|.....|.....|.....",
"+": ".....|..#..|..#..|#####|..#..|..#..|.....",
"!": "..#..|..#..|..#..|..#..|..#..|.....|..#..",
"?": ".###.|#...#|....#|...#.|..#..|.....|..#..",
"/": "....#|....#|...#.|..#..|.#...|#....|#....",
">": "#....|.#...|..#..|...#.|..#..|.#...|#....",
"<": "....#|...#.|..#..|.#...|..#..|...#.|....#",
"'": "..#..|..#..|.....|.....|.....|.....|.....",
"_": ".....|.....|.....|.....|.....|.....|#####",
"=": ".....|.....|#####|.....|#####|.....|.....",
"*": ".....|#.#.#|.###.|#####|.###.|#.#.#|.....",
"&": ".##..|#..#.|#.#..|.#...|#.#.#|#..#.|.##.#",
"#": ".#.#.|#####|.#.#.|.#.#.|#####|.#.#.|.....",
"(": "..##.|.#...|#....|#....|#....|.#...|..##.",
")": ".##..|...#.|....#|....#|....#|...#.|.##..",
"%": "##..#|##..#|...#.|..#..|.#...|#..##|#..##",
}


FONT["Ü"]=".#.#.|.....|"+FONT["U"]
FONT["Ö"]=".#.#.|.....|"+FONT["O"]
FONT["İ"]="..#..|.....|"+FONT["I"]
FONT["Ğ"]=".#.#.|..#..|"+FONT["G"]
FONT["Ç"]=FONT["C"].rsplit("|",1)[0]+"|.####|..#..|.##.."
FONT["Ş"]=FONT["S"]+"|..#..|.##.."
FONT["Â"]="..#..|.#.#.|"+FONT["A"]
ABOVE=set("ÜÖİĞÂ")

def tw(s, sc):
    """pixel width of a string at scale sc"""
    return len(s) * 6 * sc - sc

def ptext(x, y, s, sc, color, shadow=None, anchor="start", extra=""):
    """pixel text as one path (plus an optional offset shadow path)."""
    s = s.upper()
    if anchor == "middle":
        x -= tw(s, sc) // 2
    elif anchor == "end":
        x -= tw(s, sc)
    def build(ox, oy):
        d = []
        cx = x + ox
        for ch in s:
            g = FONT.get(ch, FONT["?"]).split("|")
            for r, row in enumerate(g):
                c = 0
                while c < 5:
                    if row[c] == "#":
                        e = c
                        while e < 5 and row[e] == "#":
                            e += 1
                        d.append(f"M{cx + c*sc} {y + (-2*sc if (ch in ABOVE) else 0) + r*sc + oy}h{(e-c)*sc}v{sc}h-{(e-c)*sc}z")
                        c = e
                    else:
                        c += 1
            cx += 6 * sc
        return "".join(d)
    out = ""
    if shadow:
        sh = max(1, sc // 3) if sc > 2 else 1
        out += f'<path fill="{shadow}" d="{build(sh, sh)}"/>'
    out += f'<path fill="{color}" d="{build(0, 0)}" {extra}/>'
    return out

def sprite(grid, leg, x, y, s, extra=""):
    """render a list-of-strings sprite; '.' is transparent."""
    w = max(len(r) for r in grid)
    runs = {}
    for r, row in enumerate(grid):
        row = row.ljust(w, ".")
        c = 0
        while c < w:
            ch = row[c]
            if ch == ".":
                c += 1
                continue
            e = c
            while e < w and row[e] == ch:
                e += 1
            runs.setdefault(ch, []).append(f"M{x + c*s} {y + r*s}h{(e-c)*s}v{s}h-{(e-c)*s}z")
            c = e
    body = "".join(f'<path fill="{leg[ch]}" d="{"".join(v)}"/>' for ch, v in runs.items())
    return f'<g shape-rendering="crispEdges" {extra}>{body}</g>'

def rect(x, y, w, h, fill, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" {extra}/>'

def frame(x, y, w, h, bg, border, hi=None, px=4):
    """chunky RPG dialog frame with notched corners and double border."""
    o = rect(x + px, y, w - 2*px, h, border) + rect(x, y + px, w, h - 2*px, border)
    o += rect(x + px, y + px, w - 2*px, h - 2*px, bg)
    if hi:
        o += rect(x + 2*px, y + px, w - 4*px, px, hi)
    return o

# ---------------------------------------------------------------- character
PLAYER_OLD_LEG = dict(h="#2a1a14", s="#e9a97b", d="#c98259", p=TEAL, P="#1f8f85", o=ORANGE, O="#b24325",
                  n="#2d3a6b", N="#1f2850", w="#ffffff", k=NIGHT, b=NIGHT, c="#4a4f78", C="#363a5c", y=YELLOW)

PLAYER_OLD = [
"......PPPPPPPP........",
".....PhhhhhhhhP.......",
"....hhhhhhhhhhhh......",
"....hhhhhhhhssss......",
"...pphhhhhhhsskss.....",
"...pphhhhhhhsssssd....",
"...pphhhhhhhsssss.....",
"....phhhhhhsssssd.....",
".....hhhhhhssssd......",
"......hhhhsssss.......",
".......ssssss.........",
"......oooooooo........",
".....oooooooooo.......",
"..cc.oooooooooooo.....",
"..cc.ooooooooooOOOss..",
"..cc.oooooooooooooss..",
"..cc.ooooooooooo......",
"..cc.ooooooooooo......",
"..ccnnnnnnnnnnnnn.....",
"..CCnnnnnnnnnnnnnn....",
"..CC.NNNNNN.....nn....",
"..CC............nn....",
"..CC............nn....",
"..CCC..........bbbb...",
"..C............bbbbb..",
]


# ---------------------------------------------------------------- diva character, pink / black / purple (same 22x25 grid as before)
PLAYER_LEG = {'h': '#0b0610', 's': '#e9a97b', 'd': '#c98259', 'p': '#2ec4b6', 'P': '#05020a', 'o': '#ff3d94', 'O': '#7b3fd0', 'n': '#2d3a6b', 'N': '#1f2850', 'w': '#ffffff', 'k': '#1b1033', 'b': '#1b1033', 'c': '#4a4f78', 'C': '#363a5c', 'y': '#f2c94c', 'H': '#9a4fe8', 'l': '#e0197d', 'S': '#ff7bbd', 'V': '#b05cff', 'v': '#8a4fe0', 'f': '#ff3d94'}

PLAYER = [
".....S.S.S.S..........",
"....SSSSVSSSS.........",
"....hHhhhhhhhh........",
"...Hhhfhhhhhsvkkv.....",
"...hhhhhHhhhsskskk....",
".hHhhhhfhhhhsssssd....",
".hfhhhHhhhhhsssss.....",
".hhHhhhhhhhssslld.....",
".hhfhhhhhhSssssd......",
".hHhhhhhhVsssss.......",
".hfhhhhsSSVSs.........",
".hHhhSOOOOOOOO........",
".hfhhOoooooooooO......",
".hHh.oooooooooooo.....",
".hfh.ooooooooooOOOss..",
".hHh.oooooooooooooss..",
".hhh.ooooooooooo......",
"..cc.ooooooooooo......",
"..ccnnnnnnnnnnnnn.....",
"..CCnnnnnnnnnnnnnn....",
"..CC.NNNNNN.....nn....",
"..CC............nn....",
"..CC............nn....",
"..CCC..........bbbb...",
"..C............bbbbb..",
]


# ---------------------------------------------------------------- Arabic as real pixel art (rasterised, shaped by raqm)
import re as _re
from PIL import Image, ImageDraw, ImageFont
AR_RE = _re.compile(r"[\u0600-\u06FF]")
_AF = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
def apix(text, size, sc, color, x, y, anchor="start", shadow=None):
    f = ImageFont.truetype(_AF, size, layout_engine=ImageFont.Layout.RAQM)
    im = Image.new("L", (size * len(text) * 2 + 20, size * 3), 0)
    d = ImageDraw.Draw(im); d.fontmode = "1"
    d.text((10, size // 2), text, font=f, fill=255, direction="rtl", language="ar")
    bb = im.getbbox()
    im = im.crop(bb); w, h = im.size
    px = im.load()
    if anchor == "middle": x -= (w * sc) // 2
    elif anchor == "end": x -= w * sc
    def build(ox, oy):
        out = []
        for r in range(h):
            c = 0
            while c < w:
                if px[c, r] > 127:
                    e = c
                    while e < w and px[e, r] > 127: e += 1
                    out.append(f"M{x + ox + c*sc} {y + oy + r*sc}h{(e-c)*sc}v{sc}h-{(e-c)*sc}z"); c = e
                else: c += 1
        return "".join(out)
    o = ""
    if shadow:
        sh = max(1, sc // 3)
        o += f'<path fill="{shadow}" d="{build(sh, sh)}"/>'
    o += f'<path fill="{color}" d="{build(0, 0)}"/>'
    return o, w * sc, h * sc

def txt(x, y, s, sc, color, anchor="start", shadow=None, extra=""):
    """pixel text for Latin/Turkish (bitmap font) or Arabic (rasterised). returns (svg, width)."""
    if AR_RE.search(s):
        o, w, h = apix(s, 5 * sc + 1 if sc >= 3 else 10, max(1, round(sc * 2 / 3)) if sc >= 3 else 2, color, x, y, anchor, shadow)
        return o, w
    return ptext(x, y, s, sc, color, shadow, anchor, extra), tw(s.upper(), sc)
