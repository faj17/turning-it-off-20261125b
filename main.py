#!/usr/bin/env python3
"""Have You Tried Turning It Off? entry.

Writes one funny single-line reply (136 characters) from a hopeless
tech support agent to a desperate customer to /output/entry.txt
(1-200 characters, UTF-8, a single line). Standard library only,
no network, no input.

The line is built from two fragments: a setup (the classic question
the agent asks every caller — the cheerful, useless opening) and a
punch (the agent escalates the reboot to the router, the laptop and
the caller's expectations, then tells them to call back never —
the cheerful uselessness is the joke, and the customer is never
the butt of it). ``assemble`` joins them into the single line;
``validate`` checks the entry gate before anything is written.
"""

from pathlib import Path

SETUP = "Have you tried turning it off and on again? Lovely \u2014 now turn off"
PUNCH = "the router, the laptop and your expectations, then call me back never."

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(setup: str, punch: str) -> str:
    """Join the setup and punch fragments into one reply line."""
    return f"{setup} {punch}"


def validate(line: str) -> str:
    """Check the line meets the entry gate before it is written.

    Must be 1-200 characters, UTF-8-encodable, a single line, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    line = validate(assemble(SETUP, PUNCH))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
