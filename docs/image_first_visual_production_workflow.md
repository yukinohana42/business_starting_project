# Image-First Visual Production Workflow

## Purpose

Day1からDay5、親向け説明資料まで共通で使う、画像生成前提の教材制作フローを定義する。

このフローの目的は、教材を「説明スライド」ではなく、「発見ゲーム型の学習画面」として作ること。

## Standard Flow

### 1. Learning Objective

そのページで子供または親に残したい学びを1文にする。

例:

- 仕事は、誰かの状態を少し良くすること。
- 困りごとは、価値の種。
- 赤信号は失敗ではなく、次に変えるサイン。

### 2. Page Type

各ページを次のどれかに分類する。

Child-facing:

- Mission Board
- Case File
- Evidence Board
- Card Table
- Detective Note
- Experiment Lab
- Pitch Stage
- Final Mission Sheet

Parent-facing:

- Parent Facilitator Guide
- Question Card
- OK/NG Response Sheet
- Safety Boundary Card
- Observation Log
- Reflection Support Sheet

### 3. Character Action

ページごとに、キャラクターが何をしているかを1文で書く。

必須:

- 顔だけではなく、手元、視線、姿勢、小物がある。
- 行動は学習目的と結びつく。
- ユウ、ソラ、ミホは完全オリジナルキャラクターとして扱う。

### 4. Game Element Function

ゲーム要素がどの学習行動を進めるかを書く。

例:

- Mission Card: 今日する行動を確認する。
- Evidence Card: 身近な例から「誰がどう変わるか」を選ぶ。
- Question Card: 親が正解ではなく問いを出す。
- Reflection Stamp: 発見した行動を振り返る。

### 5. Learner Action

画面を見た子供が次に何をするかを明記する。

- 見る
- 選ぶ
- 話す
- 書く
- 比べる
- 試す

親向けでは、親が次に何を言うか、どう支えるかを明記する。

### 6. Visible Change

価値や学びを、変化として定義する。

例:

- 困った -> 助かった
- 面倒 -> ラク
- わからない -> できそう
- 思い込み -> 相手の反応
- 親が教える -> 親が問いを出す

### 7. Image Generation Prompt

各ページで、画像生成用promptを作る。

promptに必ず入れる:

- aspect ratio
- page type
- scene description
- character action
- props
- game elements
- visible change
- mood
- safety rules
- text handling rule
- negative prompt

画像内の日本語本文は最小限にする。長いコピー、空欄、カード本文は後編集で載せる。

### 8. Key Visual Generation

1ページずつ生成する。

生成時の原則:

- まずDay1 Page 1など1枚だけで試す。
- 6ページを一気に量産しない。
- キャラクター一貫性をanchor promptで守る。
- 生成結果は採用前にreview manifestへ記録する。

### 9. Copy Fitting

画像生成後、本文やカード文字を載せる。

HTML/CSSの役割:

- 画像の上に文字やカードを載せる。
- 空欄やラベルを正確に配置する。
- 16:9、4:5、A4を整える。
- 画像生成で崩れやすい文字を補正する。

### 10. Composition Adjustment

次を確認し、必要なら画像promptまたはレイアウトを戻して修正する。

- 主役行動が見えるか。
- 文字が読めるか。
- カードやノートが学習行動を示しているか。
- Before/Afterが見えるか。
- 説明スライドに戻っていないか。

### 11. Review

contact sheetとページ別reviewを作る。

必須レビュー:

- Visual Learning acceptance check
- image consistency check
- safety check
- text readability check
- parent role check when parent-facing

### 12. Final Export

人間確認後にのみ進む。

- 16:9 PNG
- 4:5 PNG
- PDF
- PPTX
- A4 print

## Directory Policy

推奨構造:

```text
prompts/image_generation/
  global/
  day1/
  day2/
  day3/
  day4/
  day5/
  parents/
assets/generated/
  day1/
  day2/
  day3/
  day4/
  day5/
  parents/
reviews/image_generation/
  day1/
  day2/
  day3/
  day4/
  day5/
  parents/
scripts/
```

今回の作業では、既存の `outputs/day1/prompts/` にDay1 pilot promptsを置く。将来、自動生成に進む時点で上記構造へ整理してよい。

## Review Manifest Fields

画像生成の再現性を高めるため、次を保存する。

- `page_id`
- `session`
- `asset_role`
- `aspect_ratio`
- `prompt_path`
- `prompt_version`
- `negative_prompt`
- `generation_date`
- `model_or_tool`
- `seed_or_reference_id` if available
- `selected_output_path`
- `rejected_output_paths`
- `review_memo`
- `human_reviewer`
- `status`

## Where Image Generation Helps

画像生成に任せる:

- 人物の表情、姿勢、視線。
- 手元の作業。
- 場面の温かさ。
- Case File、Card Table、Experiment Labなどの主場面。
- Before/Afterの感情変化。

後編集やHTML/CSSで補う:

- 日本語本文。
- 空欄。
- 正確なカード文言。
- page number。
- Quest Map。
- 16:9 / 4:5 / A4の整形。
- contact sheet。

## Common Image Generation Failures

| Failure | Prevention |
| --- | --- |
| 文字が多すぎる | 画像promptでは短いラベルだけにし、本文は後編集で載せる |
| ページごとの一貫性が崩れる | anchor promptとcharacter promptを必ず使う |
| キャラクターが毎回変わる | 髪型、服装、年齢感、小物、役割を固定する |
| 教材ではなくポスターになる | page type、learner action、propsを必ず入れる |
| ゲーム要素が飾りになる | ゲーム要素ごとに学習行動を明記する |
| お金や起業を煽る | negative promptで金束、高級品、勝敗、ランキングを禁止する |

## Stop Before Mass Generation

Day1で1ページだけpilot生成し、方向性が確認できるまで大量生成しない。
