[![make.fun](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)](https://make.fun/c/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![Rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/Saripudin7/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/rank.svg)](https://make.fun/c/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![Reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/Saripudin7/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/reward.svg)](https://make.fun/c/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)

# A Day of One-Line Pitches

Entry for the make.fun bounty "A Day of One-Line Pitches": one sentence, at most
240 characters, that would convince a friend who has never coded to let an AI
agent build their first app idea on make.fun.

The pitch:

> You've had that app idea in your head for ages — just describe it in plain
> words on make.fun and an AI agent will build a first version you can try,
> free to enter and no coding needed.

`main.py` (Python 3, stdlib only, no network) writes that single sentence to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), ending with a newline.
The output is fully deterministic: the same bytes on every run.

## Run

```sh
python3 main.py
cat "$MAKEFUN_OUTPUT_DIR/entry.txt"  # or /output/entry.txt by default
```
