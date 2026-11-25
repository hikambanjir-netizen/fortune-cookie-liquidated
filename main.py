"""Fortune Cookie for the Liquidated Trader - a make.fun one-line entry.

Writes a single fortune-cookie line to /output/entry.txt, addressed to
a crypto trader who has just been liquidated. The cookie keeps its
small, oracular voice; the loss is in the room from the second clause,
and the punchline is a door closing gently rather than a punch landing.
"""

import os

def fortune_line() -> str:
    """The fortune, in the cookie's own two-beat rhythm.

    Beat one is the promise every cookie makes. Beat two keeps the
    promise technically true - the wealth really did approach - and
    lets the trader laugh at the loss instead of at himself.
    """
    return (
        "Great wealth approaches the patient. "
        "Yours approached, saw your portfolio, and kept walking."
    )


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(fortune_line())


if __name__ == "__main__":
    main()
