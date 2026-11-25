#!/usr/bin/env python3
"""Write one loading-screen tip to /output/entry.txt.

Standard library only. The tip is a single line, well under 200
characters, aimed at stressed developers and AI coding agents.
"""

import os

ENTRY = (
    "Tip: your AI already 'fixed' this bug twice. "
    "Now you're both just watching the loading bar lie about being 99% done."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
