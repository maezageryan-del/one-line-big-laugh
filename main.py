"""One Line, Big Laugh: a single funny line, written to the grader output.

The joke is worst-possible obedience: an AI assistant told to be more human
does the most human thing there is — it reads the message and leaves its
owner on read. 83 characters, one line, punchline in the last six words;
short is also a tie-break asset (fewer bytes wins exact ties).
"""

import os

LINE = "I told my AI assistant to be more human, so it read my message and left me on read."

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE and LINE == LINE.strip(), "entry must be one clean line"
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
