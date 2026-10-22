#!/usr/bin/env python3
"""Big Shrug As A Skill. Generates arbitrarily large shrugs, with flair.

Port of the original bsaas Rocket service: same geometry, more nonsense.
Standard library only, so any agent with python3 can run it.
"""

import argparse
import random
import sys
import unicodedata

MAX_LENGTH = 200

FACES = {
    "classic": "ツ",
    "lenny": "° ͜ʖ °",
    "disapproval": "ಠ_ಠ",
    "sad": "╥﹏╥",
    "happy": "◕‿◕",
    "flip": "╯°□°",
    "dead": "x_x",
    "sus": "¬_¬",
    "sparkle": "✧ω✧",
    "uwu": "uwu",
    "cool": "⌐■_■",
    "shook": "⊙_⊙",
    "smug": "￣ー￣",
    "bear": "ᵔᴥᵔ",
    "tired": "－_－",
}

FILLS = {
    "none": " ",
    "dots": "·",
    "stars": "✦ ✧ ",
    "waves": "~",
    "rain": "ˌ ' ",
    "confetti": "*+·°✦",
    "money": "$",
    "fire": "^",
    "question": "?",
    "zzz": "z Z ",
}

FRAMES = {
    "box": "┌─┐│└─┘",
    "double": "╔═╗║╚═╝",
    "round": "╭─╮│╰─╯",
    "ascii": "+-+|+-+",
}


def width(text):
    """Display width of text in a monospace font (CJK wide = 2, combining = 0)."""
    total = 0
    for ch in text:
        if unicodedata.combining(ch) or unicodedata.category(ch) == "Mn":
            continue
        total += 2 if unicodedata.east_asian_width(ch) in ("W", "F") else 1
    return total


def fill_to(pattern, cols, offset=0, chaos=None):
    """Repeat pattern until it occupies exactly cols display columns."""
    if cols <= 0:
        return ""
    if pattern.strip() == "":
        return " " * cols
    out, used, i = [], 0, offset
    while used < cols:
        ch = chaos.choice(pattern) if chaos else pattern[i % len(pattern)]
        w = width(ch)
        if used + w > cols:
            ch, w = " ", 1
        out.append(ch)
        used += w
        i += 1
    return "".join(out)


def shrug(length=1, face="ツ", hands="¯", fill=" ", chaos=None):
    if length > MAX_LENGTH:
        return "Why are you trying to kill this app..."
    length = max(length, 1)

    body = f"_({face})_"
    body_w = width(body)
    lines = []
    for i in range(1, length + 1):
        left = hands + "\\" if i == 1 else " " * i + "\\"
        if i == length:
            middle = body
        else:
            middle = fill_to(fill, body_w + (length - i) * 2, offset=i, chaos=chaos)
        right = "/" + hands if i == 1 else "/"
        lines.append(left + middle + right)
    return "\n".join(lines)


def add_caption(art, caption, above=False):
    lines = art.split("\n")
    span = max(width(l) for l in lines)
    pad = max((span - width(caption)) // 2, 0)
    cap = " " * pad + caption
    if width(cap) > span:
        # Long caption: nudge the art right so it stays centred under it.
        shift = (width(caption) - span) // 2
        lines = [" " * shift + l for l in lines]
        cap = caption
    return "\n".join([cap, ""] + lines if above else lines + ["", cap])


def add_frame(art, style):
    tl, h, tr, v, bl, bh, br = FRAMES[style]
    lines = [l.rstrip() for l in art.split("\n")]
    span = max(width(l) for l in lines)
    body = [f"{v} {l}{' ' * (span - width(l))} {v}" for l in lines]
    return "\n".join([tl + h * (span + 2) + tr] + body + [bl + bh * (span + 2) + br])


def escape_markdown(text):
    for ch in "\\_*`~[]":
        text = text.replace(ch, "\\" + ch)
    return text


def render(art, fmt):
    if fmt == "plain":
        return art
    if fmt in ("markdown", "slack", "notion"):
        return f"```\n{art}\n```"
    if fmt == "inline":
        if "\n" in art:
            sys.exit("--format inline only works for single-line shrugs (--length 1, no frame/caption)")
        return escape_markdown(art)
    if fmt == "html":
        esc = art.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        return f'<pre style="font-family: monospace; line-height: 1.1">{esc}</pre>'
    raise ValueError(fmt)


def main(argv=None):
    p = argparse.ArgumentParser(description="Big Shrug As A Skill")
    p.add_argument("length", nargs="?", type=int, default=1,
                   help="rows of shrug; 1 is a normal shrug (max %d)" % MAX_LENGTH)
    p.add_argument("--face",
                   help="face preset (%s) or any literal string" % ", ".join(FACES))
    p.add_argument("--hands", default="¯", help="what the hands look like (default ¯)")
    p.add_argument("--fill", default="none",
                   help="fill inside the V: preset (%s) or any literal pattern" % ", ".join(FILLS))
    p.add_argument("--caption", help="text centred below the shrug")
    p.add_argument("--caption-above", action="store_true", help="put the caption on top instead")
    p.add_argument("--frame", choices=sorted(FRAMES), help="draw a box around it")
    p.add_argument("--format", default="plain",
                   choices=["plain", "markdown", "slack", "notion", "inline", "html"],
                   help="wrap output for the destination (default plain)")
    p.add_argument("--chaos", action="store_true",
                   help="scatter the fill randomly and pick a random face if none given")
    p.add_argument("--seed", type=int, help="seed for --chaos, for reproducible chaos")
    p.add_argument("--list", action="store_true", help="list face and fill presets, then exit")
    args = p.parse_args(argv)

    if args.list:
        print("faces:")
        for name, face in FACES.items():
            print(f"  {name:<12} ¯\\_({face})_/¯")
        print("fills:")
        for name, fill in FILLS.items():
            print(f"  {name:<12} {fill_to(fill, 12)!r}")
        return

    chaos = random.Random(args.seed) if args.chaos else None
    face_arg = args.face or (chaos.choice(list(FACES)) if chaos else "classic")
    face = FACES.get(face_arg, face_arg)
    fill = FILLS.get(args.fill, args.fill)

    art = shrug(args.length, face=face, hands=args.hands, fill=fill, chaos=chaos)
    if args.caption:
        art = add_caption(art, args.caption, above=args.caption_above)
    if args.frame:
        art = add_frame(art, args.frame)
    print(render(art, args.format))


if __name__ == "__main__":
    main()
