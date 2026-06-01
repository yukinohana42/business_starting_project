# Prompts and Next Codex Tasks

## prompts/ にある既存プロンプト

| Prompt | Purpose |
|---|---|
| `prompts/worksheet_generation_prompt.md` | ワークシート生成用 |
| `prompts/slide_generation_prompt.md` | 子供向け・親向けスライド生成用 |
| `prompts/session_improvement_prompt.md` | セッション改善用 |
| `prompts/parent_slide_generation_prompt.md` | 親向け説明スライド生成用 |
| `prompts/day1_infographic_generation_prompt.md` | Day1インフォグラフィック生成用 |
| `prompts/codex_next_tasks.md` | 次のCodex作業指示用 |
| `prompts/codex_freeze_gpt_context_prompt.md` | 固定情報源作成・更新用 |
| `prompts/codex_design_brushup_plan_prompt.md` | デザインブラッシュアップ計画用 |
| `prompts/codex_day1_material_improvement_prompt.md` | Day1教材改善用 |
| `prompts/card_generation_prompt.md` | カード教材生成用 |

## 次に使うべきCodexプロンプト

Day1 v2へ進む場合は、次の順で使います。

1. `outputs/day1/session_01_infographic_v2_storyboard.md` と `outputs/day1/session_01_infographic_v2_copy.md` を確認する。
2. `outputs/day1/session_01_infographic_v2_illustration_prompt.md` を、既存IP模倣がないか監査する。
3. 既存 `outputs/day1/rendered/session_01_infographic_16x9.html` とCSSをベースに、v2 HTML/CSS案を作る。
4. 16:9で表示確認後、4:5へ展開する。
5. PNG再生成は、HTML/CSS表示確認後に行う。

## Day1 v2 PNG再生成に必要なプロンプト要素

- Page 1: 今日のミッション「お金と仕事の正体を見破れ」。
- Page 2: 困った顔 -> 助かった顔のBefore/After。
- Page 3: お金は「ありがとうが見える形」。
- Page 4: 価値変換カードをユウとソラが並べる。
- Page 5: ビジネス探偵ノートで身近な仕事を観察する。
- Page 6: Final Missionとして自分の言葉で1文を書く。
- 完全オリジナルキャラクターであること。
- 既存作品、既存キャラクター、特定漫画家の絵柄を模倣しないこと。
- 勝敗、ランキング、報酬で釣る表現を入れないこと。

## PR作成・merge時の注意

- 作業ブランチ: `docs/gamified-visual-foundation-v1`
- PR作成URL: `https://github.com/yukinohana42/business_starting_project/pull/new/docs/gamified-visual-foundation-v1`
- PR本文には、docs中心の変更、PNG再生成なし、既存IP模倣なし、秘密情報なしを明記する。
- merge後は、source branchを削除できる場合は削除する。
- merge後にmainのHEADを `docs/current_git_status.md` と固定情報源へ反映する。

## 固定情報源更新時の注意

- `docs/GPT_FIXED_CONTEXT_CURRENT.md` が最新版フォルダを指しているか確認する。
- 固定情報源フォルダにはMarkdown中心で置く。
- PNG、HTML、CSSはコピーせず、パスと説明だけを書く。
- SOURCE_OF_TRUTHと矛盾する表現を入れない。
- `.env`、Cookie、Login Data、Cache、秘密情報を追加しない。
- 既存IP模倣の指示を入れない。
