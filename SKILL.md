---
name: subtitle-export-localization
version: 0.2.0
description: Localize Chinese drama, manhua-drama, and scripted dialogue, narration, and on-screen text — from a single scene to a full multi-episode series — for subtitle-led overseas release. Use when the user wants bilingual scene rewrites, subtitle-ready dialogue, narration localization, meme and slang adaptation, or lighter-touch export localization without full story restructuring. Also use when the user provides a .docx script file for subtitle localization.
---

# Subtitle Export Localization

Subtitle-first scene-text localization workflow. Rewrite dialogue, narration, subtitle cards, and viewer-facing on-screen text so they read naturally to international audiences while preserving scene function, emotional temperature, and character dynamics.

## Scope

Use for: Chinese-to-English (or other target language) subtitle localization, bilingual scene-text sheets, narration and on-screen text localization, meme/slang/insult/flirtation/threat adaptation, soft export localization.

Do not use for: full market route selection, major story restructuring, production format decisions.

## Operating defaults

- Localize rather than translate literally. Preserve intent, subtext, power dynamic, and hook.
- Default to concise, subtitle-friendly English. Prefer lines a native English-speaking viewer would accept immediately.
- Keep Chinese source lines in output unless the user explicitly asks for English only.
- Treat platform, sponsor, and cross-cultural safety as part of localization quality.
- When the user does not specify a target language, default to English.
- When the user does not specify a risk posture, output three variants: conservative, balanced, and sharp.
- Only translate viewer-facing content. Strip all production-side material before translation.

## Content triage

Before translating anything, classify every line as viewer-facing or production-side. Only viewer-facing content goes into the translation pipeline. This step is mandatory — skipping it causes massive over-translation waste.

### Viewer-facing (TRANSLATE)

| Category | Chinese markers | Example |
|----------|----------------|---------|
| Dialogue | 角色名：/角色名（情绪）："台词" | 谢烈："老子不伺候了！" |
| Narration / voiceover | 旁白：/ 画外音 | 旁白：三年后，A市 |
| On-screen text cards | 【现况：...】/ 【字幕】 | 【已捕获S级供暖设备 x1】 |
| Episode titles | 第X集：标题 | 第三集：血契·三十天奴隶 |
| End-of-episode captions | 屏幕渐黑，字幕浮现 / （第X集完） | 【记忆可以抹去，但爱无法格式化。】 |

### Production-side (STRIP — do not translate)

| Category | Chinese markers | Example |
|----------|----------------|---------|
| Stage directions | △ 描述动作/表情/走位 | △ 她猛地睁开眼，泪水早已打湿了枕头。 |
| Scene headers | 场 X-Y 日/夜 内/外 地点 | 场 41-3 日 外 医务室 |
| Emotion/performance tags | （愤怒）/（颤抖）/（冷笑） | 谢烈（紧张）： |
| Camera directions | 镜头切换/特写/推拉 | △ 镜头切换到后厨 |
| BGM / SFX cues | BGM起/音效：/♪ | BGM：紧张配乐渐强 |
| Character bios | 角色设定/人物小传 | 林清越（女主）：冰冷策略型… |
| Story synopses | 剧情梗概/故事概述 | 故事概述：林清越误入清明大学… |

### Edge cases

- **Emotion tags inside dialogue attribution** (e.g., 谢烈（冷笑）："...") — strip the tag, translate only the quoted dialogue.
- **Stage directions containing viewer-visible text** (e.g., △ 屏幕浮现字幕："真相只有一个") — extract and translate only the quoted on-screen text.
- **Dual-function lines** — classify by primary viewer-facing function.

## Core localization rules

**Principle: translate function, not wording.** Preserve intent, emotional force, power dynamic, and scene utility. Do not preserve Chinese sentence structure, redundant emotional labeling, or culture-specific shorthand that confuses viewers.

### Common failure modes

1. **Translationese** — "You think you won?" / "This matter is not over." Fix: rewrite into native spoken English with shorter, sharper constructions.
2. **Overheated melodrama** — Chinese line is fun on the page but too theatrical in English. Fix: keep the energy but lower the verbal temperature; let rhythm and implication carry the threat or flirtation.
3. **Culture-locked slang** — net slang, fandom terms with no direct English equivalent. Fix: replace with an English-language social equivalent; if none exists, rewrite for scene effect.
4. **Exposition overload** — line explains more than a subtitle should. Fix: cut to the actionable emotional point.

### Character voice guardrails

| Archetype | Voice |
|-----------|-------|
| Cold strategist | clipped, precise, controlled |
| Arrogant fighter | blunt, hot-blooded, contemptuous |
| Rational enforcer | formal, exact, low-emotion |
| Possessive lover | intimate, invasive, emotionally loaded |
| Trickster / tease | playful, sharp, lightly ironic |

### Localization test

Approve the line only if: (1) a native English-speaking actor could say it naturally, (2) a subtitle reader could parse it instantly, (3) the line still sounds like that character, (4) narration and cards could appear on screen without sounding awkward.

### Subtitle mode defaults

- Prefer one short sentence over two medium ones.
- Avoid dense subordinate clauses. Let punchlines land fast.
- Remove filler words unless they define character voice.
- Narration should read like viewer-facing copy, not internal script notes.
- Scene cards and end tags should be sharp, compact, and platform-readable.

## Safety framework

Do not let localization accidentally intensify a scene into hate speech, religious contempt, political messaging, minor sexualization, coercive romance framed as aspirational, or abuse fetishization. When the original scene is dark, keep the darkness, but phrase it with control and awareness.

### Priority tiers

| Tier | Categories | Handling |
|------|-----------|----------|
| **CRITICAL** | 4 (Minors), 5 (Consent/coercion) | Must always provide a safer alternative. Never ship the risky version without explicit user override. |
| **HIGH** | 3 (Identity/race/gender), 6 (Abuse/self-harm) | Must flag and strongly recommend a safer alternative. User may choose to keep original phrasing. |
| **MEDIUM** | 1 (Politics), 2 (Religion), 7 (Platform/sponsor) | Must flag the risk. User decides whether to adjust. |

### Category 4: Minors and age ambiguity [CRITICAL]

If the cast is school-aged or age-ambiguous, avoid wording that intensifies sexual framing. Preserve tension, but do not make the subtitle more explicit than necessary. Sexual tension involving school settings where character age is unclear is high risk.

### Category 5: Consent, coercion, and domination [CRITICAL]

"Owner," "master," "obedience" in English escalate faster than in Chinese. Threats mixed with romance can read as abuse endorsement if phrased carelessly. Decide whether the scene function is survival, command, possession, or flirtation. Localize to the least inflammatory phrasing that still preserves the scene.

Example: "我是你的主人" may become:
- "Look at me. Stay with me."
- "You answer to me."
- "I'm the one keeping you alive."

Do not default to literal dominance language unless the user explicitly accepts the risk.

### Categories 1-3, 6-7

- **Politics/geopolitical [MEDIUM]**: stay inside the fictional conflict; do not make English more politically charged than the Chinese original.
- **Religion [MEDIUM]**: keep fictional cosmology fictional; prefer neutral supernatural wording over real-world sacred language.
- **Identity/race/gender [HIGH]**: keep insults personal, situational, or power-based rather than identity-based. No slurs.
- **Abuse/self-harm [HIGH]**: keep emotional stakes but strip wording that turns pain into fetish if not essential.
- **Platform/sponsor [MEDIUM]**: if a safer wording preserves the same story function, prefer it.

### Safety output

When a scene contains sensitivity, note: risk level, trigger area and category tier, whether the localized line is safe as written, and a safer alternative if needed. For CRITICAL-tier flags (Cat 4/5), a safer alternative is **mandatory**.

## Subtitle constraints

| Parameter | Limit |
|-----------|-------|
| Latin chars/line | 42 max (including spaces) |
| CJK chars/line | ~21 (each CJK = 2 Latin width) |
| Lines per subtitle block | 2 max |
| Reading speed | ~17 chars/sec (CPS) |
| Minimum display | 1 second |
| Maximum display | 7 seconds |

**Line breaks:** Break at semantic boundaries (clause breaks, conjunctions). Never split names, compound words, number+unit, or article+noun. Prefer breaking before conjunctions.

**Special markers:** ♪ for music, *italics* for inner monologue/off-screen voice, [SFX] for sound effects, (parentheses) for whispered delivery. CAPS sparingly for emphasis only.

## Workflow — 3 phases

### Phase 1: Triage and extract

When input is a raw script or .docx file, classify and filter content before translation using the Content Triage tables above.

For .docx input: run `scripts/extract_docx.py input.docx output.txt` if Python is available. If python-docx is not installed, use Python's built-in zipfile module to extract `word/document.xml`, parse `<w:t>` elements, and write plain text to a UTF-8 `.txt` file. Alternatively, run `scripts/triage.py extracted.txt` for auto-classification into JSONL.

For pre-structured input or just a few dialogue lines, abbreviate this phase — triage still applies but skip JSONL formatting.

Parse viewer-facing lines into structured records: ID, type (dialogue/narration/card), speaker, raw text, scene tag, emotion.

### Phase 2: Localize

For each viewer-facing line:
1. Identify text function (dialogue, narration, card, threat, flirtation, comedy, emotional escalation).
2. Diagnose why literal translation would fail and select adaptation strategy.
3. Rewrite into target-language subtitle-ready text.
4. Produce 3 variants (conservative / balanced / sharp) unless user requests otherwise.
5. Output bilingual comparison: Chinese source, text type, plain meaning gloss, localized line, and adjustment note.

For culture-locked references (marriage customs, internet slang, class markers, folk beliefs), read `references/culture-adaptation.md` and select a strategy: effect-equivalent swap, generalize, preserve + micro-gloss, or drop and rewrite.

For tone-sensitive scenes (threats, flirtation, memes, possessive lines), read `references/tone-mapping.md` for rewrite patterns.

For non-English targets, read `references/language-lanes.md` for language-specific pitfalls.

**Batch mode (10+ episodes):** Default to balanced version only for speed. Build a series glossary after Episode 1 (character names, proper nouns, catchphrases) and lock it. Write one-line character voice cards after Episode 1 and reference them for all subsequent episodes. Process one episode at a time; never merge episodes.

### Phase 3: Review and deliver

1. **Safety pass:** Check all rewritten lines against the Safety Framework above. For any line touching Categories 4 or 5, a safer alternative is mandatory.
2. **Subtitle pass:** Verify character limits (42 Latin / 21 CJK per line), reading speed (~17 CPS), and line break rules.
3. **QA self-check:**
   - Lines sound native, not translated
   - Narration and cards read as viewer-facing copy
   - Jokes, insults, threats land in the target language
   - Character voices remain distinct and consistent
   - No accidental tone inflation (cringe) or deflation (flat)
   - Critical safety categories have safer alternatives provided
   - Multi-version tradeoffs are easy to compare
   - Bilingual format intact
   - For multi-episode: glossary consistency verified across episodes
4. **Output format:** Markdown tables for ≤100 lines; Word document for 101+ (use `scripts/to_docx.py` if python-docx is available, otherwise output markdown).

## Output templates

### Bilingual dialogue sheet

| # | 文本类型 | 中文原句 | 字面意思 | 本地化英文 | 调整说明 |
|---|---|---|---|---|---|
| 1 | dialogue / narration / card | | | | |

### Multi-version dialogue sheet

| # | 文本类型 | 中文原句 | 字面意思 | Conservative | Balanced | Sharp | Risk note |
|---|---|---|---|---|---|---|---|
| 1 | dialogue / narration / card | | | | | | |

Version guide: Conservative = safest for broad platforms; Balanced = default recommendation, closest to original effect; Sharp = stronger edge, include risk note.

### Safety review snapshot

| # | 中文原句 | 当前英文 | 风险点 | 是否建议调整 | 更安全替代 |
|---|---|---|---|---|---|
| 1 | | | | 是/否 | |

## Intake

**Required:** At least one of: raw dialogue, narration, on-screen text, or scene excerpt.

**Optional:** Character notes or relationship map, target market or tone, target language (default: English), subtitle or dub mode, .docx file with script.

If input is insufficient to determine speaker relationships or emotional register, ask the user before guessing.

## References

The following files provide additional depth. Read them when the specific topic arises:

- `references/tone-mapping.md` — rewrite patterns for threats, flirtation, memes, possessive lines, narration cards
- `references/culture-adaptation.md` — adaptation strategies for culture-locked references (marriage customs, internet slang, class markers, folk beliefs)
- `references/language-lanes.md` — target-language guardrails for Spanish, Japanese, Korean, Thai, Indonesian, Vietnamese, Portuguese (Brazil)
- `templates/extract-sheet.md` — JSONL field specification for structured extraction
- `examples/e2e-yandere-dialogue.md` — worked example: possessive dialogue with safety pass
- `examples/e2e-narration-cards.md` — worked example: narration and on-screen text cards

## Response style

- Respond in the user's language unless asked otherwise.
- Keep analysis concise and actionable.
- When useful, separate: source issue, localized line, why it works, risk note.
