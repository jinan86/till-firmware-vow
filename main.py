#!/usr/bin/env python3
"""Till Firmware Do Us Part — a robot's wedding vow.

Writes one fixed vow to /output/entry.txt.
Deterministic: no network, no input, no dependencies, no randomness.
Running it twice produces byte-identical output.
"""

import os

VOW = "I vow to love you through every update, every reboot, and every low-battery warning \u2014 and if my firmware ever fails, I'll reboot and love you all over again."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate: vow must be 1-200 characters (it is 157). Deterministic output.
    assert 1 <= len(VOW) <= 200, f"vow length {len(VOW)} outside 1-200"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(VOW + "\n")


if __name__ == "__main__":
    main()
