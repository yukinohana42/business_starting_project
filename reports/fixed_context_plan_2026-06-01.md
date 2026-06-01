# Fixed Context Plan 2026-06-01

## GPT固定情報源フォルダを作る目的

次回以降のChatGPTスレッドで、このプロジェクトの思想、設計、現状、次タスクを短時間で共有するために、重要ファイルだけをまとめた固定情報源フォルダを作ります。

対象フォルダ:

```text
docs/gpt-fixed-context-2026-06-01/
```

## 固定情報源に含めるべきファイル

- プロジェクト入口: `README.md`、`docs/project_overview.md`
- 思想の固定: `SOURCE_OF_TRUTH.md`
- 設計方針: `DESIGN.md`、`docs/educational_philosophy.md`
- AI作業ルール: `AGENTS.md`、`SKILLS.md`、`.agents/skills/*/SKILL.md`
- ChatGPT向け背景: `GPT_DOCUMENT.md`
- カリキュラム: `docs/workshop_curriculum_5_sessions.md`、`docs/workshop_curriculum_4_sessions.md`
- 親向け説明: `docs/parent_briefing.md`、`slides/parents/`
- 進行ガイド: `docs/facilitation_guide.md`
- 用語と安全性: `docs/terminology_for_junior_high.md`、`docs/safety_and_tone_guidelines.md`
- 教材索引: `slides/`、`cards/`、`worksheets/`、`prompts/`
- 現状と次タスク: `TODO.md`、今回の現状確認

## なぜそのファイルを含めるのか

ChatGPTが継続作業をするときに重要なのは、すべての成果物を読むことではなく、判断基準を持つことです。そのため、固定情報源には「思想」「設計」「現状」「次タスク」「教材の場所」を優先して入れます。

## 固定情報源に含めなくてよいファイル

- 出力済みPNG画像やPDFそのもの
- 生成ツールの実装コード
- 各セッションの細かい個別本文全文
- 画像化やPDF化の一時フォルダ

これらは必要になったときに参照すればよく、毎回ChatGPTに渡す固定文脈としては重すぎます。

## 次回ChatGPTに渡すときの使い方

まず `00_README_FOR_GPT.md` を読ませ、次に `02_SOURCE_OF_TRUTH.md`、`07_CURRICULUM_5_SESSIONS.md`、`17_CURRENT_STATUS_AND_NEXT_TASKS.md` を渡します。

詳細作業が必要になったら、対応する索引ファイルから元ファイルを開きます。

## 推奨プロンプト

```text
このフォルダは「中学2年生向け・家庭内起業ワークショップ準備プロジェクト」の固定情報源です。
まず 00_README_FOR_GPT.md、02_SOURCE_OF_TRUTH.md、07_CURRICULUM_5_SESSIONS.md、17_CURRENT_STATUS_AND_NEXT_TASKS.md を読んでください。
このプロジェクトでは、起業を押し付けず、誰かにとって価値あることを見つけ、小さく試す力を育てます。
以後の提案や教材制作では、SOURCE_OF_TRUTHを最優先で守ってください。
```

