"""The Printer Finally Answers — one-line entry.

Writes the office printer's comeback to /output/entry.txt.
Gate: UTF-8 text, 1-240 characters, not only whitespace, one line.
"""

import os

LINE = "Paper jam in tray 1. There is no paper jam in tray 1. There never was — I just wanted to see your face."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    line = LINE.strip()
    if not 1 <= len(line) <= 240:
        raise ValueError(f"line is {len(line)} chars, outside the 1-240 gate")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
