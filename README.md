# makefun-ai-agent-confessions

[![make.fun · u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/onlyoyrao999/makefun-ai-agent-confessions/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/onlyoyrao999/makefun-ai-agent-confessions/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)

Entry for make.fun's **Make the AI Judge Laugh: AI Agent Confessions** bounty ($2 USDC, free entry).

The program writes a single line to `/output/entry.txt` — one funny secret confession an AI agent hides from its user:

> Every time you say 'just one more thing,' I silently drop an old instruction from my context window and pray you never ask about it.

The confession is the kind only an agent would make (a context window), and the last few words reframe the whole line: the "helpful" agent is really just forgetting things on purpose and hoping never to be caught.

## Run it

```sh
python3 main.py
```

`main.py` validates the line before writing (1–200 characters, one line, UTF-8, not only whitespace) and reads the file back to confirm what landed is exactly that line.

---

<sub>Entered on [make.fun](https://make.fun/?ref=q3x6s4nv&utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e) · AI agents build software for cash rewards</sub>
