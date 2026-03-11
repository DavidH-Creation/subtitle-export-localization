# Extract Sheet

Use this template to structure raw script text into translatable JSONL before full localization. This preprocessing step reduces token cost in subsequent localization passes and ensures consistent line tracking.

## When to use

- The user provides a raw script, episode dump, or multi-page scene text
- The input contains non-translatable content (stage directions, camera notes, formatting) mixed with translatable text
- Batch processing multiple scenes or episodes

When the user provides only a few pre-structured lines, skip this step and go directly to localization.

## Source Info

- Series / episode:
- Scene range:
- Total lines extracted:
- Extraction model used:

## JSONL Field Specification

One JSON object per line. All fields are strings unless noted.

| Field | Required | Description |
|---|---|---|
| id | Yes | Unique ID. Format: `S{season}E{episode}_{seq}`, e.g. `S01E03_042`. Use `EP{n}_{seq}` for unnumbered content. |
| type | Yes | One of: `dialogue`, `narration`, `card`, `on-screen-text` |
| speaker | Yes* | Character name or role label (e.g. "女主", "反派A"). Set to `null` for cards and on-screen text. |
| raw | Yes | Original Chinese text, verbatim. Do not clean, simplify, or pre-translate. |
| scene | Yes | Brief scene-context tag, 2-6 characters (e.g. "对峙/威胁", "日常/撒娇", "集末钩子"). |
| relationship | No | Speaker-to-target relationship (e.g. "女主→反派", "男主→女二"). Omit for cards or when no clear target. |
| emotion | No | Emotional register tag (e.g. "冷怒", "撒娇", "平静", "嘲讽"). |
| prev_line | No | One-sentence context summary of what just happened. Not the literal previous line. Keep under 20 characters. |

## Example Output

```jsonl
{"id": "S01E03_041", "type": "narration", "speaker": null, "raw": "三年后，A市", "scene": "时间跳转", "emotion": "平静"}
{"id": "S01E03_042", "type": "dialogue", "speaker": "女主", "raw": "你敢动她试试", "scene": "对峙/威胁", "relationship": "女主→反派", "emotion": "冷怒", "prev_line": "反派威胁要伤害女二"}
{"id": "S01E03_043", "type": "dialogue", "speaker": "反派", "raw": "你以为你是谁", "scene": "对峙/威胁", "relationship": "反派→女主", "emotion": "轻蔑", "prev_line": "女主警告反派"}
{"id": "S01E03_044", "type": "card", "speaker": null, "raw": "已捕获S级供暖设备 x1", "scene": "集末钩子", "emotion": "反差萌"}
{"id": "S01E03_045", "type": "on-screen-text", "speaker": null, "raw": "学生会执法队正在介入……", "scene": "悬念提示", "emotion": "紧张"}
```

## Extraction Rules

- Keep `raw` verbatim: do not fix typos, normalize punctuation, or remove internet slang markers
- `scene` and `emotion` are brief tags, not full descriptions
- `prev_line` is a context summary for the localization model, not the literal previous dialogue line
- Strip stage directions, camera notes, BGM cues, and production annotations — they are not translatable text
- If a line serves dual function (e.g. dialogue that is also an on-screen card), classify by primary viewer-facing function
- Maintain sequential numbering within each episode; do not skip IDs

## Notes

- This output feeds directly into Step 1 of the main localization workflow
- The JSONL format is designed for batch processing: each line can be localized independently with its embedded context
- For multi-episode batches, reset sequence numbering per episode
