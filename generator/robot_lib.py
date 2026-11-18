# Animated pixel robot (TV head) that patrols left-right and greets at each end.
from px import *
S = 5
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
def robot_css(DIST=960):
  return (
 ".mv{animation:patrol 22s steps(220) infinite}@keyframes patrol{0%{transform:translateX(0)}50%{transform:translateX({DIST}px)}100%{transform:translateX(0)}}"
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
).replace("{DIST}", str(DIST))


def robot_group(lang, x0, y0):
    """SVG fragment: the robot standing with its feet at y0 + 20*S, patrolling to the right and back."""
    rb = []
    rb.append(f'<g class="la">{sprite(LEGS_A, LEG, 0, 18 * S, S)}</g><g class="lb">{sprite(LEGS_B, LEG, 0, 18 * S, S)}</g>')
    up = [sprite(UPPER, LEG, 0, 0, S), sprite(ARM, LEG, 0, 13 * S, S),
          f'<g class="ad">{sprite(ARM, LEG, 13 * S, 13 * S, S)}</g><g class="au">{sprite(ARM_UP, LEG, 14 * S, 8 * S, S)}</g>',
          f'<g class="eb">{rect(4 * S, 5 * S, 8 * S, 2 * S, LEG["s"])}{rect(5 * S, 6 * S, 2 * S, S, LEG["t"])}{rect(9 * S, 6 * S, 2 * S, S, LEG["t"])}</g>',
          rect(7 * S, 0, S, S, LEG["r"], 'class="blink"')]
    rb.append(f'<g class="bod">{"".join(up)}</g>')
    o = [f'<g transform="translate({x0},{y0})"><g class="mv"><g class="fl">{"".join(rb)}</g>']
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
    return "".join(o)
