---
name: subtitle-export-localization
description: Localize Chinese drama, manhua-drama, and short-form scripted dialogue, narration, and on-screen text for subtitle-led overseas release. Use when the user wants bilingual scene rewrites, subtitle-ready dialogue, narration localization, meme and slang adaptation, or lighter-touch export localization without full story restructuring.
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

Accept any subset of:
- raw dialogue
- narration
- on-screen text
- scene excerpt
- episode pages
- character notes
- target market or tone target
- target language
- subtitle mode or dub mode

If the user gives only a scene and no market, default to globally legible English for subtitle-led export.

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
- Read [`references/export-safety-red-lines.md`](references/export-safety-red-lines.md) when the scene contains sensitive power dynamics, religion, politics, identity language, minors, coercion, or taboo content.
- Use [`templates/bilingual-dialogue-sheet.md`](templates/bilingual-dialogue-sheet.md) for line-by-line output.
- Use [`templates/scene-pass-summary.md`](templates/scene-pass-summary.md) when the user wants a quick assessment before rewriting.
- Use [`templates/safety-review.md`](templates/safety-review.md) when the user wants a risk pass or when the scene is obviously sensitive.
- Use [`templates/multi-version-dialogue-sheet.md`](templates/multi-version-dialogue-sheet.md) when the user wants version selection or language selection.

## Workflow

1. Identify the text function.
   Decide whether each line is dialogue, narration, subtitle card, exposition, threat, flirtation, humiliation, comedy, or emotional escalation.
2. Diagnose why literal translation would fail.
   Flag stiffness, culture-locked wording, over-explaining, meme mismatch, or melodrama that will sound awkward in English.
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
