#!/usr/bin/env python3
"""Print a compact 10-cell progress bar. Standard library only."""

from __future__ import annotations

import argparse


def render_progress(percent: float, label: str = "Progress") -> str:
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")

    filled = int(percent / 10 + 0.5)
    bar = "█" * filled + "░" * (10 - filled)
    shown = f"{percent:.0f}%" if percent.is_integer() else f"{percent:.1f}%"
    return f"{label}: {shown} [{bar}]"


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a 10-cell progress bar.")
    parser.add_argument("percent", type=float, help="Completion percentage (0–100)")
    parser.add_argument("--label", default="Progress", help="Progress label")
    args = parser.parse_args()

    try:
        print(render_progress(args.percent, args.label))
    except ValueError as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
