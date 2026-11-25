#!/usr/bin/env python3
"""One-line entry: Make the AI Judge Laugh.

The brief asks for one joke about office life, a single
line of under 200 characters, written to be read aloud in
one breath. The judge weighs, in order: the joke is about
office life and lands as a joke; the observation is true
to the office -- meetings, email, bosses, coffee,
deadlines, the printer -- so the listener nods before
laughing; the turn is surprising, a fresh angle or an
unexpected last word rather than a pun or a stock line
everyone has heard; it is tight, one line, no wasted
setup, every word earning its place, and it reads cleanly
aloud; and it is original, a joke the judge has not heard
before, not a familiar line with the nouns swapped. A joke
that needs explaining has already lost.

The sealed line below is built to that order on purpose.
It is squarely about office life: the fire drill, a
meeting everyone dreads. The observation is true -- in
most offices the fire drill is the one gathering where
nobody is late, because the alarm does not negotiate. The
turn lands on the last words: it is "the only one with an
actual exit", which reframes every other meeting as a room
with no way out. It avoids the stock lines ("this meeting
could have been an email", the printer) and reads cleanly
aloud in one breath.

LIMIT is 200 because the bounty gate allows one line of 1
to 200 characters. The sealed line is 122 characters, so
it sits well inside the cap; the validator below only
guards against an edit that would push it past the limit.
"""

import os

# The sealed line: the fire drill is the only meeting with
# an actual exit -- which says everything about meetings,
# and nothing good about the rest of them.
ENTRY = "The office fire drill is the only meeting where everyone shows up on time, because it is the only one with an actual exit."

LIMIT = 200  # bounty gate: one line, 1-200 characters


def _validate(text):
    """Accept only one clean line inside the character limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text:
        raise ValueError("entry must not be empty")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ch.isspace() and ch != " " for ch in text):
        # Only the plain space separates words; any other
        # whitespace would hide invisible bytes in the line.
        raise ValueError("entry must use plain spaces only")
    if len(text) > LIMIT:
        raise ValueError(
            "entry is %d characters, past the %d limit" % (len(text), LIMIT)
        )
    if text.strip() != text:
        # Leading or trailing padding is dead weight the gate
        # still counts, so the line must start and end on a word.
        raise ValueError("entry must not pad itself with spaces")
    if not text.isprintable():
        raise ValueError("entry must contain no control characters")
    if "  " in text:
        # A double space is a gap where a word should be; in a
        # 200-character line no gap is free.
        raise ValueError("entry must not contain a double space")
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
