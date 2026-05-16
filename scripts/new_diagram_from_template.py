#!/usr/bin/env python3
"""Create a standalone neural-network dynamic-diagram HTML file from template."""

from __future__ import annotations

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", help="Output HTML path")
    parser.add_argument("--title", default="Neural Network Dynamic Diagram")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite output if it already exists",
    )
    args = parser.parse_args()

    skill_dir = Path(__file__).resolve().parents[1]
    template = skill_dir / "assets" / "html-template" / "index.html"
    output = Path(args.output).expanduser().resolve()

    if output.exists() and not args.force:
        raise SystemExit(f"Refusing to overwrite existing file: {output}")

    html = template.read_text(encoding="utf-8")
    html = html.replace("__DIAGRAM_TITLE__", args.title)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(html, encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
