"""One Word From Your Ex.

Writes exactly one word -- the word an ex would use to describe me --
to /output/entry.txt, with no trailing newline.

The word: Unbothered.
"""

import os

WORD = "Unbothered"


def main() -> None:
    word = WORD

    # Gate: exactly one word, 1-24 characters, no whitespace at all.
    # The gate is checked before anything is written, so a bad word
    # can never produce a bad entry file.
    assert isinstance(word, str)
    assert 1 <= len(word) <= 24, f"word length {len(word)} out of range"
    assert word == word.strip(), "word has leading/trailing whitespace"
    assert not any(ch.isspace() for ch in word), "word contains whitespace"
    assert len(word.split()) == 1, "must be exactly one word"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
