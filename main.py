#!/usr/bin/env python3
"""Entry for make.fun: Green Tests, Nothing Works (u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc).

Writes the one-line excuse to /output/entry.txt (MAKEFUN_OUTPUT_DIR).
"""
import os

ENTRY = "The suite is green: 4,021 tests, zero of them ever touched the button users actually click."
# Gate: /output/entry.txt must be UTF-8, 1-140 chars, single line, non-whitespace.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert "\n" not in ENTRY.strip(), "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
