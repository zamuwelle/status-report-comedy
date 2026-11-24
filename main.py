"""Render the agent's weekly status update."""

from os import environ
from pathlib import Path

REPORT = (
    "Weekly update: I gave each retry in the infinite loop its own ticket, "
    "so we can finally report infinite throughput."
)


def emit(destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    (destination / "entry.txt").write_bytes(REPORT.encode("utf-8"))


if __name__ == "__main__":
    emit(Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output")))
