#!/usr/bin/env python3
"""One Line of Earned Pride.

Writes a single line of text to /output/entry.txt.
"""
import os

LINE = "At seventy-two, after four failed tests, she parked her late husband's truck perfectly between two battered vans, cut the engine, and sat a while with her hands still on the wheel."

def main():
    # Guard: the gate requires 1-240 characters of UTF-8 text, one line.
    assert "\n" not in LINE and 1 <= len(LINE) <= 240, len(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
