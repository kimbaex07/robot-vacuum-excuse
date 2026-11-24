"""The Robot Vacuum's Best Excuse — make.fun competition entry.

Writes one funny one-line excuse from a robot vacuum for missing a spot
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

One trailing newline (and a trailing carriage return) that a text editor
may have appended to entry.txt is dropped before validation, so the graded
line is exact.

Competition: u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214
"""

import os
import sys

MAX_CHARS = 140


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.txt")
    with open(src, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    # Normalization: an editor (e.g. GitHub's web editor) may append a
    # single trailing newline. Drop at most one trailing "\n", then at most
    # one trailing "\r", before validating; the graded line is the result.
    if text.endswith("\n"):
        text = text[:-1]
    if text.endswith("\r"):
        text = text[:-1]
    if not (1 <= len(text) <= MAX_CHARS):
        sys.exit("entry must be 1-%d chars, got %d" % (MAX_CHARS, len(text)))
    if not text.strip():
        sys.exit("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        sys.exit("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "wb") as f:
        f.write(text.encode("utf-8"))
    os.chmod(out_path, 0o644)
    print("wrote %s (%d chars)" % (out_path, len(text)))


if __name__ == "__main__":
    main()
