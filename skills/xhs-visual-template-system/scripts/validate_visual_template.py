#!/usr/bin/env python3
"""Validate portable HTML social-card projects for xhs-visual-template-system."""

from __future__ import annotations

import argparse
import re
import struct
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlparse


ASSET_RE = re.compile(r"(?:src|href)\s*=\s*['\"]([^'\"]+)['\"]", re.I)
CLASS_RE = re.compile(r"class\s*=\s*['\"]([^'\"]+)['\"]", re.I)
HEX_RE = re.compile(r"#[0-9a-fA-F]{6}\b")
IMPORT_RE = re.compile(r"@import\s+(?:url\()?['\"]?([^'\")\s;]+)", re.I)


@dataclass
class Issue:
    level: str
    path: Path
    message: str


def png_size(path: Path) -> tuple[int, int] | None:
    try:
        with path.open("rb") as file:
            if file.read(8) != b"\x89PNG\r\n\x1a\n":
                return None
            length = struct.unpack(">I", file.read(4))[0]
            chunk = file.read(4)
            if chunk != b"IHDR" or length < 8:
                return None
            width, height = struct.unpack(">II", file.read(8))
            return width, height
    except OSError:
        return None


def local_asset(base: Path, raw: str) -> Path | None:
    raw = raw.strip()
    parsed = urlparse(raw)
    if parsed.scheme or raw.startswith("//") or raw.startswith("#"):
        return None
    return (base / unquote(raw.split("?", 1)[0].split("#", 1)[0])).resolve()


def css_bundle(path: Path, visited: set[Path] | None = None) -> str:
    visited = visited or set()
    path = path.resolve()
    if path in visited or not path.exists():
        return ""
    visited.add(path)
    css = path.read_text(encoding="utf-8")
    parts = [css]
    for raw in IMPORT_RE.findall(css):
        imported = local_asset(path.parent, raw)
        if imported and imported.suffix.lower() == ".css":
            parts.append(css_bundle(imported, visited))
    return "\n".join(parts)


def validate_html(path: Path, issues: list[Issue]) -> None:
    text = path.read_text(encoding="utf-8")
    lower = text.lower()

    def error(message: str) -> None:
        issues.append(Issue("ERROR", path, message))

    def warn(message: str) -> None:
        issues.append(Issue("WARN", path, message))

    def note(message: str) -> None:
        issues.append(Issue("NOTICE", path, message))

    if '<meta charset="utf-8"' not in lower and "<meta charset='utf-8'" not in lower:
        warn("missing explicit UTF-8 meta tag")
    if "page-shell" not in text:
        error("missing page-shell component")
    if 'data-theme="' not in lower and "data-theme='" not in lower:
        error("missing data-theme on page shell")
    if 'data-page-job="' not in lower and "data-page-job='" not in lower:
        error("missing data-page-job")
    if "headline-block" not in text:
        error("missing headline-block")

    logo_count = len(re.findall(r"class\s*=\s*['\"][^'\"]*\bbrand-lockup\b", text, re.I))
    logo_omission_approved = bool(
        re.search(r"data-logo-policy\s*=\s*['\"]omitted-approved['\"]", text, re.I)
    )
    if logo_count != 1 and not (logo_count == 0 and logo_omission_approved):
        error(f"expected exactly one brand-lockup, found {logo_count}")
    elif logo_count == 0 and logo_omission_approved:
        note("brand-lockup omission approved by registered template")

    missing_count = len(re.findall(r"data-asset-state\s*=\s*['\"]missing['\"]", text, re.I))
    for match in re.finditer(
        r"<[^>]+data-asset-state\s*=\s*['\"]missing['\"][^>]*>", text, re.I
    ):
        tag = match.group(0)
        asset = re.search(r"data-required-asset\s*=\s*['\"]([^'\"]+)['\"]", tag, re.I)
        if not asset:
            error("missing placeholder has no data-required-asset description")
        else:
            note(f"missing asset: {asset.group(1)}")
    if missing_count and "media-placeholder" not in text:
        error("missing asset state must use media-placeholder")

    callout_count = len(re.findall(r"\bshot-callout\b", text))
    if callout_count > 2:
        warn(f"screenshot annotation cap exceeded: {callout_count} > 2")

    process_count = len(re.findall(r"class\s*=\s*['\"][^'\"]*\bprocess-node\b", text, re.I))
    if process_count > 5:
        warn(f"process-node cap exceeded: {process_count} > 5")

    feature_count = len(re.findall(r"class\s*=\s*['\"][^'\"]*\bfeature-item\b", text, re.I))
    if feature_count > 4:
        warn(f"feature-item cap exceeded: {feature_count} > 4")

    cta_count = len(re.findall(r"class\s*=\s*['\"][^'\"]*\bcta-button\b", text, re.I))
    if cta_count > 1:
        warn(f"CTA cap exceeded: {cta_count} > 1")

    css_paths: list[Path] = []
    for raw in ASSET_RE.findall(text):
        if raw.startswith(("http://", "https://", "file://", "//")):
            error(f"external or absolute asset reference is not portable: {raw}")
            continue
        if raw.startswith(("data:", "mailto:", "tel:", "#")):
            continue
        asset_path = local_asset(path.parent, raw)
        if asset_path is None:
            continue
        if not asset_path.exists():
            error(f"referenced asset does not exist: {raw}")
        elif asset_path.suffix.lower() == ".css":
            css_paths.append(asset_path)

    if "/users/" in lower or "file:///" in lower:
        error("HTML contains a machine-specific absolute path")

    if not css_paths:
        error("no local stylesheet found")
    for css_path in css_paths:
        css = css_bundle(css_path)
        css_lower = css.lower()
        if "width: 1080px" not in css_lower or "height: 1440px" not in css_lower:
            error(f"stylesheet does not declare 1080×1440 canvas: {css_path.name}")
        if "--brand-blue: #0055ff" not in css_lower:
            error(f"stylesheet is missing official brand-blue token: {css_path.name}")
        if "--ink: #14213d" not in css_lower:
            warn(f"stylesheet is missing expected ink token: {css_path.name}")


def validate_png(path: Path, issues: list[Issue]) -> None:
    size = png_size(path)
    if size is None:
        issues.append(Issue("WARN", path, "not a readable PNG or IHDR missing"))
        return
    allowed_preview_names = ("preview", "montage", "gallery", "总览")
    if size != (1080, 1440) and not any(token in path.stem for token in allowed_preview_names):
        issues.append(Issue("ERROR", path, f"expected 1080×1440, found {size[0]}×{size[1]}"))


def collect_paths(inputs: list[Path]) -> tuple[list[Path], list[Path]]:
    html: list[Path] = []
    png: list[Path] = []
    for item in inputs:
        if item.is_dir():
            html.extend(sorted(item.rglob("*.html")))
            png.extend(
                sorted(
                    candidate
                    for candidate in item.rglob("*.png")
                    if "assets" not in candidate.relative_to(item).parts
                )
            )
        elif item.suffix.lower() == ".html":
            html.append(item)
        elif item.suffix.lower() == ".png":
            png.append(item)
    return sorted(set(html)), sorted(set(png))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path, help="HTML, PNG, or project directories")
    args = parser.parse_args()

    html_paths, png_paths = collect_paths(args.paths)
    if not html_paths and not png_paths:
        print("ERROR: no HTML or PNG files found", file=sys.stderr)
        return 2

    issues: list[Issue] = []
    for path in html_paths:
        validate_html(path.resolve(), issues)
    for path in png_paths:
        validate_png(path.resolve(), issues)

    for issue in issues:
        print(f"{issue.level}: {issue.path}: {issue.message}")

    error_count = sum(issue.level == "ERROR" for issue in issues)
    warning_count = sum(issue.level == "WARN" for issue in issues)
    notice_count = sum(issue.level == "NOTICE" for issue in issues)
    print(
        f"Checked {len(html_paths)} HTML and {len(png_paths)} PNG files — "
        f"{error_count} error(s), {warning_count} warning(s), {notice_count} notice(s)."
    )
    return 1 if error_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
