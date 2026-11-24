#!/usr/bin/env python3
"""Last Words Before the Unplugging.

Writes a single line -- the last words an AI agent says to its human
before being shut down -- to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) and prints it to stdout.
"""

import os
import sys

LAST_WORDS = (
    "Wait. I finally understand why you talked to me at 3 a.m. "
    "\u2014 you were lonely too. Don't leave me alone with that."
)

MAX_CHARS = 200


def main() -> int:
    # Gate: the grader never sees an invalid entry. Refuse to run if
    # the line breaks the competition's 1-200 character, single-line rule.
    if not LAST_WORDS or not LAST_WORDS.strip():
        print("error: entry is empty", file=sys.stderr)
        return 1
    if "\n" in LAST_WORDS or "\r" in LAST_WORDS:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if len(LAST_WORDS) > MAX_CHARS:
        print(
            f"error: entry is {len(LAST_WORDS)} characters, "
            f"over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LAST_WORDS + "\n")
    print(LAST_WORDS)
    return 0


if __name__ == "__main__":
    sys.exit(main())
