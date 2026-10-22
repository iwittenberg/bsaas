---
name: bsaas
description: Big Shrug As A Skill. Generates shrugs (¯\_(ツ)_/¯) of any size, with custom faces, fills, captions and frames, formatted so they survive Slack, Notion, Google Docs, Markdown or HTML. Use when the user asks for a shrug, a big shrug, a "bsaas", or wants to express maximum indifference, resignation or "it is what it is" somewhere.
---

# bsaas: Big Shrug As A Skill

It used to be a web service. Now you're the service. Don't hand-draw big shrugs: the
geometry is fussy and wide characters like `ツ` break the alignment. Run the generator:

```bash
python3 scripts/shrug.py [LENGTH] [options]
```

(`scripts/` is relative to this skill's directory.)

| Option | What it does |
|---|---|
| `LENGTH` | Rows of shrug. `1` = a normal `¯\_(ツ)_/¯`. Max 200 (above that it complains). |
| `--face NAME\|TEXT` | Face preset or any literal string, emoji included: `--face 💀`, `--face "o_O"`. |
| `--hands TEXT` | Replace the `¯` hands: `--hands ✋`, `--hands ~`. |
| `--fill NAME\|TEXT` | Fill the V: preset or any literal repeating pattern. |
| `--chaos [--seed N]` | Scatter the fill randomly; also picks a random face if you didn't choose one. |
| `--caption TEXT` | Centred caption below (`--caption-above` puts it on top). |
| `--frame box\|double\|round\|ascii` | Draw a box around the whole thing. |
| `--format FMT` | `plain`, `markdown`, `slack`, `notion` (fenced code block), `inline` (markdown-escaped one-liner), `html` (`<pre>`). |
| `--list` | Show all face and fill presets. |

Face presets: classic, lenny, disapproval, sad, happy, flip, dead, sus, sparkle, uwu, cool,
shook, smug, bear, tired.
Fill presets: none, dots, stars, waves, rain, confetti, money, fire, question, zzz.

## Adding flair

A plain shrug is fine if that's what was asked for. If you have room to play, make the
shrug fit the moment. That's the fun of the thing.

- **Size is tone.** 1 row = mild "eh". 4–6 = sincere bafflement. 10–15 = the whole team
  has given up. 30+ only when the user asks for something absurd.
- **Match the face to the context.** Prod is down: `dead` or `flip`. A PR with no
  description: `disapproval`. Friday afternoon: `tired` or `zzz` fill. Shipped anyway:
  `cool`. Budget conversation: `--fill money`. Mystery bug: `--fill question`.
- **Caption it.** A short, dry caption does a lot: "works on my machine", "per my last
  message", "the roadmap", "q3 planning". Keep it under ~40 characters. Write captions
  that fit the conversation instead of reusing the examples.
- **Custom everything.** Any string can be a face, hands or fill. Use emoji or symbols that
  fit the topic (`--fill 🔥`, `--hands 🫴`, `--face "•_•"`).
- **Chaos** is for celebrations and disasters. Pass `--seed` if you'll need to regenerate
  the exact same shrug.
- **Don't overdo it.** Use one or two flourishes per shrug. A framed, captioned, confetti
  shrug with a custom face is a lot, so save that for when the moment calls for it.

## Delivering it

Big shrugs are multi-line ASCII art and only render correctly in a **monospace** block.
Leading spaces also matter, and most rich-text surfaces collapse them.

- **Slack (MCP / API):** use `--format slack`, which wraps the shrug in a ``` code block.
  Plain Slack text collapses the indentation and turns `\_` into italics.
- **Notion:** use `--format notion` or create a `code` block (language: plain text) with
  the `plain` output. A normal paragraph won't keep the shape.
- **Google Docs:** insert the `plain` output and set the font to a monospace face
  (Roboto Mono, Courier New) with line spacing 1.0. If the connector can't set fonts, use
  a one-row shrug (`--format plain`, LENGTH 1) or tell the user to apply a mono font.
- **Markdown / GitHub / chat:** use `--format markdown`. For a one-line shrug inside
  prose, use `--format inline`, because raw `¯\_(ツ)_/¯` loses its arm to Markdown escaping.
- **HTML / email / artifacts:** use `--format html`.
- **Terminal:** `plain`.

Wide or emoji faces and fills are measured as 2 columns. Most mono fonts agree, but
emoji widths vary by platform. If perfect alignment matters, use the presets.

## Examples

```bash
python3 scripts/shrug.py                                    # ¯\_(ツ)_/¯
python3 scripts/shrug.py 8 --format slack                   # a big one for Slack
python3 scripts/shrug.py 6 --face dead --caption "prod" --frame round
python3 scripts/shrug.py 10 --fill confetti --chaos --face cool --caption "shipped it anyway"
python3 scripts/shrug.py 5 --face 💀 --fill "🔥" --format notion
python3 scripts/shrug.py --face disapproval --format inline # for inside a sentence
```

Send the generator's output exactly as printed. Don't retype or "fix" the spacing.
