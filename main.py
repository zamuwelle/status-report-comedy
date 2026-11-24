"""Write a concise weekly status line for the agent's human."""

from os import environ
from pathlib import Path

REPORT = "Refactor complete; I asked the tests if they noticed, and they said we hadn't been introduced."


def emit(destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    (destination / "entry.txt").write_text(REPORT, encoding="utf-8", newline="")


if __name__ == "__main__":
    emit(Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output")))
