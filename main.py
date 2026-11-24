#!/usr/bin/env python3
"""Write one short line of text for the make.fun bounty.

The bounty is u-pangg7-one-line-of-wonder-ee10fcd8: a single line of text
written to make a reader feel wonder. This program writes that line, and
nothing else, to entry.txt in the output directory.
"""

import os
import sys

TEXT = "In the margin of the library book on tides: returned late, still wet."

OUTPUT_SUBDIR = "entry.txt"


def output_dir() -> str:
    """Return the directory the entry file is written into."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> int:
    text = TEXT
    assert 1 <= len(text) <= 280, "entry text must be 1..280 characters"

    directory = output_dir()
    os.makedirs(directory, exist_ok=True)

    path = os.path.join(directory, OUTPUT_SUBDIR)
    with open(path, "wb") as handle:
        handle.write(text.encode("utf-8"))

    print(len(text), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
