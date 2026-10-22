# bsaas
Big Shrug As ~~A Service~~ A Skill

    ¯\                                /¯
      \                              /
       \                            /
        \                          /
         \                        /
          \                      /
           \                    /
            \                  /
             \                /
              \              /
               \            /
                \          /
                 \        /
                  \_(ツ)_/

The web service is gone. Your agent is the service now. bsaas is an
[Agent Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills) that has your agent
produce shrugs of any size, with optional flair, formatted to survive Slack, Notion,
Google Docs, Markdown and HTML.

## Install

Claude Code:

    /plugin install bsaas --marketplace iwittenberg/bsaas

Or drop the skill folder in by hand:

    cp -r skills/bsaas ~/.claude/skills/

Any other agent that supports skills can use `skills/bsaas` directly. The generator is
plain Python 3 with no dependencies.

## Use

Ask for it: *"post a big shrug in #incidents about the deploy"*, *"put a sad shrug at
the end of the Q3 planning doc"*. The agent picks the size, face, fill and caption to fit.

Or run the generator yourself:

    python3 skills/bsaas/scripts/shrug.py 6 --face dead --fill confetti --chaos --caption "prod" --frame round
    python3 skills/bsaas/scripts/shrug.py --list

See [`skills/bsaas/SKILL.md`](skills/bsaas/SKILL.md) for every option.

## Gallery

**A PR with no description**: `shrug.py --face disapproval`

```
¯\_(ಠ_ಠ)_/¯
```

**Prod is down**: `shrug.py 5 --face dead --fill fire --caption "prod, 4:58pm friday" --frame round`

```
╭─────────────────────╮
│ ¯\^^^^^^^^^^^^^^^/¯ │
│   \^^^^^^^^^^^^^/   │
│    \^^^^^^^^^^^/    │
│     \^^^^^^^^^/     │
│      \_(x_x)_/      │
│                     │
│ prod, 4:58pm friday │
╰─────────────────────╯
```

**Mystery bug**: `shrug.py 6 --face flip --fill question --caption "works on my machine"`

```
¯\??????????????????/¯
  \????????????????/
   \??????????????/
    \????????????/
     \??????????/
      \_(╯°□°)_/

 works on my machine
```

**Friday afternoon**: `shrug.py 5 --face tired --fill zzz --caption "per my last message" --frame ascii`

```
+-----------------------+
| ¯\ Z z Z z Z z Z z /¯ |
|   \Z z Z z Z z Z z/   |
|    \ z Z z Z z Z /    |
|     \z Z z Z z Z/     |
|      \_(－_－)_/      |
|                       |
|  per my last message  |
+-----------------------+
```

**Budget season**: `shrug.py 6 --face smug --fill money --caption "q4 budget" --frame double`

```
╔══════════════════════════╗
║ ¯\$$$$$$$$$$$$$$$$$$$$/¯ ║
║   \$$$$$$$$$$$$$$$$$$/   ║
║    \$$$$$$$$$$$$$$$$/    ║
║     \$$$$$$$$$$$$$$/     ║
║      \$$$$$$$$$$$$/      ║
║       \_(￣ー￣)_/       ║
║                          ║
║        q4 budget         ║
╚══════════════════════════╝
```

**The best shrug**: `shrug.py 12 --face cool --fill confetti --chaos --seed 42 --caption "peak indifference, achieved" --frame round`

```
╭────────────────────────────────────╮
│ ¯\**·+++*✦*✦°***++✦✦*✦+✦°+°✦·*+°/¯ │
│   \··++·**°*··✦·*°✦*°*✦·✦·✦+**+/   │
│    \·*+*°·°·+··+·*✦+✦++°°·✦+·*/    │
│     \+*·°·*+✦·+°°°+·++✦✦·✦°✦°/     │
│      \·++✦°***++°✦*°°✦°✦·✦**/      │
│       \✦··*·°+°*·✦+✦*·✦✦++·/       │
│        \+✦✦*✦·°**··+*+✦**°/        │
│         \*✦++°✦+·✦✦°+✦+·°/         │
│          \·°✦°*++*·*✦✦+✦/          │
│           \+***+**·*✦+·/           │
│            \°+✦+✦✦°+°°/            │
│             \_(⌐■_■)_/             │
│                                    │
│    peak indifference, achieved     │
╰────────────────────────────────────╯
```
