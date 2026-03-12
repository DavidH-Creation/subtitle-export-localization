#!/usr/bin/env python3
"""Auto-classify script lines as viewer-facing or production-side.

Reads a plain-text script (one paragraph per line, as produced by extract_docx.py)
and outputs:
  1. A JSONL file of viewer-facing lines (dialogue, cards, narration)
  2. A triage report with statistics

Usage:
    python scripts/triage.py extracted.txt -o viewer_facing.jsonl

Classification rules follow templates/extract-sheet.md content-triage table.
"""

import argparse
import json
import os
import re
import sys


# ---------------------------------------------------------------------------
# Pattern definitions (order matters — first match wins)
# ---------------------------------------------------------------------------

# Production-side patterns → STRIP
_RE_STAGE_DIRECTION = re.compile(r"^[△▲]")
_RE_SCENE_HEADER = re.compile(r"^场\s*\d")
_RE_CAMERA_CUE = re.compile(r"^(镜头|特写|推拉|切换|俯拍|仰拍|航拍)")
_RE_BGM_SFX = re.compile(r"^(BGM|音效|♪|bgm|SFX)")
_RE_BIO_SYNOPSIS = re.compile(r"^(角色设定|人物小传|故事概述|故事梗概|总体故事|核心人物)")
_RE_TAG_LINE = re.compile(
    r"^(女频|男频|标签|类型|关键词)"
)

# Viewer-facing patterns → EXTRACT
_RE_EPISODE_TITLE = re.compile(r"^第[一二三四五六七八九十百千\d]+[集章节回]")
_RE_EPISODE_END = re.compile(r"^（第[一二三四五六七八九十百千\d]+[集章节回][完]）")
_RE_CARD_BRACKET = re.compile(r"^【.*】$")
_RE_NARRATION = re.compile(r"^(旁白|画外音|电子音|广播|系统)[：:（(]")
_RE_EMBEDDED_CARD = re.compile(r"【(.+?)】")

# Dialogue: "角色名（情绪）：台词" or "角色名：台词"
# Speaker name is typically 2-5 Chinese chars, optionally followed by (emotion)
_RE_DIALOGUE = re.compile(
    r"^(?P<speaker>[\u4e00-\u9fff\w]{1,8})"       # speaker name
    r"(?:[（(](?P<emotion>[^)）]+)[)）])?"          # optional emotion tag
    r"[：:]"                                        # colon
    r"\s*(?P<line>.+)"                              # spoken line
)

# Scene status card embedded in stage direction (△ 屏幕渐黑，字幕浮现：)
_RE_SCREEN_TEXT_CUE = re.compile(r"(屏幕|字幕|画面).*(浮现|显示|出现)")


# ---------------------------------------------------------------------------
# Episode tracking
# ---------------------------------------------------------------------------

_EPISODE_NUM_MAP = {
    "一": 1, "二": 2, "三": 3, "四": 4, "五": 5,
    "六": 6, "七": 7, "八": 8, "九": 9, "十": 10,
    "十一": 11, "十二": 12, "十三": 13, "十四": 14, "十五": 15,
    "十六": 16, "十七": 17, "十八": 18, "十九": 19, "二十": 20,
    "二十一": 21, "二十二": 22, "二十三": 23, "二十四": 24, "二十五": 25,
    "二十六": 26, "二十七": 27, "二十八": 28, "二十九": 29, "三十": 30,
    "三十一": 31, "三十二": 32, "三十三": 33, "三十四": 34, "三十五": 35,
    "三十六": 36, "三十七": 37, "三十八": 38, "三十九": 39, "四十": 40,
    "四十一": 41, "四十二": 42, "四十三": 43, "四十四": 44, "四十五": 45,
    "四十六": 46, "四十七": 47, "四十八": 48, "四十九": 49, "五十": 50,
}


def _parse_episode_num(text: str) -> int | None:
    """Try to extract episode number from a title line."""
    m = re.search(r"第([一二三四五六七八九十百千]+|\d+)[集章节回]", text)
    if not m:
        return None
    raw = m.group(1)
    if raw.isdigit():
        return int(raw)
    return _EPISODE_NUM_MAP.get(raw)


# ---------------------------------------------------------------------------
# Classification engine
# ---------------------------------------------------------------------------

def classify_line(text: str) -> dict | None:
    """Classify a single line. Returns a dict with extraction fields, or None to strip."""

    stripped = text.strip()
    if not stripped:
        return None

    # --- STRIP patterns ---
    if _RE_STAGE_DIRECTION.match(stripped):
        # But check for embedded viewer-visible text
        cards = _RE_EMBEDDED_CARD.findall(stripped)
        if cards:
            return {
                "type": "card",
                "speaker": None,
                "raw": "【" + "】【".join(cards) + "】",
                "emotion": None,
            }
        return None

    if _RE_SCENE_HEADER.match(stripped):
        return None
    if _RE_CAMERA_CUE.match(stripped):
        return None
    if _RE_BGM_SFX.match(stripped):
        return None
    if _RE_BIO_SYNOPSIS.match(stripped):
        return None
    if _RE_TAG_LINE.match(stripped):
        return None

    # --- EXTRACT patterns ---

    # Episode title
    if _RE_EPISODE_TITLE.match(stripped):
        return {"type": "card", "speaker": None, "raw": stripped, "emotion": None}

    # Episode end tag
    if _RE_EPISODE_END.match(stripped):
        return {"type": "card", "speaker": None, "raw": stripped, "emotion": None}

    # On-screen card 【...】
    if _RE_CARD_BRACKET.match(stripped):
        return {"type": "card", "speaker": None, "raw": stripped, "emotion": None}

    # Narration / system voice
    m = _RE_NARRATION.match(stripped)
    if m:
        # Extract the narration text after the speaker label
        colon_pos = stripped.find("：")
        if colon_pos == -1:
            colon_pos = stripped.find(":")
        narration_text = stripped[colon_pos + 1 :].strip() if colon_pos >= 0 else stripped
        speaker_label = m.group(1)
        return {
            "type": "narration",
            "speaker": speaker_label,
            "raw": narration_text,
            "emotion": None,
        }

    # Dialogue
    m = _RE_DIALOGUE.match(stripped)
    if m:
        speaker = m.group("speaker")
        emotion = m.group("emotion")
        line = m.group("line").strip()

        # Filter out character bios that look like dialogue
        # (speaker followed by a very long description without quotes)
        if len(line) > 80 and "\uff1a" not in line and "\u201c" not in line and '"' not in line:
            # Likely a character bio, not dialogue
            return None

        # Strip surrounding quotes if present
        if (line.startswith("\u201c") and line.endswith("\u201d")) or (
            line.startswith('"') and line.endswith('"')
        ):
            line = line[1:-1]

        return {
            "type": "dialogue",
            "speaker": speaker,
            "raw": line,
            "emotion": emotion,
        }

    # Screen text cue in a stage-direction-like line
    if _RE_SCREEN_TEXT_CUE.search(stripped):
        cards = _RE_EMBEDDED_CARD.findall(stripped)
        if cards:
            return {
                "type": "card",
                "speaker": None,
                "raw": "【" + "】【".join(cards) + "】",
                "emotion": None,
            }

    # Standalone 【...】 content embedded in other text
    cards = _RE_EMBEDDED_CARD.findall(stripped)
    if cards and len("".join(cards)) > len(stripped) * 0.5:
        return {
            "type": "card",
            "speaker": None,
            "raw": "【" + "】【".join(cards) + "】",
            "emotion": None,
        }

    # If nothing matched, strip it (likely a production note or formatting)
    return None


# Detect speaker-only lines (dialogue split across two lines)
# Matches: "角色名（情绪）：" or "角色名：" with no dialogue text,
# or with only an opening quote character.
_RE_SPEAKER_ONLY = re.compile(
    r"^(?P<speaker>[\u4e00-\u9fff\w]{1,8})"
    r"(?:[（(](?P<emotion>[^)）]+)[)）])?"
    r"[：:]\s*"
    r"(?P<partial>[\u201c\"']?)$"  # optionally starts a quote but nothing else
)


def _merge_split_lines(raw_lines: list[str]) -> list[str]:
    """Merge split-dialogue lines where speaker and text are on separate lines.

    Chinese drama scripts often split dialogue like:
        谢烈（烦躁）：
        "台词内容"
    or:
        男生（崩溃）："
        台词内容"

    This function merges them into single lines before classification.
    """
    merged: list[str] = []
    i = 0
    while i < len(raw_lines):
        line = raw_lines[i].rstrip("\n\r")
        stripped = line.strip()

        if not stripped:
            merged.append(line)
            i += 1
            continue

        m = _RE_SPEAKER_ONLY.match(stripped)
        if m and i + 1 < len(raw_lines):
            next_line = raw_lines[i + 1].rstrip("\n\r").strip()
            if next_line:
                # Merge: speaker line + next line
                partial = m.group("partial") or ""
                if partial:
                    # Speaker line already has opening quote, e.g. 男生（崩溃）："
                    merged.append(stripped + next_line)
                else:
                    # Speaker line ends with just colon, next line has full quote
                    merged.append(stripped + next_line)
                i += 2
                continue

        merged.append(line)
        i += 1

    return merged


def process_file(input_path: str) -> tuple[list[dict], dict]:
    """Process an entire script file. Returns (jsonl_records, stats)."""

    with open(input_path, "r", encoding="utf-8") as f:
        raw_lines = f.readlines()

    # Pre-process: merge split-dialogue lines
    lines = _merge_split_lines(raw_lines)

    records: list[dict] = []
    current_episode = 0
    seq = 0
    total_lines = len(raw_lines)  # report original line count
    stripped_count = 0
    in_production_header = True  # start in production zone (title, bios, synopsis)

    for line in lines:
        text = line.rstrip("\n\r")
        if not text.strip():
            continue

        # Check for episode title — only match lines that START with 第X集
        if _RE_EPISODE_TITLE.match(text.strip()):
            ep = _parse_episode_num(text)
            if ep is not None:
                current_episode = ep
                seq = 0
            in_production_header = False  # episode content starts

        result = classify_line(text)

        # Strip dialogue-like lines that appear before the first episode
        # (these are character bios, synopsis, etc.)
        if in_production_header and result is not None and result["type"] == "dialogue":
            stripped_count += 1
            continue

        if result is None:
            stripped_count += 1
            continue

        seq += 1
        ep_label = f"EP{current_episode:02d}" if current_episode > 0 else "EP00"
        result["id"] = f"{ep_label}_{seq:03d}"

        # Add scene tag placeholder (agent will refine)
        if "scene" not in result:
            result["scene"] = ""

        records.append(result)

    non_empty = sum(1 for l in lines if l.strip())
    extracted = len(records)

    stats = {
        "total_lines": total_lines,
        "non_empty_lines": non_empty,
        "extracted": extracted,
        "stripped": non_empty - extracted,
        "extract_ratio": round(extracted / non_empty * 100, 1) if non_empty else 0,
        "strip_ratio": round((non_empty - extracted) / non_empty * 100, 1) if non_empty else 0,
        "episodes_detected": current_episode,
    }

    return records, stats


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Auto-classify script lines into viewer-facing JSONL."
    )
    parser.add_argument("input", help="Path to extracted .txt script file")
    parser.add_argument(
        "-o", "--output",
        default=None,
        help="Output JSONL path (default: <input_stem>_viewer.jsonl)",
    )
    parser.add_argument(
        "--report",
        default=None,
        help="Output report path (default: <input_stem>_report.txt)",
    )
    args = parser.parse_args()

    if not os.path.isfile(args.input):
        print(f"Error: file not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    stem = os.path.splitext(args.input)[0]
    output_path = args.output or f"{stem}_viewer.jsonl"
    report_path = args.report or f"{stem}_report.txt"

    records, stats = process_file(args.input)

    # Write JSONL
    with open(output_path, "w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    # Write report
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("=== Content Triage Report ===\n\n")
        f.write(f"Input file:      {args.input}\n")
        f.write(f"Total lines:     {stats['total_lines']}\n")
        f.write(f"Non-empty lines: {stats['non_empty_lines']}\n")
        f.write(f"Extracted:       {stats['extracted']} ({stats['extract_ratio']}%)\n")
        f.write(f"Stripped:        {stats['stripped']} ({stats['strip_ratio']}%)\n")
        f.write(f"Episodes:        {stats['episodes_detected']}\n\n")

        # Ratio sanity check
        if stats["strip_ratio"] < 30:
            f.write(
                "⚠ WARNING: Strip ratio below 30%. "
                "You may be extracting production content. Re-check triage rules.\n\n"
            )
        elif stats["strip_ratio"] > 70:
            f.write(
                "⚠ WARNING: Strip ratio above 70%. "
                "You may be stripping viewer-facing content. Re-check triage rules.\n\n"
            )
        else:
            f.write("✓ Strip ratio within expected 30-70% range.\n\n")

        # Type breakdown
        type_counts: dict[str, int] = {}
        for rec in records:
            t = rec["type"]
            type_counts[t] = type_counts.get(t, 0) + 1

        f.write("Type breakdown:\n")
        for t, c in sorted(type_counts.items()):
            f.write(f"  {t}: {c}\n")

    # Print summary to stderr
    print(f"Triage complete:", file=sys.stderr)
    print(f"  {stats['extracted']} viewer-facing lines → {output_path}", file=sys.stderr)
    print(f"  {stats['stripped']} production lines stripped", file=sys.stderr)
    print(f"  Strip ratio: {stats['strip_ratio']}%", file=sys.stderr)
    print(f"  Report → {report_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
