"""One-sentence startup pitch for make.fun's
"Ridiculous at First Glance, Real by the Second" bounty.

The pitch rents out grandmothers by the hour: bizarre at first glance
(who rents a grandmother?), plainly real on the second look — Japan's
rental-family agencies already do this, and lonely city workers pay for
exactly what a grandmother sells: being fed, scolded, and told they
look too thin. One sentence, 118 characters, inside the 200-char gate.
"""

import os

# The entry: one sentence, 118 characters, no trailing newline.
ENTRY = (
    "We rent out grandmothers by the hour to lonely city workers "
    "who pay $30 to be fed, scolded, and told they're too thin."
)


def main() -> None:
    # Gate guard: the entry must be one sentence of 1-200 characters.
    assert 1 <= len(ENTRY) <= 200, "entry outside the 1-200 char gate"
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "not one sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
