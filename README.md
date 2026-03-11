# subtitle-export-localization

A Codex skill for subtitle-led export localization of Chinese scripted dialogue.

It focuses on:

- bilingual source-to-target dialogue sheets
- conservative / balanced / sharp variant output
- subtitle-friendly localization rather than literal translation
- cross-market safety review for political, religious, identity, coercion, and other export-sensitive lines
- multiple language lanes including English, Spanish, Japanese, Korean, Thai, Indonesian, Vietnamese, and Portuguese (Brazil)

## Structure

- `SKILL.md`: main skill instructions
- `agents/openai.yaml`: UI metadata
- `references/`: localization rules, tone mapping, language lanes, and safety red lines
- `templates/`: bilingual, multi-version, and safety review output templates

## Install

Copy this skill into your Codex skills directory, or install it from GitHub with your preferred workflow.
