# Extract Sheet

Use this template to structure raw script text into translatable JSONL before full localization. This preprocessing step reduces token cost in subsequent localization passes and ensures consistent line tracking.

## When to use

- The user provides a raw script, episode dump, or multi-page scene text
- The input contains non-translatable content (stage directions, camera notes, formatting) mixed with translatable text
- Batch processing multiple scenes or episodes

When the user provides only a few pre-structured lines, skip this step and go directly to localization.

## DOCX Preprocessing

Use this step when the user provides a `.docx` file instead of pasted text.

A `.docx` file is a ZIP archive containing XML. It cannot be read directly as plain text. Follow these steps in order:

1. Extract the file using Python's `zipfile` module and read `word/document.xml` from inside the ZIP.
2. Parse the XML to extract all `<w:t>` text run elements. Join runs without separator, and separate paragraphs with a newline.
3. Write the extracted plain text to a UTF-8 encoded intermediate `.txt` file before any further processing. This step is mandatory for Chinese text — skipping it causes mojibake from incorrect encoding assumptions.
4. `document.xml` inside a `.docx` can exceed 1 MB and will exceed direct read-tool limits. Always work from the intermediate `.txt` file, not the raw XML.
5. Once you have the plain-text intermediate file, proceed with JSONL extraction below.

If `python-docx` is available (`pip install python-docx`), prefer it over manual zipfile+xml parsing — it handles run splitting and paragraph styles automatically.

```python
# Minimal example using python-docx
from docx import Document
doc = Document('script.docx')
with open('script_extracted.txt', 'w', encoding='utf-8') as f:
    for para in doc.paragraphs:
        if para.text.strip():
            f.write(para.text + '\n')
```

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
- **Strip all production-side content** — it is NOT translatable text. Use it as context only.
- If a line serves dual function (e.g. dialogue that is also an on-screen card), classify by primary viewer-facing function
- Maintain sequential numbering within each episode; do not skip IDs

### Content triage for Chinese drama scripts

Apply this classification to every line before extraction. Only lines marked EXTRACT go into the JSONL output. Lines marked STRIP are read for context but never sent to translation.

| Line pattern | Classification | Action |
|---|---|---|
| 角色名："台词" or 角色名：台词 | Dialogue | EXTRACT as `dialogue` |
| 旁白：text / 画外音 | Narration | EXTRACT as `narration` |
| 【现况：...】/ 【字幕：...】 | Status card | EXTRACT as `card` |
| 第X集：标题 | Episode title | EXTRACT as `card` |
| 屏幕渐黑，字幕浮现：【...】 | End-card caption | EXTRACT the 【】 content as `card` |
| （第X集完） | Episode end tag | EXTRACT as `card` |
| △ action/blocking/expression | Stage direction | STRIP — context only |
| 场 X-Y 日/夜 内/外 地点 | Scene header | STRIP — context only |
| 角色名（情绪标签）： | Emotion tag | STRIP — attach emotion to next dialogue line's `emotion` field |
| 镜头切换/特写/推拉 | Camera cue | STRIP |
| BGM/音效/♪ | Audio cue | STRIP |
| 角色设定/人物小传/故事概述 | Production reference | STRIP |

**Critical:** When stage directions contain embedded viewer-visible text (e.g., △ 屏幕上浮现文字："真相只有一个"), extract only the quoted on-screen text, not the stage direction wrapper.

**Ratio check:** In a typical Chinese drama script, 40–60% of lines are production-side. If your JSONL output contains nearly as many lines as the raw input, you are probably extracting production content. Re-check your triage.

## Notes

- This output feeds directly into Step 1 of the main localization workflow
- The JSONL format is designed for batch processing: each line can be localized independently with its embedded context
- For multi-episode batches, reset sequence numbering per episode

## Series-Scale Batch Guidance

Use this section when processing a full series (10+ episodes, 500+ extractable lines).

### Chunking strategy

- Process one episode at a time. Reset sequence numbering per episode (IDs restart at `_001`).
- Keep each JSONL batch to roughly 300–400 lines before handing off to the localization step. This fits within safe context limits for most models.
- Never merge multiple episodes into a single JSONL file for the localization step — the localization model needs episode-scoped context, not series-scoped context.

### Glossary tracking

Maintain a running glossary alongside the JSONL output. Lock entries after Episode 1 and never vary them across subsequent episodes.

| Term (Chinese) | Approved English rendering | Notes |
|---|---|---|
| Character names | | One row per main and recurring character |
| In-world proper nouns | | Faction names, place names, titles, artifacts |
| Recurring slang or catchphrases | | Lock in after Ep 1, do not vary |
| Honorifics kept verbatim | | e.g. 师尊, 殿下 — note if kept or swapped |

Before localizing any episode beyond Episode 1, re-read the glossary. Do not introduce a new English rendering for any term already in the glossary.

### Character voice cards

After Episode 1 is complete, write one-line voice descriptors for all recurring characters. Reference this card at the start of each subsequent episode's localization pass.

Example format:
```
男主: clipped, threat-forward, drops subjects. Never apologizes.
女主: precise diction, dry humor, uses full sentences even under pressure.
反派A: elaborate, formal register, addresses everyone as inferiors.
```

### Output routing for full-series delivery

When total extractable lines exceed ~100 (roughly one mid-length episode), markdown tables in chat become impractical for the user.

- At that threshold, confirm with the user: chat tables or Word document?
- If Word document: complete all localization and QA first, then invoke the docx skill to format and deliver the final file.
- Do not start the docx skill until all localization passes are complete.
