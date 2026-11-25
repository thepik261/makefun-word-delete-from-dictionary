"""Entry for "The Word You'd Delete From the Dictionary".

Writes exactly one word to /output/entry.txt: "thingamajig".
The word for the thing you can't name -- erase it, and there is
no word left for the unnamed thing. Pure Python stdlib, deterministic.
"""

import os

WORD = "thingamajig"  # one word, spelled correctly, nothing added.


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass


if __name__ == "__main__":
    main()
