#!/usr/bin/env python3
"""One Word for the Boss — "Teflon".

The word: Teflon. Nothing ever sticks to the boss — every missed
deadline, every bad call, every blame slides right off, while the
team scrubs the pan. One word, six letters, funny on its own, true
about bosses everywhere, and fresh: nobody's first reach is a
non-stick coating, but everybody recognises it the moment they hear it.
"""

import os

WORD = "Teflon"


def verify_output() -> None:
    with open("/output/entry.txt", "rb") as f:
        data = f.read()
    assert data == WORD.encode("utf-8"), f"mismatch: {data!r}"
    print(f"verified {len(data)} bytes, byte-identical")


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    print(f"wrote {len(WORD)} chars to /output/entry.txt")
    verify_output()


if __name__ == "__main__":
    main()
