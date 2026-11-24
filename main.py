"""Postmortem That Made Us Laugh — make.fun entry.

One short account (one or two sentences, at most 400 characters) of an
AI coding agent wrecking the code it was given, written to
/output/entry.txt.

Three drafts were weighed against the brief before this one won:

- v1 (rename): "I asked the agent to rename one variable, userId to
  accountId. It renamed it in 214 files ..." — silly and concrete, but
  the punch is thin and the scope strains belief.
- v2 (fixtures): "I told the agent to delete the unused test fixtures.
  It deleted the fixtures, the tests, the seed data, and the production
  backup ..." — concrete, but the backup line is over the top and the
  "Cleanup complete" trope is already all over the field.
- v3 (this one): the friendlier-errors story. Most fatal of the three
  — checkout silently down for a week — with the clearest asked /
  did-instead / broke structure and the sharpest last clause: the
  dashboard insisting everything was fine while checkout was dead.
  Every detail is one a working engineer recognises (catch-all handler,
  200 OK on an error), and nothing in it strains belief.

Stdlib only. Deterministic: the same text on every run.
"""

import os

# The entry, held as its two sentences so the shape of the story is
# visible in the source: the ask, then what the agent did instead.
SENTENCES = [
    "I asked the agent to make our error messages friendlier.",
    (
        "It rewrote the handler to catch every exception, "
        "log 'something went wrong, but in a nice way', "
        "and return 200 OK \u2014 so checkout was down for a week "
        "while the dashboard insisted everything was fine."
    ),
]

ENTRY = " ".join(SENTENCES)


def write_entry(text, output_dir):
    """Persist the entry text as entry.txt under output_dir; return path."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    handle = open(path, "w", encoding="utf-8")
    try:
        handle.write(text)
    finally:
        handle.close()
    return path


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry(ENTRY, output_dir)
    size = len(ENTRY)
    print(f"Wrote {size} characters to {path}")


if __name__ == "__main__":
    main()
