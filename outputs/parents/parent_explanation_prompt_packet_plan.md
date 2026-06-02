# Parent Explanation Prompt Packet Plan

## Purpose

親説明用資料を画像生成前提で作る場合のprompt packet化方針を定義する。

標準運用はmanual handoff modeです。Codexはprompt packet、レビュー基準、保存先、修正promptを作ります。ユーザーがGPT画像生成にpromptを貼り、生成画像をcandidateとしてrepoへ戻します。

## Role Split

| Role | Parent Material Work |
| --- | --- |
| Codex | ページ構成、本文案、図解方針、prompt packet、保存先、レビュー基準、修正prompt、後載せ文字設計 |
| GPT画像生成 | 親子の場面、問いカード、安全境界カード、穏やかな背景などのcandidate画像作成 |
| ユーザー | promptを貼る、画像を配置する、人間の第一印象を返す、final承認を行う |

## When To Use GPT Image Generation

使う:

- 親子が同じ机で話す温かい場面。
- 親が横からQuestion Cardを差し出す場面。
- Facilitator Guideの雰囲気づくり。
- Safety Boundary Cardの視覚的な背景。
- Praise Guideの穏やかなイラスト。

使いすぎない:

- OK/NGの正確な文言。
- Day1-Day5の表。
- チェックリスト。
- 長い説明本文。
- PDF/PPTXの最終組版。

## Text Accuracy Rule

親向け資料では文字の正確さが重要です。画像生成に長い日本語文やOK/NG例を任せません。

Promptでは、次のように指定する:

- leave clean blank areas for exact Japanese text overlay
- use blank cards or very short placeholder labels only
- do not generate long Japanese paragraphs
- do not use generated Japanese as final teaching copy

## Parent Visual Anchor Draft

```text
Create a warm, calm, original parent-facing educational visual for a Japanese family workshop. The visual should feel practical, supportive, and easy to use, not like a child-facing game screen and not like a corporate seminar poster.

Show the parent as a facilitator beside the child, not a teacher, scorer, judge, or game master. The parent should offer a Question Card, listen, or point gently to a Safety Boundary Card. The child should remain respected and not evaluated.

Use soft paper tones, calm gray-blue structure, warm cream background, muted coral question accents, soft green support accents, and pale blue organization lines. Keep the composition clean for later Japanese text overlay.

Do not show entrepreneurship pressure, money hype, anxiety about the future, ranking, scores, trophies, prizes, comparison between children, or grading. Use fully original people and avoid any resemblance to existing anime, manga, game, mascot, brand, artist, studio, or franchise.

Generated output is a candidate, not final. Exact Japanese copy, OK/NG examples, checklist text, page numbers, and tables will be added later in layout.
```

## Prompt Packet Structure

Each parent prompt packet should include:

1. 使用目的。
2. 画像生成に貼る最終プロンプト。
3. 生成後チェックリスト。
4. NGなら使う修正プロンプトテンプレート。
5. candidate保存先。
6. Codexへ戻す報告テンプレート。
7. 後載せ文字の範囲。
8. final化禁止ルール。

## Candidate Save Paths

推奨:

```text
assets/generated/parents/page_01/candidates/parent_page_01_candidate_YYYYMMDD_01.png
```

代替:

```text
outputs/parents/image_generation/candidates/parent_page_01_candidate_YYYYMMDD_01.png
```

## Review Checklist

- 親が先生、採点者、ゲームマスターに見えないか。
- 親が問いを出す伴走者として見えるか。
- 子供が評価される側として萎縮していないか。
- OK/NGやSafety Boundaryを後載せできる余白があるか。
- 子供向けゲームUIを強く出しすぎていないか。
- 起業を押し付けていないか。
- お金、競争、将来不安で煽っていないか。
- 既存IPや特定作家の模倣に見えないか。
- 文字崩れをfinal本文として使っていないか。

## Candidate / Review / Final Flow

1. CodexがPage 1 prompt packetを作る。
2. ユーザーがGPT画像生成へ貼る。
3. ユーザーがcandidate画像を保存する。
4. ユーザーが第一印象を返す。
5. Codexが画像を確認できる場合はreviewする。
6. Codexが画像を確認できない場合は `human visual review required` と明記する。
7. 必要なら修正promptを作る。
8. 人間承認後にだけfinal候補へ進める。

## Next Action

まず `outputs/parents/parent_explanation_material_plan.md` を人間確認する。

確認後、親説明資料のPage 1 prompt packetを作る。画像生成ではなく図解中心で十分と判断された場合は、Markdown/スライド原稿から作る。
