# Image Generation Review And Refinement Workflow

## Purpose

画像生成ファースト制作では、最初に出た画像をそのままfinal教材画像にしない。

必ず candidate -> review -> revise -> final の順で進める。生成画像は、発見ゲーム型教材として意味が通るか、キャラクター行動が自然か、教材として不適切な要素がないかを確認してから採用する。

## Core Rule

Generated images are candidates, not final assets.

最初の生成物は、どれだけ良く見えても `candidate` または `direction sample` として扱う。`final` に移せるのは、視覚レビュー、修正判断、人間確認、採用理由の記録が終わった画像だけ。

## Required Workflow

1. candidate画像を保存する。
2. 画像をレビューする。
3. 意味不明な描写、破綻、不適切な描写を検出する。
4. 修正プロンプトを作成する。
5. 必要なら再生成する。
6. final候補を再レビューする。
7. final採用品だけを `final` として保存する。
8. `rejected`、`draft`、`candidate` は採用版と明確に分けて保存する。
9. レビュー結果と採用理由をMarkdownに残す。

## Visual Review Requirement

Codex環境で画像を視覚的に確認できる場合:

- 画像そのものを開いて確認する。
- 小物、手、視線、文字、画面タイプ、教材意図を実画像に基づいてレビューする。
- 見えた問題を具体的に書く。

Codex環境で画像を視覚的に確認できない場合:

- 見たふりをしない。
- `human visual review required` と明記して停止する。
- 画像ファイルのパス、レビュー観点、チェックリスト、修正プロンプト雛形を作る。
- 人間が見た評価だけを根拠に書く場合は、その範囲を明記する。

## Review Outputs

1画像につき、原則としてレビューMarkdownを1つ残す。

Recommended path:

```text
outputs/day1/image_generation/reviews/day1_page_01_review_YYYY-MM-DD.md
```

最低限書く:

- page id
- candidate filename
- prompt path
- review date
- reviewer
- visual review availability
- educational fit
- visual defects
- safety defects
- text handling notes
- correction prompt
- decision
- next action

## Decision Levels

| Decision | Meaning |
| --- | --- |
| PASS_FINAL | そのままfinal候補としてよい |
| PASS_WITH_MINOR_FIX | 小修正または後載せで対応可能 |
| REGENERATE_WITH_REVISED_PROMPT | promptを修正して再生成が必要 |
| REJECT | 方針違い、教材として不適切、または意味不明描写が多く不採用 |
| DIRECTION_APPROVED_NOT_FINAL | 方向性サンプルとして採用。ただしfinal化にはレビュー精製が必要 |

## Meaningless Or Broken Depiction Check

修正対象:

- 小物が意味不明な場所から出ている。
- 持ち物が手とつながっていない。
- 虫眼鏡、ペン、カード、ノートが顔や体に不自然に重なる。
- 同じ小物が不要に増殖している。
- 背景装飾が学習意図より目立つ。
- 何をしている場面かわからない。
- キャラクターの視線と行動が合っていない。
- 手、指、腕、姿勢が不自然で学習行動に見えない。
- カードやノートが読めないほど崩れている。
- 日本語文字が崩れて意味不明。
- 画面内ラベルが内容と矛盾している。
- お金や報酬を煽るように見える。
- 勝敗、ランキング、採点、トロフィー、レベルアップ報酬に見える。

## Correction Prompt Template

```text
Revise the previous image while keeping the approved overall direction:

- Keep: [approved style, character, page type, learning action]
- Fix: [specific broken or confusing visual issue]
- Remove: [meaningless duplicate props, broken text, inappropriate element]
- Clarify: [character hand action, gaze, prop connection, game element function]
- Text: keep generated text minimal; exact Japanese copy will be added later
- Safety: no money hype, no competition, no score, no reward bait, no IP resemblance
- Output: same aspect ratio and composition family
```

## Finalization Rule

`final` に保存する前に、以下を満たす。

- visual review済み。
- final候補の問題点が許容範囲または後編集で対応可能。
- 採用理由がMarkdownに書かれている。
- 後載せ予定文字が決まっている。
- 人間確認者または確認待ち状態が記録されている。

## Relation To Layout

画像生成は、場面、人物、手元、小物、感情、画面タイプを作る。正確な日本語本文、空欄、カード文言、ページ番号、Quest Mapの細かい表示は、後編集またはHTML/CSSで載せる。

画像内に長い日本語本文を入れすぎた候補は、原則として修正対象にする。
