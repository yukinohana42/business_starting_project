# TODO

## Current Next Task: Manual GPT Image Handoff

Day1の画像制作は、Codexが画像生成するのではなく、ユーザーがGPT画像生成へprompt packetを貼るmanual handoff modeで進める。

最初に人間確認する:

- `outputs/day1/image_generation/prompt_packets/README.md`
- `outputs/day1/image_generation/user_handoff_template.md`
- `outputs/parents/parent_explanation_material_plan.md`

## Day1 Prompt Packet Handoff

- Page1からPage6まで、prompt packetを人間が順番にGPT画像生成へ貼る。
- Page1 / Page2の既存方向性画像がある場合は、repoへcandidateとして配置する。
- Page1 / Page2の既存画像を配置できない場合は、Page1から再生成する。
- Page3 candidateを1枚だけ生成する。
- Page4 candidateを1枚だけ生成する。
- Page5 candidateを1枚だけ生成する。
- Page6 candidateを1枚だけ生成する。
- 各candidateを `outputs/day1/image_generation/user_handoff_template.md` でCodexへ戻す。
- 各candidateをCodexでレビューする。Codexが画像を見られない場合は `human visual review required` と記録する。
- 必要なら修正promptで再生成する。
- 画像はレビュー前にfinalへ置かない。

## Day1 Candidate Save Paths

推奨保存先:

- `assets/generated/day1/page_01/candidates/day1_page_01_candidate_YYYYMMDD_01.png`
- `assets/generated/day1/page_02/candidates/day1_page_02_candidate_YYYYMMDD_01.png`
- `assets/generated/day1/page_03/candidates/day1_page_03_candidate_YYYYMMDD_01.png`
- `assets/generated/day1/page_04/candidates/day1_page_04_candidate_YYYYMMDD_01.png`
- `assets/generated/day1/page_05/candidates/day1_page_05_candidate_YYYYMMDD_01.png`
- `assets/generated/day1/page_06/candidates/day1_page_06_candidate_YYYYMMDD_01.png`

代替保存先:

- `outputs/day1/image_generation/candidates/day1_page_XX_candidate_YYYYMMDD_01.png`

## Day1 After Candidate Review

- Day1 16:9 final 6枚を人間承認で確定する。
- Day1 final contact sheetを作成する。
- Day1の後載せ文字設計を行う。
- Day1 16:9がOKなら4:5展開へ進む。
- Day1台本、カード、ワークシートへ反映する。
- その後、親説明用資料の作成へ進む。

## Parent Explanation Material

- 親説明用資料では、まず `outputs/parents/parent_explanation_material_plan.md` を人間確認する。
- 親は先生、採点者、ゲームマスターではなく、問いを出す伴走者として扱う。
- 子供向けほどゲームUIを強くしない。
- Facilitator Guide / Question Card / OK-NG Response Sheet / Safety Boundary Card / Session Flow Mapとして設計する。
- 画像生成を使う場合もmanual handoff modeにする。
- 正確な日本語本文、OK/NG声かけ、表、チェックリストは後編集またはMarkdown/スライド組版で載せる。

## Paused Routes

- Codex-run image generationはしない。
- GPT画像生成の代行実行はしない。
- Day1画像の一括生成はしない。
- Day1 v3 HTML/CSS中心の制作は、Day1 16:9 final候補と人間承認が揃うまで進めない。
- 4:5版、PDF、PPTX、A4印刷物は、Day1 16:9 final 6枚が確定するまで進めない。
- 台本、カード、ワークシートへの反映は、Day1 16:9 final 6枚と後載せ文字設計が固まるまで進めない。
- candidateをfinalフォルダへ置かない。
- 固定情報源フォルダへ画像本体をコピーしない。

## Safety Checks Before Commit

- `SOURCE_OF_TRUTH.md` と矛盾していないか確認する。
- docs-only commitに、教材生成物、画像生成物、PDF、PPTX、ブラウザプロファイルが混ざっていないか確認する。
- `.env`, Cookie, Login Data, Cache, Crashpad dump, 秘密情報を含めない。
- `git add .` は使わない。

## 既存の改善候補

- 各スライドを実際に見せる想定で、文字量をさらに減らす。
- ワークシートをA4印刷用に整える。
- カードをA4で切りやすい配置に変換する。
- 子供たちの興味に合わせて、ゲーム、部活、スマホ、勉強の例を増やす。
- 30分版、45分版、60分版の進行時間を各セッションで明確に分ける。
- 第3回と第4回を統合した4回版の台本を詳しく作る。
- 実施後の振り返りメモをもとに、問いの言い方を修正する。
- 親向け説明スライドをPowerPointやPDFに変換する。
- 子供向けスライドをMarpで表示確認する。
- 親御さん向け6枚インフォグラフィックを実際に印刷し、文字量と余白を確認する。
- 第1回Zoom実施パッケージ `outputs/day1/` を実際に画面共有で確認する。
- 第1回4:5試作PNGをスマホで確認し、必要なら余白と改行を調整する。
- 第1回実施後に `outputs/day1/session_01_after_action_review.md` へ反応を記録する。
- 第2回のZoom実施パッケージを作る。

## Codexへ次に依頼するとよいタスク

- Day1 image candidateをレビューしてください。
- Day1の後載せ文字設計を作ってください。
- 親説明用資料のPage1 prompt packetを作ってください。
- `slides/kids` の各MarkdownをMarp形式に整えてください。
- `cards` のカードをA4印刷用Markdownに整えてください。
- `worksheets` の各シートを記入欄つきの印刷用レイアウトにしてください。
