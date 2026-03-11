# End-to-End Example: Narration Cards and On-Screen Text

This example walks through the full localization workflow for non-dialogue text: narration cards, episode title cards, hook cards, and on-screen text overlays.

## Input

**Scene context**: Female-lead manhua drama about a returning CEO protagonist. These are various cards and on-screen text from Episode 5. Target: English subtitles.

**Raw text items**:

```
1. [集标题卡] 第五集：她不是好惹的
2. [旁白卡] 三年前，她一无所有地离开。三年后，她带着整个帝国回来了。
3. [屏幕文字/弹幕风格叠字] 全场震惊.jpg
4. [反转提示卡] 你以为她是来求和的？
5. [集末钩子卡] 已解锁隐藏身份：幕后大Boss x1
6. [下集预告文字] 当她摘下面具的那一刻，所有人都沉默了……
```

---

## Step 0: Extract

```jsonl
{"id": "EP05_001", "type": "card", "speaker": null, "raw": "第五集：她不是好惹的", "scene": "集标题", "emotion": "霸气"}
{"id": "EP05_002", "type": "narration", "speaker": null, "raw": "三年前，她一无所有地离开。三年后，她带着整个帝国回来了。", "scene": "背景交代", "emotion": "大气/反转"}
{"id": "EP05_003", "type": "on-screen-text", "speaker": null, "raw": "全场震惊.jpg", "scene": "反应叠字", "emotion": "搞笑/夸张"}
{"id": "EP05_004", "type": "card", "speaker": null, "raw": "你以为她是来求和的？", "scene": "反转提示", "emotion": "挑衅/钩子"}
{"id": "EP05_005", "type": "card", "speaker": null, "raw": "已解锁隐藏身份：幕后大Boss x1", "scene": "集末钩子", "emotion": "反差萌/游戏感"}
{"id": "EP05_006", "type": "card", "speaker": null, "raw": "当她摘下面具的那一刻，所有人都沉默了……", "scene": "下集预告", "emotion": "悬念"}
```

---

## Step 1-3: Diagnosis

### Text function identification

| ID | Type | Function | Why literal translation fails |
|----|------|----------|------------------------------|
| 001 | Episode title | Sets tone and hooks viewer | "She is not easy to provoke" — stiff, loses swagger |
| 002 | Narration | Establishes time jump + power reversal | "She left with nothing" is OK but "brought the whole empire back" is melodramatic in English |
| 003 | On-screen meme text | Internet-coded audience reaction | ".jpg" is a Chinese internet format joke; direct translation is meaningless to global viewers |
| 004 | Hook card | Subverts viewer expectation | "You think she came to beg for peace?" — too wordy for a card |
| 005 | Achievement card | Game-UI styled punchline | "Unlocked hidden identity: behind-scenes big Boss x1" — inventory format is culture-locked |
| 006 | Next-episode teaser | Builds anticipation | "The moment she took off her mask, everyone went silent" — acceptable but can be punchier |

### Tone lane selection

- Card text should feel: **punchy, clicky, hook-oriented**
- Narration should feel: **cinematic, compact**
- On-screen meme text: **match social energy, not lexical meaning**
- Safety flags: **None** — low-risk content

---

## Step 4-6: Multi-Version Output

| # | 文本类型 | 中文原句 | Conservative | Balanced | Sharp |
|---|---------|---------|-------------|----------|-------|
| 001 | card | 第五集：她不是好惹的 | Episode 5: Don't Cross Her | Episode 5: She Bites Back | Episode 5: Wrong Woman to Mess With |
| 002 | narration | 三年前，她一无所有地离开。三年后，她带着整个帝国回来了。 | Three years ago, she left with nothing. Now she's back — and she brought an empire. | She left with nothing. She came back with everything. | Nothing when she left. An empire when she returned. |
| 003 | on-screen-text | 全场震惊.jpg | *everyone_shocked.gif* | *the room when she walked in* | *jaws on the floor rn* |
| 004 | card | 你以为她是来求和的？ | You thought she came to make peace? | Think she's here to play nice? | Cute. You think she's here to beg? |
| 005 | card | 已解锁隐藏身份：幕后大Boss x1 | Hidden identity unlocked: the real boss | Achievement unlocked: Secret Boss x1 | [NEW TITLE ACQUIRED] Final Boss x1 |
| 006 | card | 当她摘下面具的那一刻，所有人都沉默了…… | The moment the mask came off, the room went silent. | She dropped the mask. No one said a word. | Mask off. Dead silence. |

**Recommended version**: Balanced. Keeps hook energy without being too internet-coded for global audiences.

---

## Step 7: Safety Review

### Scene Risk Snapshot

- Risk level: **LOW**
- Primary triggers: None identified
- Safe for overseas subtitle: **Yes, all versions safe**

No Category 4 or 5 triggers. The "boss" language in line 005 is game-coded, not dominance-coded; no adjustment needed.

---

## Step 8: Final Subtitle Pass (Balanced version)

| # | Type | Final English subtitle | Char count | Lines |
|---|------|----------------------|-----------|-------|
| 001 | title card | Episode 5: She Bites Back | 26 | 1 |
| 002 | narration | She left with nothing. | 22 | 2 |
|     |           | She came back with everything. | 31 |   |
| 003 | on-screen | *the room when she walked in* | 30 | 1 |
| 004 | hook card | Think she's here to play nice? | 31 | 1 |
| 005 | end card | Achievement unlocked: Secret Boss x1 | 37 | 1 |
| 006 | teaser | She dropped the mask. No one said a word. | 42 | 1 |

All lines within 42-char limit. Cards are short and punchy for quick on-screen display.

### Key localization decisions

- **Line 002**: Split the time contrast into two short sentences instead of one long compound. More cinematic, easier to time.
- **Line 003**: Replaced `.jpg` meme format with English internet-native caption style. Preserved the "audience reaction overlay" energy.
- **Line 005**: Kept game-UI "achievement unlocked" format because it translates well to global internet culture. Added brackets in Sharp version for extra game-UI feel.
- **Line 006**: Compressed from 15 Chinese characters to 42 English characters while keeping the dramatic beat. Balanced version uses two short punches instead of one flowing sentence.
