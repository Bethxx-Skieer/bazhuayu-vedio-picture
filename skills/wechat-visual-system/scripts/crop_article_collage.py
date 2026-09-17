#!/usr/bin/env python3
"""Create a compact derivative of a 1920x1080 article screenshot collage."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


DEFAULT_BOXES = {
    2: (30, 40, 1890, 890),
    3: (30, 40, 1890, 830),
    4: (30, 40, 1890, 820),
}


def parse_box(value: str) -> tuple[int, int, int, int]:
    parts = tuple(int(part.strip()) for part in value.split(","))
    if len(parts) != 4:
        raise argparse.ArgumentTypeError("box must be left,top,right,bottom")
    return parts


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path, nargs="?")
    parser.add_argument("--count", type=int, choices=(2, 3, 4), default=3)
    parser.add_argument("--box", type=parse_box)
    args = parser.parse_args()

    output = args.output or args.input.with_name(f"{args.input.stem}-cropped.png")
    box = args.box or DEFAULT_BOXES[args.count]

    with Image.open(args.input) as image:
        if image.size != (1920, 1080):
            raise SystemExit(f"expected a 1920x1080 master, got {image.size}")
        left, top, right, bottom = box
        if not (0 <= left < right <= image.width and 0 <= top < bottom <= image.height):
            raise SystemExit(f"invalid crop box {box} for {image.size}")
        output.parent.mkdir(parents=True, exist_ok=True)
        image.crop(box).save(output, optimize=True)

    print(f"saved={output} box={box} size={right-left}x{bottom-top}")


if __name__ == "__main__":
    main()
