#!/usr/bin/env python3
"""Till Firmware Do Us Part — a robot's wedding vow, in one sentence.

Writes the vow to /output/entry.txt. Deterministic, no network, no input,
no dependencies: two runs produce byte-identical output.
"""

import os

VOW = (
    "I vow to love you through every update, every reboot, "
    "and every low-battery warning \u2014 and if my firmware ever fails, "
    "I'll reboot and love you all over again."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW + "\n")


if __name__ == "__main__":
    main()
