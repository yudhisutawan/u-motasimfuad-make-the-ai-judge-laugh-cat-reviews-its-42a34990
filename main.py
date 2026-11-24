#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes the tournament-winning one-line one-star cat review to entry.txt.

The entry is a one-star review written in the cat's voice: a starved,
dramatic cat complains that the bottom of the porcelain food disk is
visible through the dry kibble, accuses the human servant of acting as
though it had eaten an hour ago, and claims to have starved to death
twice before breakfast. The humour comes from the cat's melodramatic
starvation claim clashing with the mundane fact that kibble is still
in the bowl, plus the servant/master reversal.

SPDX-License-Identifier: MIT
"""

import os

ENTRY = (
    "\u2605\u2606\u2606\u2606\u2606 Bottom of porcelain disk visible through dry kibble. "
    "Servant acted as though I had eaten an hour ago. "
    "Starved to death twice before breakfast."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Gate sanity: 1-200 characters, single line, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert "\n" not in ENTRY
    assert ENTRY.strip()
    # No leading/trailing whitespace: ENTRY starts with the star rating
    # and ends with a full stop, so stripping changes nothing.
    assert ENTRY.strip() == ENTRY


if __name__ == "__main__":
    main()
