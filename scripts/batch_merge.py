#!/usr/bin/env python3
"""Merge translated JSONL batch files and validate completeness.

Usage:
    python scripts/batch_merge.py batch_*.jsonl -o translated_all.jsonl
    python scripts/batch_merge.py /tmp/batches/ -o translated_all.jsonl --glossary glossary.md
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

_RE_EP = re.compile(r"^EP(\d+)")


def _extract_ep_num(record_id: str) -> int | None:
    m = _RE_EP.match(record_id)
    return int(m.group(1)) if m else None


def main() -> None:
    parser = argparse.ArgumentParser(description="Merge translated JSONL batches")
    parser.add_argument(
        "inputs",
        nargs="+",
        help="Input JSONL files or a directory containing them",
    )
    parser.add_argument("-o", "--output", required=True, help="Output merged JSONL file")
    parser.add_argument(
        "--glossary",
        help="Optional glossary file for term consistency check (markdown with 'term → translation' lines)",
    )
    args = parser.parse_args()

    # Resolve input files
    input_files: list[Path] = []
    for inp in args.inputs:
        p = Path(inp)
        if p.is_dir():
            input_files.extend(sorted(p.glob("*.jsonl")))
        else:
            input_files.append(p)

    if not input_files:
        print("ERROR: no input files found", file=sys.stderr)
        sys.exit(1)

    # Read all records
    records: list[dict] = []
    seen_ids: set[str] = set()
    missing_en: list[str] = []
    episodes: dict[int, int] = defaultdict(int)

    for fpath in sorted(input_files):
        with fpath.open(encoding="utf-8") as f:
            for line_num, line in enumerate(f, 1):
                line = line.rstrip("\n\r")
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"WARNING: {fpath}:{line_num} invalid JSON: {e}", file=sys.stderr)
                    continue

                record_id = obj.get("id", "")
                if record_id in seen_ids:
                    print(f"WARNING: duplicate ID '{record_id}' in {fpath}:{line_num}", file=sys.stderr)
                    continue
                seen_ids.add(record_id)

                # Check for 'en' field
                if "en" not in obj and "english" not in obj:
                    missing_en.append(record_id)

                ep_num = _extract_ep_num(record_id)
                if ep_num is not None:
                    episodes[ep_num] += 1

                records.append(obj)

    # Sort by episode and sequence
    def sort_key(obj: dict) -> tuple[int, int]:
        parts = obj.get("id", "EP00_000").split("_")
        ep = int(parts[0][2:]) if len(parts) >= 1 else 0
        seq = int(parts[1]) if len(parts) >= 2 and parts[1].isdigit() else 0
        return (ep, seq)

    records.sort(key=sort_key)

    # Write merged output
    output_path = Path(args.output)
    with output_path.open("w", encoding="utf-8") as f:
        for obj in records:
            f.write(json.dumps(obj, ensure_ascii=False) + "\n")

    # Report
    print(f"Merged: {len(records)} lines from {len(input_files)} files -> {output_path}")
    print(f"Episodes found: {len(episodes)} ({min(episodes) if episodes else '?'}-{max(episodes) if episodes else '?'})")

    # Check for missing episodes
    if episodes:
        expected = set(range(min(episodes), max(episodes) + 1))
        missing_eps = expected - set(episodes.keys())
        if missing_eps:
            print(f"WARNING: missing episodes: {sorted(missing_eps)}", file=sys.stderr)

    # Check for missing translations
    if missing_en:
        print(f"WARNING: {len(missing_en)} lines missing 'en' field:", file=sys.stderr)
        for rid in missing_en[:10]:
            print(f"  - {rid}", file=sys.stderr)
        if len(missing_en) > 10:
            print(f"  ... and {len(missing_en) - 10} more", file=sys.stderr)

    # Glossary consistency check
    if args.glossary:
        glossary_path = Path(args.glossary)
        if glossary_path.exists():
            terms: dict[str, str] = {}
            with glossary_path.open(encoding="utf-8") as f:
                for gline in f:
                    # Match patterns like "术语 → translation" or "术语 -> translation"
                    m = re.match(r"[-*]\s*(.+?)\s*[→\->]+\s*(.+)", gline.strip())
                    if m:
                        terms[m.group(1).strip()] = m.group(2).strip()

            if terms:
                print(f"\nGlossary check ({len(terms)} terms):")
                all_en_text = " ".join(
                    obj.get("en", obj.get("english", "")) for obj in records
                )
                for cn_term, en_term in terms.items():
                    count = all_en_text.lower().count(en_term.lower())
                    if count == 0:
                        print(f"  MISSING: '{en_term}' (for '{cn_term}') not found in any translation")

    # Summary
    ok = len(missing_en) == 0
    print(f"\nStatus: {'OK' if ok else 'INCOMPLETE'} ({len(records)} lines, {len(missing_en)} missing translations)")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
