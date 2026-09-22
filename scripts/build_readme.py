#!/usr/bin/env python3
"""Regenerate the README aggregate from the category files.

Each category file under ``categories/`` starts with an ``# H1`` title,
followed by an intro paragraph and one-line entries of the form::

    - [Name](URL) - Category: one-sentence description.

This script rebuilds two machine-generated sections of ``README.md`` in place,
between the marker comments:

    <!-- BEGIN:COVERAGE --> ... <!-- END:COVERAGE -->
    <!-- BEGIN:FULL_LIST --> ... <!-- END:FULL_LIST -->

Everything outside those markers is hand-written and left untouched.
Run it after editing any category file:

    python scripts/build_readme.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATEGORIES_DIR = ROOT / "categories"
README = ROOT / "README.md"

# Order categories appear in the README. Files not listed here are appended
# alphabetically, so a new category still shows up even before it's ordered.
ORDER = [
    "open-alternatives-replicas.md",
    "ports-runtimes.md",
    "sdks-integrations.md",
    "benchmarks-calibration.md",
    "related-discussions.md",
]

ENTRY_RE = re.compile(r"^- \[.+?\]\(.+?\)")


def ordered_category_files() -> list[Path]:
    files = {p.name: p for p in CATEGORIES_DIR.glob("*.md")}
    ordered = [files.pop(name) for name in ORDER if name in files]
    ordered += [files[name] for name in sorted(files)]
    return ordered


def parse_category(path: Path) -> tuple[str, str, list[str]]:
    """Return (title, anchor, entries) for one category file."""
    lines = path.read_text(encoding="utf-8").splitlines()
    title = ""
    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
            break
    if not title:
        raise ValueError(f"{path.name}: no '# Title' heading found")
    anchor = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    entries = [line.rstrip() for line in lines if ENTRY_RE.match(line)]
    return title, anchor, entries


def build_sections() -> tuple[str, str]:
    coverage_lines: list[str] = []
    full_lines: list[str] = []
    total = 0

    for path in ordered_category_files():
        title, anchor, entries = parse_category(path)
        count = len(entries)
        total += count
        noun = "entry" if count == 1 else "entries"
        coverage_lines.append(f"- [{title}](#{anchor}) — {count} {noun}")

        full_lines.append(f"### {title}\n")
        full_lines.append(f"Source file: [`categories/{path.name}`](categories/{path.name})\n")
        full_lines.extend(entries)
        full_lines.append("")

    coverage = (
        f"**{total} entries across {len(ordered_category_files())} categories.**\n\n"
        + "\n".join(coverage_lines)
    )
    full_list = "\n".join(full_lines).rstrip()
    return coverage, full_list


def replace_block(text: str, name: str, body: str) -> str:
    begin = f"<!-- BEGIN:{name} -->"
    end = f"<!-- END:{name} -->"
    pattern = re.compile(re.escape(begin) + r".*?" + re.escape(end), re.DOTALL)
    if not pattern.search(text):
        raise ValueError(f"README is missing the {begin} / {end} markers")
    return pattern.sub(f"{begin}\n{body}\n{end}", text)


def main() -> int:
    coverage, full_list = build_sections()
    text = README.read_text(encoding="utf-8")
    text = replace_block(text, "COVERAGE", coverage)
    text = replace_block(text, "FULL_LIST", full_list)
    README.write_text(text, encoding="utf-8")
    print("README.md regenerated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
