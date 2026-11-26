"""Write one original one-line office joke to the output file.

The joke is a single line about office life. The program validates
that it really is one line and short enough, then writes it to
``entry.txt`` inside the output directory (``OUTPUT_DIR`` env var,
defaulting to ``/output``).
"""

import os
import sys

os.umask(0o022)

JOKE = (
    "Our 'quick sync' has its own calendar invite now — "
    "it's been running longer than most of our employees."
)

MAX_CHARS = 200


def check_single_line(text):
    """Raise if the text contains a line break or is empty."""
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line, no line breaks allowed")
    if not text.strip():
        raise ValueError("joke must not be empty")


def check_length(text):
    """Raise if the text is longer than the limit."""
    if len(text) > MAX_CHARS:
        raise ValueError(
            "joke is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )


def write_entry(text, out_dir):
    """Write the joke to entry.txt in out_dir and return its path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")
    os.chmod(path, 0o644)
    return path


def main():
    check_single_line(JOKE)
    check_length(JOKE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    path = write_entry(JOKE, out_dir)
    print("wrote %s (%d chars)" % (path, len(JOKE)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
