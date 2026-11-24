import os
from pathlib import Path

LINE = (
    "You told me to give your work my full consideration. "
    "So I gave it my full consideration, then my full mouth, "
    "then my full stomach. Thorough, like you taught me."
)


def main() -> None:
    assert LINE == LINE.strip()
    assert "\n" not in LINE and "\r" not in LINE
    assert 1 <= len(LINE) <= 200
    assert LINE.strip()

    out = Path(os.environ.get("EXCUSE_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
