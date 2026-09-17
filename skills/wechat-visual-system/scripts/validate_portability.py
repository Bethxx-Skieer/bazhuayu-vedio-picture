#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ABSOLUTE_PATTERNS = (
    re.compile(r"""(?:src|href)\s*=\s*["']/(?!/)""", re.I),
    re.compile(r"""(?:src|href)\s*=\s*["']file://""", re.I),
    re.compile(r"/Users/|/home/|[A-Za-z]:\\"),
)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_portability.py <project-folder>")
        return 2

    root = Path(sys.argv[1]).resolve()
    if not root.is_dir():
        print(f"ERROR: folder not found: {root}")
        return 2

    errors = []
    files = list(root.rglob("*.html")) + list(root.rglob("*.css"))
    if not files:
        errors.append("no HTML or CSS files found")

    for path in files:
        text = path.read_text(encoding="utf-8")
        for pattern in ABSOLUTE_PATTERNS:
            if pattern.search(text):
                errors.append(f"{path.relative_to(root)} contains an absolute path")
        for value in re.findall(r"(?:src|href)\s*=\s*[\"']([^\"']+)[\"']", text, re.I):
            if value.startswith(("http://", "https://", "data:", "#")):
                continue
            target = (path.parent / value.split("#", 1)[0]).resolve()
            if not target.exists():
                errors.append(f"{path.relative_to(root)} references missing file: {value}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"PASS: {len(files)} HTML/CSS files use portable local paths")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
