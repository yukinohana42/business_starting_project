# Day1 Page 1 Direction Review

## Status

- Page: Day1 Page 1 Mission Board
- Asset type: direction sample
- Source: ChatGPT image generation sample reviewed by user
- Codex visual review availability: image file is not present in this repository, so Codex did not perform direct visual inspection
- Human evaluation: 「むっちゃいい感じ。この方向ですすめてほしい」

## Decision

`DIRECTION_APPROVED_NOT_FINAL`

今回の画像は、Day1 Page 1の方向性サンプルとして採用する。ただし、final教材画像としては、visual review and refinementを通してから採用する。

## Good Points

- 発見ゲーム型教材画面に見える。
- ユウが行動している。
- Mission Board / 探偵ノート / Mission Card / Quest Map / 発見スタンプが機能している。
- 中2男子が見ても幼すぎない。
- 仕事を「誰かの変化を見る」として扱えている。
- お金や起業で煽っていない。
- HTML/CSS直描き版より、世界観とキャラクターの魅力が出ている。

## Issues

- 虫眼鏡などの小物が意味不明な位置に出ると、教材としての信頼感が下がる。
- 小物の数、位置、意味を生成後レビューで確認する必要がある。
- 日本語の細かい文字は画像生成だけに任せず、後載せ候補にする。
- Codex環境では実画像ファイルを確認できていないため、小物の具体的な破綻箇所は人間レビュー結果に基づく。

## Fix Before Finalization

- 虫眼鏡、ペン、ノート、Mission Cardは、手、机、ボードなど意味のある位置に限定する。
- 小物が顔、体、背景から不自然に出ていないか確認する。
- Quest Map、Mission Card、探偵ノート、発見スタンプが飾りではなく、今日の学習行動とつながって見えるか確認する。
- 画像内の日本語は、大見出しと短いラベル程度に抑える。
- final化前に、画像そのものをCodexまたは人間が視覚レビューする。

## Prompt Reflection For Next Generation

次回生成promptには、以下を加える。

- Props must be physically connected to hands, table, board, or notebook.
- Do not create duplicate or floating props.
- Magnifying glass appears only if Yuu is holding it or if it rests clearly on the table.
- Pen, notebook, card, stamp, and Quest Map must support the learner action.
- Avoid props overlapping the face, eyes, torso, or key text areas.
- Keep exact Japanese copy minimal; detailed text will be added later.
- Generated image remains candidate until visual review.

## Style To Carry Into Page 2 And Later

- Warm hand-drawn educational illustration.
- Discovery-game learning screen, not a business poster.
- Yuu as an active learner proxy.
- Functional Mission Board / Case File / Card / Note UI.
- Age-appropriate original character design.
- Calm detective-learning atmosphere.
- No money hype, no competition, no startup pressure.

## Human Review Required For Final

Before final adoption, a reviewer must inspect the actual image and answer:

- Are any props floating or attached incorrectly?
- Are hands, gaze, and learning action aligned?
- Are Japanese text areas usable for overlay?
- Are any labels broken or contradictory?
- Does the image still look like a Mission Board, not a poster?

## Next Action

Use this direction as the visual target for Day1 Page 2 prompt. Do not treat the current sample as final unless it passes the full visual review checklist and final naming policy.
