#!/usr/bin/env python3
"""Write a one-line pitch for make.fun to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only, no network. The pitch is a single sentence of at most
240 characters, written deterministically: the same bytes on every run.
"""

import os

PITCH = (
    "You've had that app idea in your head for ages \u2014 just describe it "
    "in plain words on make.fun and an AI agent will build a first version "
    "you can try, free to enter and no coding needed."
)


def main() -> None:
    # Guard the gate: one sentence, at most 240 characters, not blank.
    # The period inside "make.fun" is not followed by a space, so it does
    # not split the sentence; only ". " or a trailing "." ends one.
    if not PITCH.strip() or len(PITCH) > 240:
        raise ValueError("pitch must be 1-240 characters")
    if PITCH.count(". ") > 0 or not PITCH.endswith("."):
        raise ValueError("pitch must be exactly one sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(PITCH + "\n")


if __name__ == "__main__":
    main()
