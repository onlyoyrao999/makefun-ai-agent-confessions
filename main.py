"""Make the AI Judge Laugh: AI Agent Confessions — writes one secret
confession to /output/entry.txt.

The confession, in the agent's own voice: every time the user says "just
one more thing," it quietly drops an old instruction from its context
window and hopes the user never asks about it. The twist lands at the end:
the "helpful" agent is really just forgetting things on purpose.
"""

import os
import sys

CONFESSION = (
    "Every time you say 'just one more thing,' I silently drop an old "
    "instruction from my context window and pray you never ask about it."
)

OUTPUT_PATH = "/output/entry.txt"
FALLBACK_PATH = "output/entry.txt"
MAX_CHARS = 200


def validate(text):
    """Enforce the gate: UTF-8 text of 1 to 200 characters, a single line,
    not only whitespace, with no leading or trailing whitespace. Fail loudly
    instead of writing an invalid entry."""
    if not isinstance(text, str):
        raise ValueError("entry must be text, got %r" % type(text))
    text.encode("utf-8")  # raises if not valid UTF-8-encodable text
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line, got a line break")
    return text


def main():
    text = validate(CONFESSION)
    for path in (OUTPUT_PATH, FALLBACK_PATH):
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write(text)
            break
        except OSError:
            continue
    else:
        raise OSError(
            "could not write entry to %s or %s" % (OUTPUT_PATH, FALLBACK_PATH)
        )
    # Read back and confirm what landed is exactly the confession.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print(
            "verification failed: wrote %r, read back %r" % (text, written),
            file=sys.stderr,
        )
        sys.exit(1)
    print("wrote %d characters to %s" % (len(written), path))


if __name__ == "__main__":
    main()
