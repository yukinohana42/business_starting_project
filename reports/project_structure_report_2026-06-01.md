# Project Structure Report 2026-06-01

## 現在の状態

- project root: `junior-entrepreneurship-workshop/`
- git branch: Gitリポジトリではないため取得不可
- HEAD: Gitリポジトリではないため取得不可
- worktree status: Gitリポジトリではないため取得不可

## トップレベル構成

```text
junior-entrepreneurship-workshop/
  .agents/
  assets/
  cards/
  docs/
  output/
  prompts/
  reports/
  sessions/
  slides/
  tools/
  worksheets/
  AGENTS.md
  CHANGELOG.md
  DESIGN.md
  GPT_DOCUMENT.md
  README.md
  SKILLS.md
  SOURCE_OF_TRUTH.md
  TODO.md
```

## 各トップレベルフォルダの役割

- `.agents/`: CodexやAIエージェントが守る作業スキル定義。
- `assets/`: 見た目、色、アイコン、比喩表現の方針。
- `cards/`: 印刷して使うカード教材案。
- `docs/`: 教育方針、カリキュラム、親向け説明、進行ガイド。
- `output/`: PDF、HTML、PNGなどの出力物。
- `prompts/`: 今後ChatGPTやCodexに作業依頼するときのプロンプト。
- `reports/`: 現状報告と固定情報源設計の報告。
- `sessions/`: Day1からDay5までの個別進行台本とワーク。
- `slides/`: 子供向け、親向けのMarkdownスライド原稿。
- `tools/`: PNG画像生成など、出力物作成用の補助スクリプト。
- `worksheets/`: 子供が記入するワークシート案。

## 主要Markdownファイルの役割

- `README.md`: プロジェクト入口。読む順番と全体像。
- `AGENTS.md`: CodexやAIが守る作業ルール。正式名称は `AGENTS.md`。
- `DESIGN.md`: 教育設計、スライド、カード、ワークシート、親向け資料の設計方針。
- `SOURCE_OF_TRUTH.md`: このプロジェクトで絶対にぶらさない思想。正式名称は `SOURCE_OF_TRUTH.md`。
- `GPT_DOCUMENT.md`: ChatGPTに背景を渡すための文脈文書。
- `SKILLS.md`: `.agents/skills/` にあるスキルの一覧。
- `TODO.md`: 次に改善すべきタスク。
- `CHANGELOG.md`: 作成・更新履歴。

## セッション別フォルダ

```text
sessions/
  session_01_value_work/
  session_02_finding_value/
  session_03_idea_creation/
  session_04_pmf/
  session_05_pitch/
```

各セッションには、主に次のファイルがあります。

- `README.md`: 回の目的、使うもの、ゴール。
- `facilitator_script.md`: 親が進行するときの台本。
- `slide_outline.md`: スライドの構成案。
- `worksheet.md`: その回で使う記入シート。
- `cards.md`: その回で使うカード案。
- `reflection.md`: 実施後の振り返り。

一部の回には追加で `interview_homework.md`、`experiment_plan.md`、`pitch_sheet.md`、`parent_judge_sheet.md` があります。

## スライド、カード、ワークシート、プロンプト、Skillの配置

- 子供向けスライド: `slides/kids/session_01_value_work.md` から `session_05_pitch.md`
- 親向けスライド: `slides/parents/`
- 親向けインフォグラフィック原稿: `slides/parents/parent_infographic_6_pages.md`
- カード教材: `cards/value_cards.md`、`problem_cards.md`、`customer_cards.md`、`idea_cards.md`、`pmf_signal_cards.md`、`pitch_prompt_cards.md`
- ワークシート: `worksheets/business_idea_sheet.md`、`interview_sheet.md`、`pmf_check_sheet.md`、`mini_experiment_sheet.md`、`pitch_sheet.md`、`reflection_sheet.md`
- プロンプト: `prompts/`
- Skill: `.agents/skills/workshop-designer/` など5種類

## 出力物

- `output/parent_infographic_6_pages.html`: 6枚構成の親向けHTML。
- `output/parent_infographic_pdf_final/`: PDF版。PDF化では文字化けリスクあり。
- `output/parent_infographic_images_day1_5/`: Day1からDay5までのPNG画像版。文字化け回避用として現在はこちらが実用的。

## 今後どこを編集すればよいか

- 教育思想を変える場合: `SOURCE_OF_TRUTH.md` と `docs/gpt-fixed-context-2026-06-01/02_SOURCE_OF_TRUTH.md`
- 各回の中身を直す場合: `sessions/session_XX_*/`
- 子供向けスライドを直す場合: `slides/kids/`
- 親向け説明を直す場合: `docs/parent_briefing.md` と `slides/parents/`
- カードを印刷可能にする場合: `cards/`
- ワークシートを印刷可能にする場合: `worksheets/`
- 次のAI作業を設計する場合: `prompts/` と `docs/gpt-fixed-context-2026-06-01/`

