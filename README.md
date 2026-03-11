# subtitle-export-localization

> Subtitle-first export localization skill for Chinese dialogue, narration, and on-screen text.

## 导览 / Overview

- 中文说明见下方 `中文`
- English documentation starts at `English`
- 核心目录：`SKILL.md`、`agents/`、`references/`、`templates/`

## 中文

这是一个面向 Codex 的字幕出海本地化 skill，专门用于把中文剧情对白、旁白和屏幕文字处理成更适合海外观众接受的字幕版本。

它不做大纲级重构，也不负责完整的市场路线判断，而是聚焦在“台词怎么翻得更像本地人会说的话，同时又尽量保留原意和张力”。

### 这个 skill 主要解决什么问题

- 中文台词、旁白和字幕卡直译后容易出现翻译腔
- 一些网感梗、羞辱、威胁、暧昧、病娇感台词，直接翻成英文或其他语言会显得尴尬、过火，或者踩线
- 同一句台词在不同平台、不同市场，需要不同风险等级的版本
- 出海字幕不只是翻译，还要考虑政治、宗教、身份、未成年、强迫关系等敏感问题

### 它会做什么

- 输出中外文对照的场景文本本地化版本，包括对白、旁白和屏幕文字
- 默认提供三档版本：
  - `Conservative`：更安全，适合广泛平台和 sponsor 敏感场景
  - `Balanced`：默认推荐，尽量保留原台词的戏剧效果
  - `Sharp`：张力更强，但会附带风险提示
- 支持多语言分路，包括：
  - English
  - Spanish
  - Japanese
  - Korean
  - Thai
  - Indonesian
  - Vietnamese
  - Portuguese (Brazil)
- 对高风险台词做额外的出海安全审查

### 仓库结构

- `SKILL.md`
  skill 主说明，定义使用场景、工作流和输出方式
- `agents/openai.yaml`
  给 Codex / UI 使用的元信息
- `references/`
  本地化规则、语气映射、语言分路、出海红线审查规则
- `templates/`
  中外文对照、多版本对照、安全审查的输出模板

### 适合的使用场景

- 中文短剧、漫剧、网文改编剧的字幕出海，包括对白和旁白卡点文案
- 女频、怪谈、悬疑、病娇、强设定类对白本地化
- 想保留原作味道，但又不希望海外字幕显得生硬或翻车
- 希望同一句台词一次产出多个风险等级版本，方便选择

### 不适合的使用场景

- 完整剧本结构改编
- 海外发行市场路线选择
- 制作方式决策
- 单纯逐字直译

### 安装方式

#### Codex

```bash
git clone https://github.com/DavidH-Creation/subtitle-export-localization.git ~/.codex/skills/subtitle-export-localization
```

#### Claude Code

```bash
git clone https://github.com/DavidH-Creation/subtitle-export-localization.git ~/.claude/skills/subtitle-export-localization
```

也可以按你的工作流把这个 skill 复制到本地 skills 目录中使用。

---

## English

This is a Codex skill for subtitle-led export localization, designed to turn Chinese scripted dialogue, narration, and on-screen text into subtitle versions that feel more acceptable and natural to overseas audiences.

It does not do outline-level restructuring or full market-route planning. Instead, it focuses on how to rewrite lines so they sound like something a native speaker would actually say, while preserving the original intent and dramatic force as much as possible.

### What problem this skill solves

- Literal translation of Chinese dialogue, narration, and subtitle cards often sounds unnatural
- Some internet-coded jokes, humiliation, threats, flirtation, and yandere-style lines can become awkward, over-the-top, or risky when translated directly
- The same line may need different risk levels for different platforms and markets
- Subtitle export is not just translation; it also needs to account for political, religious, identity, minor-related, and coercion-sensitive issues

### What it does

- Produces bilingual scene-text localization output for dialogue, narration, and on-screen text
- Provides three default versions:
  - `Conservative`: safer for broader platforms and sponsor-sensitive contexts
  - `Balanced`: the default recommendation, preserving the original dramatic effect as much as possible
  - `Sharp`: stronger in edge and tension, with an attached risk note
- Supports multiple language lanes, including:
  - English
  - Spanish
  - Japanese
  - Korean
  - Thai
  - Indonesian
  - Vietnamese
  - Portuguese (Brazil)
- Adds an extra export-safety review for high-risk lines

### Repository Structure

- `SKILL.md`
  Main skill instructions defining the use cases, workflow, and output shape
- `agents/openai.yaml`
  Metadata used by Codex / UI
- `references/`
  Localization rules, tone mapping, language lanes, and export safety review rules
- `templates/`
  Output templates for bilingual comparison, multi-version comparison, and safety review

### Best fit use cases

- Subtitle export for Chinese short dramas, manhua dramas, and web-novel adaptations, including dialogue and narration-card text
- Dialogue localization for female-targeted, horror, suspense, yandere, and strong-concept material
- Cases where you want to preserve the original flavor without making the overseas subtitles feel stiff or embarrassing
- Cases where you want multiple risk-tiered versions of the same line for easier selection

### Not a fit for

- Full script structure adaptation
- Overseas release market-route selection
- Production-format decisions
- Pure word-for-word translation

### Installation

#### Codex

```bash
git clone https://github.com/DavidH-Creation/subtitle-export-localization.git ~/.codex/skills/subtitle-export-localization
```

#### Claude Code

```bash
git clone https://github.com/DavidH-Creation/subtitle-export-localization.git ~/.claude/skills/subtitle-export-localization
```

You can also copy this skill into your local skills directory using your preferred workflow.
