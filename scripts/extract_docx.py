#!/usr/bin/env python3
"""Extract plain text from a .docx file, with reliable Chinese text handling.

Usage:
    python scripts/extract_docx.py input.docx [output.txt]

If output path is omitted, prints to stdout.
Requires: python-docx (pip install python-docx) — falls back to zipfile+xml if unavailable.
"""

import argparse
import io
import sys
import os


def extract_with_python_docx(path: str) -> list[str]:
    """Extract paragraphs using python-docx (preferred)."""
    from docx import Document

    doc = Document(path)
    return [para.text for para in doc.paragraphs]


def extract_with_zipfile(path: str) -> list[str]:
    """Fallback: extract paragraphs via zipfile + xml.etree."""
    import zipfile
    import xml.etree.ElementTree as ET

    ns = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

    with zipfile.ZipFile(path) as zf:
        xml_bytes = zf.read("word/document.xml")

    root = ET.fromstring(xml_bytes)
    paragraphs: list[str] = []

    for para in root.iter(f"{{{ns}}}p"):
        runs = para.findall(f".//{{{ns}}}t")
        text = "".join(r.text or "" for r in runs)
        paragraphs.append(text)

    return paragraphs


def extract(path: str) -> list[str]:
    """Extract paragraphs from a .docx file. Tries python-docx first, then zipfile."""
    try:
        return extract_with_python_docx(path)
    except ImportError:
        return extract_with_zipfile(path)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract plain text from a .docx file (Chinese-safe, UTF-8 output)."
    )
    parser.add_argument("input", help="Path to the .docx file")
    parser.add_argument(
        "output",
        nargs="?",
        default=None,
        help="Output .txt path (default: stdout)",
    )
    args = parser.parse_args()

    if not os.path.isfile(args.input):
        print(f"Error: file not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    paragraphs = extract(args.input)

    # Build output: skip truly empty paragraphs but preserve structure
    lines = [p for p in paragraphs if p.strip()]

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        total = len(lines)
        print(f"Extracted {total} non-empty paragraphs → {args.output}", file=sys.stderr)
    else:
        # Force UTF-8 on stdout for Windows
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
        for line in lines:
            print(line)


if __name__ == "__main__":
    main()
