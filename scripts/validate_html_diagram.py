#!/usr/bin/env python3
"""Static validation for standalone neural-network HTML dynamic diagrams."""

from __future__ import annotations

import argparse
import re
from html.parser import HTMLParser
from pathlib import Path


class TagCounter(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tags: dict[str, int] = {}
        self.attrs: list[tuple[str, dict[str, str]]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.tags[tag] = self.tags.get(tag, 0) + 1
        self.attrs.append((tag, {key: value or "" for key, value in attrs}))


def inline_script_blocks(html: str) -> list[str]:
    pattern = re.compile(
        r"<script(?![^>]*\bsrc=)(?![^>]*type=[\"']module[\"'])[^>]*>(.*?)</script>",
        re.IGNORECASE | re.DOTALL,
    )
    return [match.group(1).strip() for match in pattern.finditer(html)]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html_file", help="HTML diagram to validate")
    args = parser.parse_args()

    path = Path(args.html_file).expanduser().resolve()
    html = path.read_text(encoding="utf-8")
    parser_obj = TagCounter()
    parser_obj.feed(html)

    problems: list[str] = []
    required_tags = ["html", "head", "body", "title", "style", "script"]
    for tag in required_tags:
        if parser_obj.tags.get(tag, 0) == 0:
            problems.append(f"Missing <{tag}> tag")

    has_viewport = any(
        tag == "meta" and attrs.get("name") == "viewport"
        for tag, attrs in parser_obj.attrs
    )
    if not has_viewport:
        problems.append("Missing viewport meta tag")

    if "TODO" in html or "__DIAGRAM_TITLE__" in html:
        problems.append("Template placeholder or TODO text remains")

    has_visual_surface = any(parser_obj.tags.get(tag, 0) for tag in ("svg", "canvas"))
    if not has_visual_surface:
        problems.append("Expected at least one <svg> or <canvas> visual surface")

    scripts = inline_script_blocks(html)
    if not scripts:
        problems.append("Expected at least one inline classic <script> block")

    control_words = ["play", "pause", "reset", "next", "prev", "播放", "暂停", "重置", "下一步", "上一步"]
    if not any(word in html for word in control_words):
        problems.append("No obvious animation control labels found")

    if problems:
        print(f"Validation failed: {path}")
        for problem in problems:
            print(f"- {problem}")
        raise SystemExit(1)

    print(f"Validation passed: {path}")
    print(f"Inline classic scripts: {len(scripts)}")
    print(f"SVG tags: {parser_obj.tags.get('svg', 0)}; canvas tags: {parser_obj.tags.get('canvas', 0)}")


if __name__ == "__main__":
    main()
