# TODO

## Current Next Task: Day1 v3 Prototype Review

- 人間が `outputs/day1/rendered/session_01_infographic_16x9_v3_prototype_contact_sheet.png` を確認する。
- 方向性がOKなら、Day1 v3正式版6ページの16:9 HTML/CSSへ進む。
- 正式版6ページの16:9 PNG確認後に、4:5展開へ進む。
- v3構成が確定してから、台本・カード・ワークシートへ反映する。
- 最後に固定情報源をMarkdown中心で更新する。PNG/HTML/CSS本体は固定情報源フォルダへコピーしない。

## Current Next Task: Image-First Visual Workflow

- `docs/image_first_visual_production_workflow.md` と `docs/global_visual_system_spec.md` を人間確認する。
- Day1 pilotとして、まずPage 1 Mission Boardだけ画像生成を小さく試すか判断する。
- pilot生成する場合は `outputs/day1/prompts/day1_visual_anchor_prompt.md`、`day1_character_prompt.md`、`day1_page_prompts.md` を使う。
- 生成後はcontact sheetではなく、まず1枚レビューで発見ゲーム型画面に見えるか確認する。
- OKならDay1残り5ページへ進む。NGならpromptと画面タイプ定義に戻る。

## Current Next Task: Day1 Image Review And Refinement

- Day1 Page 1 direction sampleを基準にする。
- ただしfinal化にはvisual review and refinementが必要。
- Page 2 final prompt `outputs/day1/prompts/day1_page_02_image_generation_prompt_final.md` を人間確認する。
- Page 2を1枚だけ画像生成する。
- candidate画像をレビューする。
- 意味不明な描写があれば修正プロンプトで再生成する。
- final判定後に次ページへ進む。
- Day1 6枚が揃うまでは4:5展開しない。
- final採用前に後載せ文字範囲を決める。

## Current Next Task: Day1 16:9 Image Completion

- Page 1 / Page 2 candidate画像をrepo内に配置し、finalレビューする。
- Page 3 candidate生成を1枚だけ行う。
- Page 3 visual reviewを行う。
- Page 4 candidate生成を1枚だけ行う。
- Page 4 visual reviewを行う。
- Page 5 candidate生成を1枚だけ行う。
- Page 5 visual reviewを行う。
- Page 6 candidate生成を1枚だけ行う。
- Page 6 visual reviewを行う。
- Day1 16:9 final 6枚を確定する。
- その後に4:5展開へ進む。
- その後に台本・カード・ワークシートへ反映する。

## Priority 1

- GPT固定情報源フォルダ `docs/gpt-fixed-context-2026-06-01-visual-system-v2/` の内容を最終確認する
- PR `docs/gamified-visual-foundation-v1` を作成し、docs中心・PNG再生成なし・既存IP模倣なしを明記する
- Day1 v2 PNG/contact sheetは採用版にしない前提で人間確認する
- Day1 v3制作前に `outputs/day1/session_01_infographic_v3_design_brief.md` と `session_01_infographic_v3_storyboard.md` を人間確認する
- Day1 v3のHTML/CSS/PNG生成前に、キャラクター行動・ゲーム要素・子供の行動・相手の変化・合格基準表を確認する
- Day2以降のvisual design briefを人間確認する
- 親向け資料は `docs/parent_material_design_principles_v2.md` に沿って再設計する
- 合格後にDay1 v3 HTML/CSSへ進む
- Day1 v3確認後に4:5版へ展開する

## Priority 2

- v3構成をDay1台本、カード、ワークシートへ反映
- Day2 Problem HunterのMission Board / Observation Map案を作る
- 全体クエストマップ、Discovery Stamp、Learning Badgeを学びの行動記録として設計する

## Priority 3

- PR merge後に `docs/current_git_status.md` と固定情報源のHEAD情報を更新
- Day2以降のHTML/CSS/PNG生成
- 親向け説明資料、カード、ワークシートのv2合格基準レビュー
- バッジ・スタンプ・進捗表のデザイン統一

## 既存の改善候補

- 各スライドを実際に見せる想定で、文字量をさらに減らす
- ワークシートをA4印刷用に整える
- カードをA4で切りやすい配置に変換する
- 子供たちの興味に合わせて、ゲーム、部活、スマホ、勉強の例を増やす
- 30分版、45分版、60分版の進行時間を各セッションで明確に分ける
- 第3回と第4回を統合した4回版の台本を詳しく作る
- 実施後の振り返りメモをもとに、問いの言い方を修正する
- 親向け説明スライドをPowerPointやPDFに変換する
- 子供向けスライドをMarpで表示確認する
- 親御さん向け6枚インフォグラフィックを実際に印刷し、文字量と余白を確認する
- `output/parent_infographic_6_pages.html` をPDF化して共有用ファイルにする
- 第1回Zoom実施パッケージ `outputs/day1/` を実際に画面共有で確認する
- 第1回Zoom共有用PNG 6枚を実際にZoomで表示し、文字サイズとページ切り替えを確認する
- 第1回4:5試作PNGをスマホで確認し、必要なら余白と改行を調整する
- 第1回実施後に `outputs/day1/session_01_after_action_review.md` へ反応を記録する
- 第2回のZoom実施パッケージを作る

## Codexへ次に依頼するとよいタスク

- `slides/kids` の各MarkdownをMarp形式に整えてください
- `cards` のカードをA4印刷用Markdownに整えてください
- `worksheets` の各シートを記入欄つきの印刷用レイアウトにしてください
- 第1回を実際に45分で進めるための詳細台本にしてください
- 実施後メモを読み、次回改善案を `TODO.md` に反映してください
