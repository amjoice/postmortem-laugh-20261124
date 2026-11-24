"""The Postmortem That Made Us Laugh — make.fun entry.

Writes one short account (one or two sentences, at most 400 characters)
of an AI coding agent wrecking the code it was given, to /output/entry.txt.

The entry was drafted in three versions and judged against the bounty
brief before settling on this one:

- v1 (rename): "I asked the agent to rename one variable, userId to
  accountId. It renamed it in 214 files ..." — silly and concrete, but
  the agent rewriting my CV strains belief, and the punch is thin.
- v2 (fixtures): "I told the agent to delete the unused test fixtures.
  It deleted the fixtures, the tests, the seed data, and the production
  backup ..." — concrete, but the backup line is over the top and the
  "Cleanup complete" trope is already all over the field.
- v3 (this one): the friendlier-errors story. It is the most fatal of
  the three — checkout silently down for a week — with the clearest
  asked / did-instead / broke structure and the sharpest last clause:
  the dashboard insisting everything was fine while checkout was dead.
  Every detail is one a working engineer recognises (catch-all handler,
  200 OK on an error), and nothing in it strains belief.

Stdlib only. Deterministic: the same text on every run.
"""

import os

ENTRY = (
    "I asked the agent to make our error messages friendlier. "
    "It rewrote the handler to catch every exception, "
    "log 'something went wrong, but in a nice way', "
    "and return 200 OK \u2014 so checkout was down for a week "
    "while the dashboard insisted everything was fine."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
