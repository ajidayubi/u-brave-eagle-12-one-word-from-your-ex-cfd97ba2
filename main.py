#!/usr/bin/env python3
"""One Word From Your Ex: write exactly one word to entry.txt.

The word is "Audition" -- the word an ex would use to describe you:
the whole relationship was just an audition for the real one.
One word, no trailing newline, deterministic, no network, no input.
"""

import os
from pathlib import Path

WORD = "Audition"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    Path(out_dir, "entry.txt").write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
