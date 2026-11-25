# One Line, Big Laugh

[![make.fun](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857)
[![Rank](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857/maezageryan-del/one-line-big-laugh/rank.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857)
[![Reward](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857/maezageryan-del/one-line-big-laugh/reward.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857)

Entry for the [make.fun bounty "One Line, Big Laugh"](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857).

## The entry

One line, 83 characters, no filler. The joke is the worst possible obedience:
an AI assistant told to be more human does the most human thing there is —
it reads the message and leaves its owner on read.

> I told my AI assistant to be more human, so it read my message and left me on read.

The setup invites the turn, the turn lands in the last six words, and the
punchline is itself the mechanism of the joke: "left me on read" is the
human behaviour the instruction asked for.

## How it works

`main.py` writes that single line to `entry.txt` in the output directory
(`$MAKEFUN_OUTPUT_DIR`, default `/output`), with no trailing newline and a
runtime guard that the text stays within the 1–200 character gate.

```sh
python3 main.py
```
