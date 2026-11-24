"""One Emoji, One Dream Vacation.

The entry is exactly one emoji: a palm tree (U+1F334).
It stands in for a tropical island dream vacation — warm sun,
a quiet beach, and nowhere else to be.

The emoji is a single code point with no variation selector,
so the entry file holds exactly one character and nothing else:
no words, no newline, no extra whitespace.
"""

import os
from pathlib import Path

EMOJI = "\U0001F334"


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(EMOJI, encoding="utf-8")


if __name__ == "__main__":
    main()
