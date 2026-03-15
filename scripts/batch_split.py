#!/usr/bin/env python3
"""Split a viewer-facing JSONL file into batches by episode range.

Usage:
    python scripts/batch_split.py viewer.jsonl --batch-size 10 --output-dir /tmp/batches/
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
    parser = argparse.ArgumentParser(description="Split JSONL into batches by episode")
    parser.add_argument("input", help="Input JSONL file")
    parser.add_argument(
        "--batch-size",
        type=int,
        default=10,
        help="Number of episodes per batch (default: 10)",
    )
    parser.add_argument(
        "--output-dir",
        default=".",
        help="Output directory for batch files (default: current dir)",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Group lines by episode number
    episodes: dict[int, list[str]] = defaultdict(list)
    with input_path.open(encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n\r")
            if not line:
                continue
            obj = json.loads(line)
            ep_num = _extract_ep_num(obj.get("id", ""))
            if ep_num is None:
                print(f"WARNING: skipping line with no episode ID: {obj.get('id')}", file=sys.stderr)
                continue
            episodes[ep_num].append(line)

    if not episodes:
        print("ERROR: no episodes found in input file", file=sys.stderr)
        sys.exit(1)

    all_eps = sorted(episodes.keys())
    batch_size = args.batch_size

    # Create batches
    batch_num = 0
    i = 0
    total_lines = 0
    while i < len(all_eps):
        batch_num += 1
        batch_eps = all_eps[i : i + batch_size]
        batch_file = output_dir / f"batch_{batch_num:02d}.jsonl"

        line_count = 0
        with batch_file.open("w", encoding="utf-8") as f:
            for ep in batch_eps:
                for record_line in episodes[ep]:
                    f.write(record_line + "\n")
                    line_count += 1

        ep_range = f"EP{batch_eps[0]:02d}-EP{batch_eps[-1]:02d}"
        print(f"  Batch {batch_num:02d}: {ep_range} ({len(batch_eps)} eps, {line_count} lines) -> {batch_file}")
        total_lines += line_count
        i += batch_size

    print(f"\nSplit complete: {batch_num} batches, {len(all_eps)} episodes, {total_lines} total lines")


if __name__ == "__main__":
    main()
