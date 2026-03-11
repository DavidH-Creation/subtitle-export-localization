# End-to-End Example: Yandere Confrontation Dialogue

This example walks through the full localization workflow for a female-targeted possessive/yandere confrontation scene.

## Input

**Scene context**: Female-lead short drama, Episode 3. Male lead confronts female lead who tried to leave. He is possessive, cold, controlling. She is defiant but trapped. The scene is tense, not romantic. Target: English subtitles.

**Raw script excerpt**:

```
【场景：豪宅客厅，夜。男主挡在门口，女主拎着行李箱。】

男主：你想去哪？
女主：跟你没关系。
男主：你是我的人，你哪儿也去不了。
女主：我不是你的附属品。
男主：（靠近，低声）听话，把东西放下。
女主：你越这样，我越想走。
男主：（捏住她下巴）走？你走得了吗。

【旁白卡：第一次，她在他眼里看到了裂痕。】
```

---

## Step 0: Extract

```jsonl
{"id": "S01E03_001", "type": "dialogue", "speaker": "男主", "raw": "你想去哪？", "scene": "对峙/控制", "relationship": "男主→女主", "emotion": "冷压迫", "prev_line": "女主拎行李箱准备离开"}
{"id": "S01E03_002", "type": "dialogue", "speaker": "女主", "raw": "跟你没关系。", "scene": "对峙/控制", "relationship": "女主→男主", "emotion": "冷硬反抗", "prev_line": "男主质问去哪"}
{"id": "S01E03_003", "type": "dialogue", "speaker": "男主", "raw": "你是我的人，你哪儿也去不了。", "scene": "对峙/控制", "relationship": "男主→女主", "emotion": "占有/威胁", "prev_line": "女主拒绝回答"}
{"id": "S01E03_004", "type": "dialogue", "speaker": "女主", "raw": "我不是你的附属品。", "scene": "对峙/控制", "relationship": "女主→男主", "emotion": "愤怒反击", "prev_line": "男主宣称占有"}
{"id": "S01E03_005", "type": "dialogue", "speaker": "男主", "raw": "听话，把东西放下。", "scene": "对峙/控制", "relationship": "男主→女主", "emotion": "低声胁迫", "prev_line": "女主拒绝被定义"}
{"id": "S01E03_006", "type": "dialogue", "speaker": "女主", "raw": "你越这样，我越想走。", "scene": "对峙/控制", "relationship": "女主→男主", "emotion": "倔强", "prev_line": "男主命令放下行李"}
{"id": "S01E03_007", "type": "dialogue", "speaker": "男主", "raw": "走？你走得了吗。", "scene": "对峙/控制", "relationship": "男主→女主", "emotion": "冷威胁", "prev_line": "女主声明要离开"}
{"id": "S01E03_008", "type": "card", "speaker": null, "raw": "第一次，她在他眼里看到了裂痕。", "scene": "情感转折卡", "emotion": "微妙/脆弱"}
```

---

## Step 1-3: Diagnosis

### Text function identification

| ID | Function | Why literal translation fails |
|----|----------|------------------------------|
| 003 | Possessive declaration | "You are my person, you can't go anywhere" — stilted, cringe in English |
| 004 | Defiant pushback | "I am not your accessory" — sounds like a feminist slogan, too on-the-nose |
| 005 | Coercive command | "Be obedient, put things down" — too literal, loses the sinister intimacy |
| 007 | Cold threat | "Leave? Can you leave?" — grammatically odd, loses menace |
| 008 | Emotional turn card | "For the first time, she saw cracks in his eyes" — reads like a novel, not a subtitle |

### Tone lane selection

- Scene function: **power struggle with vulnerability underneath**
- Tone: cold tension, not romantic; the possessiveness should feel unsettling, not aspirational
- Safety flags: **Category 5 [CRITICAL]** — consent/coercion/domination language

---

## Step 4-6: Multi-Version Output

| # | 文本类型 | 中文原句 | Conservative | Balanced | Sharp | Risk note |
|---|---------|---------|-------------|----------|-------|-----------|
| 001 | dialogue | 你想去哪？ | Where do you think you're going? | Where do you think you're going? | Going somewhere? | — |
| 002 | dialogue | 跟你没关系。 | That's none of your business. | None of your business. | Not your concern. | — |
| 003 | dialogue | 你是我的人，你哪儿也去不了。 | You're not leaving. Not tonight. | You're staying. That's not a question. | You belong here. You're not going anywhere. | Cat 5: "belong" + trapped framing. Sharp version intensifies possession. |
| 004 | dialogue | 我不是你的附属品。 | I'm not something you own. | I don't belong to you. | I'm not your thing. | — |
| 005 | dialogue | 听话，把东西放下。 | Put that down. Stay. | Put it down. Be smart about this. | Put. It. Down. | Conservative removes coercive "be obedient" entirely. Sharp uses rhythm for menace. |
| 006 | dialogue | 你越这样，我越想走。 | The more you do this, the more I want to leave. | Every time you do this, I want to leave more. | Keep going. See if that makes me stay. | Sharp gives her more bite. |
| 007 | dialogue | 走？你走得了吗。 | You think you can just walk away? | Walk away? Try it. | Leave? (scoffs) You won't make it to the door. | Cat 5: Sharp version escalates physical threat implication. |
| 008 | card | 第一次，她在他眼里看到了裂痕。 | For the first time — a crack in his composure. | Something cracked behind his eyes. | She saw it. The first fracture. | — |

**Recommended version**: Balanced. Preserves dramatic tension while avoiding gratuitous dominance framing.

---

## Step 7: Safety Review

### Scene Risk Snapshot

- Risk level: **HIGH** (touches CRITICAL Category 5)
- Primary trigger: consent/coercion — male lead physically blocks exit and uses possessive language
- Safe for overseas subtitle: **Balanced and Conservative versions are safe.** Sharp version requires user acknowledgment.

### Line Risks

| # | 中文原句 | Risk | Category | Tier | Safe? | Safer alternative |
|---|---------|------|----------|------|-------|-------------------|
| 003 | 你是我的人，你哪儿也去不了。 | Possessive + trapped | 5 | CRITICAL | Conservative/Balanced: Yes. Sharp: No — "belong" intensifies. | Use Balanced: "You're staying. That's not a question." |
| 005 | 听话，把东西放下。 | Coercive command | 5 | CRITICAL | Conservative: Yes. Sharp: borderline — rhythm conveys menace without explicit coercion. | Keep Sharp as-is; menace is in delivery, not wording. |
| 007 | 走？你走得了吗。 | Physical threat implication | 5 | CRITICAL | Conservative/Balanced: Yes. Sharp: No — "won't make it to the door" implies physical restraint. | Use Balanced: "Walk away? Try it." |

---

## Step 8: Final Subtitle Pass (Balanced version)

| # | Final English subtitle | Char count | Lines | CPS @2.5s |
|---|----------------------|-----------|-------|-----------|
| 001 | Where do you think you're going? | 33 | 1 | 13.2 |
| 002 | None of your business. | 22 | 1 | 8.8 |
| 003 | You're staying. That's not a question. | 38 | 1 | 15.2 |
| 004 | I don't belong to you. | 22 | 1 | 8.8 |
| 005 | Put it down. Be smart about this. | 33 | 1 | 13.2 |
| 006 | Every time you do this, | 23 | 2 | 15.2 |
|     | I want to leave more. | 21 |   |       |
| 007 | Walk away? Try it. | 18 | 1 | 7.2 |
| 008 | Something cracked behind his eyes. | 35 | 1 | 14.0 |

All lines within 42-char/line limit. All CPS within 17 chars/sec target.
