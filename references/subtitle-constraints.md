# Subtitle Technical Constraints

Use this file to ensure localized output meets standard subtitle delivery requirements. These constraints apply during Step 8 (final subtitle pass) and should be checked via `templates/qa-checklist.md`.

## Character Limits

### Latin-script languages (English, Spanish, Portuguese, Indonesian, Vietnamese)

- Maximum **42 characters per line** (including spaces and punctuation)
- Maximum **2 lines** per subtitle block (84 characters total)
- Prefer single-line subtitles when the line fits

### CJK languages (Japanese, Korean)

- CJK characters occupy approximately **double the width** of Latin characters in most subtitle renderers
- Effective limit: **~21 CJK characters per line**
- Mixed CJK + Latin: count each CJK character as 2, each Latin character as 1

### Thai

- Thai script has no spaces between words; line length is measured by rendered width
- Approximate limit: **~35 Thai characters per line** (varies by font)

## Reading Speed

- Target: **~17 characters per second** (CPS) for comfortable reading
- Minimum display duration formula: `min_duration_sec = char_count / 17`
- For dense or emotionally loaded subtitles, allow slightly longer display time
- Never show a subtitle for less than **1 second**, even for very short lines
- Maximum display duration: **7 seconds** (re-split if longer)

| Chars | Min Duration |
|-------|-------------|
| 17 | 1.0 sec |
| 34 | 2.0 sec |
| 51 | 3.0 sec |
| 68 | 4.0 sec |
| 84 | 5.0 sec |

## Line Break Rules

- Break at **semantic boundaries**: clause breaks, conjunctions, prepositions
- Never split:
  - a person's name
  - a compound word or term
  - a number and its unit
  - an article and its noun (e.g., keep "the boss" on one line)
- Prefer breaking **before** conjunctions: put "and", "but", "because" at the start of the second line
- For questions, keep the question word and its verb together

### Examples

Good:
```
You think you can walk away
after everything you've done?
```

Bad:
```
You think you can walk away after
everything you've done?
```

## Special Markers

| Marker | Usage |
|--------|-------|
| ♪ ... ♪ | Music / song lyrics |
| *italics* | Inner monologue, off-screen voice (OS), or narration |
| [SFX] | Sound effects description (e.g., [door slams]) |
| (parentheses) | Whispered or sotto voce delivery |
| CAPS | Use sparingly for emphasis; never for full sentences |

## Bilingual Output Note

When producing bilingual (Chinese + target language) output for client review, these constraints apply to the **target-language line only**. The Chinese source line is for reference and does not need to meet subtitle length limits.
