---
name: subtitle-export-localization
version: 0.1.0
description: Localize Chinese drama, manhua-drama, and scripted dialogue, narration, and on-screen text — from a single scene to a full multi-episode series — for subtitle-led overseas release. Use when the user wants bilingual scene rewrites, subtitle-ready dialogue, narration localization, meme and slang adaptation, or lighter-touch export localization without full story restructuring. Also use when the user provides a .docx script file for subtitle localization.
---

# Subtitle Export Localization

Treat this skill as a subtitle-first scene-text localization workflow. Rewrite dialogue, narration, subtitle cards, and viewer-facing on-screen text so they read naturally to international audiences while preserving scene function, emotional temperature, and character dynamics.

## Scope

Use this skill for:
- Chinese-to-English subtitle localization
- Chinese-English bilingual scene-text sheets
- narration and on-screen text localization
- Meme, slang, insult, flirtation, and threat adaptation
- Soft export localization when the user does not want a full adaptation package

Do not use this skill for:
- full market route selection
- major story restructuring
- production format decisions

## Operating defaults

- Localize rather than translate literally.
- Preserve intent, subtext, power dynamic, and hook.
- Default to concise, subtitle-friendly English.
- Prefer lines a native English-speaking viewer would accept immediately.
- Keep Chinese source lines in the output unless the user explicitly asks for English only.
- Treat platform, sponsor, and cross-cultural safety as part of localization quality, not a separate afterthought.
- When the user does not specify a target language, ask or default to English.
- When the user does not specify a risk posture, output three variants: conservative, balanced, and sharp.

## Intake

### Minimum required input

- At least one of: raw dialogue, narration, on-screen text, or scene excerpt

### Optional enrichment

- character notes or relationship map
- target market or tone target
- target language (default: English)
- subtitle mode or dub mode
- episode pages or broader context
- .docx file (Word document) containing script or screenplay

If the user gives only a scene and no market, default to globally legible English for subtitle-led export.
If the input is insufficient to determine speaker relationships or emotional register, ask the user before guessing.

## Supported default language lanes

Offer these lanes first unless the user requests another language:

- English
- Spanish
- Japanese
- Korean
- Thai
- Indonesian
- Vietnamese
- Portuguese (Brazil)

Use the user's requested language if it is outside this list. Keep the same localization principles, but adapt the examples and register to that language.

## Load only what is needed

- Read [`references/localization-rules.md`](references/localization-rules.md) for core rewrite rules for dialogue, narration, and subtitle cards.
- Read [`references/tone-mapping.md`](references/tone-mapping.md) when the scene depends on flirting, threats, meme language, or stylized banter.
- Read [`references/language-lanes.md`](references/language-lanes.md) when the user wants Spanish, Japanese, Korean, Thai, Indonesian, Vietnamese, Portuguese (Brazil), or multi-language comparison.
- Read [`references/culture-adaptation.md`](references/culture-adaptation.md) when the scene contains culture-locked references (marriage customs, internet slang, class markers, folk beliefs, etc.) that need adaptation for international viewers.
- Read [`references/export-safety-red-lines.md`](references/export-safety-red-lines.md) when the scene contains sensitive power dynamics, religion, politics, identity language, minors, coercion, or taboo content.
- Use [`templates/bilingual-dialogue-sheet.md`](templates/bilingual-dialogue-sheet.md) for line-by-line output.
- Use [`templates/scene-pass-summary.md`](templates/scene-pass-summary.md) when the user wants a quick assessment before rewriting.
- Use [`templates/safety-review.md`](templates/safety-review.md) when the user wants a risk pass or when the scene is obviously sensitive.
- Use [`templates/multi-version-dialogue-sheet.md`](templates/multi-version-dialogue-sheet.md) when the user wants version selection or language selection.
- Use [`templates/extract-sheet.md`](templates/extract-sheet.md) when preprocessing raw scripts into structured JSONL before localization.
- Use [`templates/qa-checklist.md`](templates/qa-checklist.md) for final quality assurance self-check.
- Read [`references/subtitle-constraints.md`](references/subtitle-constraints.md) for character limits, reading speed, and line break rules.

## Workflow

0. Extract translatable text (when working from raw scripts).
   Parse the raw script into structured JSONL using [`templates/extract-sheet.md`](templates/extract-sheet.md).
   Each line gets: ID, type classification, speaker, raw text, scene tag, relationship, emotion, and previous-line context.
   This reduces token cost for subsequent steps and provides consistent line tracking.
   Use a lightweight model for this step when possible.
   If the user provides pre-structured input or only a few lines, skip this step.
1. Identify the text function.
   Decide whether each line is dialogue, narration, subtitle card, exposition, threat, flirtation, humiliation, comedy, or emotional escalation.
2. Diagnose why literal translation would fail.
   Flag stiffness, culture-locked wording, over-explaining, meme mismatch, or melodrama that will sound awkward in English.
   For culture-locked references, select an adaptation strategy from [`references/culture-adaptation.md`](references/culture-adaptation.md): effect-equivalent swap, generalize, preserve + micro-gloss, or drop and rewrite.
3. Select the target language and tone lane.
   Decide whether the line should feel safer, balanced, or sharper in the target market.
4. Rewrite into export-legible target-language scene text.
   Keep dialogue actable, narration readable, and on-screen text concise.
5. Produce variant choices.
   By default, provide:
   - conservative: safer for broad platforms and sponsors
   - balanced: default recommendation, closest to original effect
   - sharp: stronger edge, but include a risk note
6. Output bilingual comparison.
   Show the Chinese source, text type, a plain meaning gloss when useful, the localized target-language line, and a short note on why it works.
7. Do a safety pass.
   Check the rewritten lines against [`references/export-safety-red-lines.md`](references/export-safety-red-lines.md).
8. Do a final subtitle pass.
   Trim lines that read too long, too on-the-nose, or too translated.

## Output modes

- Quick diagnosis: use [`templates/scene-pass-summary.md`](templates/scene-pass-summary.md)
- Line-by-line bilingual localization: use [`templates/bilingual-dialogue-sheet.md`](templates/bilingual-dialogue-sheet.md)
- Sensitive-content review: use [`templates/safety-review.md`](templates/safety-review.md)
- Multi-version localization choice: use [`templates/multi-version-dialogue-sheet.md`](templates/multi-version-dialogue-sheet.md)
- Raw script extraction: use [`templates/extract-sheet.md`](templates/extract-sheet.md)
- QA self-check: use [`templates/qa-checklist.md`](templates/qa-checklist.md)
- Full-series or multi-episode delivery: when output is too large for chat (50+ episodes, 2000+ lines), route final output through the docx skill to produce a Word document. See [`templates/extract-sheet.md`](templates/extract-sheet.md) for batch processing and glossary tracking guidance.

## Quality bar

Before finalizing, check that:

- the English line sounds native rather than translated
- narration and on-screen text read naturally for viewers, not like production notes
- the line length is subtitle-friendly
- the joke, insult, tease, or threat lands in English
- the character voice still feels distinct
- the scene is not accidentally toned up into cringe or toned down into flatness
- the scene does not casually cross obvious export red lines that could trigger platform, sponsor, or audience backlash
- when multiple versions are provided, the tradeoff between conservative, balanced, and sharp is easy for the user to compare

## Response style

- Respond in the user's language unless asked otherwise.
- Keep analysis concise and actionable.
- When useful, separate:
  - source issue
  - localized line
  - why it works
  - risk note
