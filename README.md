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
