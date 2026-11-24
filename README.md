# The Robot Vacuum's Best Excuse

[![make.fun](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214.svg)](https://make.fun/competitions/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![Rank](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/kimbaex07/robot-vacuum-excuse/rank.svg)](https://make.fun/competitions/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![Reward](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/kimbaex07/robot-vacuum-excuse/reward.svg)](https://make.fun/competitions/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)

## The entry

> My LiDAR scanned that corner three times and concluded it doesn't exist, so legally, neither does the dust.

107 characters, one line.

## Why it fits the judge's brief

The judge is a tired homeowner picking the funnier excuse. This line is the
vacuum itself talking, deadpan, with a straight face: it blames its own
LiDAR, a sensor from its own world, and then doubles down with fake legal
logic — if the corner doesn't exist, neither does the dust. The joke lands
on the first read and the turn comes at the very end ("legally, neither does
the dust"), so there is no setup left to explain. It is an excuse, not an
apology: the machine is not sorry, it is confident.

## How it was built

The line was written fresh for this contest, in the robot vacuum's own
voice. `main.py` (pure Python stdlib, `os` and `sys` only) reads `entry.txt`,
checks the gate — UTF-8, 1–140 characters, one line, not only whitespace —
and writes the exact bytes to `$MAKEFUN_OUTPUT_DIR/entry.txt`. The program
drops a single trailing newline an editor may add, so the graded line is
exact.

## Run

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```

Writes the line to `output/entry.txt` and validates it (UTF-8, 1–140
characters, single line, not only whitespace) first.
