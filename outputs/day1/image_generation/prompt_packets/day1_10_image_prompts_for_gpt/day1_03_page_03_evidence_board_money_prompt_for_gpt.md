# Day1 03 Page 03 Evidence Board Money Prompt For GPT

## 使う目的

Day1 Page3「お金は『ありがとう』が見える形」を、価値が届いたサインとして見せるcandidate画像を作る。

## GPT画像生成に貼り付ける最終プロンプト

```text
Create a 16:9 horizontal warm hand-drawn educational illustration for a Japanese junior high school grade 8 workshop.

This is a discovery-game learning screen, not a business poster, shopping poster, or generic explanation slide.

Use fully original characters only. Do not imitate existing anime, manga, game, mascot, brand, logo, artist, studio, or franchise.

Page type: Evidence Board - Money.

Scene:
A warm Evidence Board shows the flow: value reaches someone -> thank-you card -> small money sign. A same-age student who was helped gives a small thank-you card. Yuu places a thank-you card or value evidence card on the Evidence Board.

Show:
- Evidence Board
- Thank-you Card
- Value Evidence Card
- a tiny coin, small receipt-like icon, or simple money sign card as a quiet sign
- Detective Note area
- Discovery Stamp slot as a learning record
- Quest Map with the money / thank-you step emphasized
- clean blank headline area for later Japanese overlay: "お金は「ありがとう」が見える形"

Character action:
Yuu pins, places, or writes an evidence card. Hands, card exchange, board, and gaze connect naturally.

Money rule:
Money appears only as a small sign. Do not show wealth. No money pile, cash rain, gold bars, luxury goods, rich lifestyle, or profit celebration.

Text handling:
Do not generate long Japanese text. Important Japanese body text and labels will be added later. Leave clean overlay areas.

Safety:
No startup pressure. No money hype. No ranking, score, trophy, winner/loser, prize, or reward-like elements.

Negative prompt:
existing anime, manga, game, mascot, brand, logo, specific artist style, studio style, money piles, cash rain, gold bars, luxury car, expensive watch, rich lifestyle, profit celebration, ranking, score, trophy, prize, reward, Yuu standing still, face-only icon, floating thank-you card, duplicate coins, random money props, broken hands, impossible fingers, broken Japanese paragraphs.
```

## 生成後チェック

- Evidence Boardに見えるか。
- value reaches someone -> thank-you card -> small money sign の流れが見えるか。
- お金が小さなサインで、主役になっていないか。
- Yuuがカードを貼る、置く、メモする行動をしているか。
- 助かった人の表情が自然で、大げさすぎないか。
- 小物が浮いたり増殖したりしていないか。
- 日本語を後載せできる余白があるか。
- 金儲け煽り、報酬化、勝敗、採点、ランキングがないか。
- 既存作品や特定絵柄に似ていないか。

## 修正プロンプトテンプレート

```text
Revise the Day1 Page3 Evidence Board image while keeping the warm discovery-game educational style.

Keep: Evidence Board, Yuu placing a thank-you or value evidence card, helped student with thank-you card, small quiet money sign, 16:9 layout.
Fix: [specific issue]
Clarify: money is a small sign of gratitude, not profit or status. Yuu's hand connects to the card or board.
Remove: money piles, luxury goods, duplicate coins, floating cards, broken Japanese, score, ranking, trophy, reward-like elements, IP resemblance.
Text: leave clean blank areas for exact Japanese overlay.
```

## 候補保存先

```text
assets/generated/day1/page_03/candidates/day1_page_03_candidate_YYYYMMDD_01.png
```

代替:

```text
outputs/day1/image_generation/candidates/day1_page_03_candidate_YYYYMMDD_01.png
```

## Codexへ戻すテンプレート

```text
page_id: day1_page_03
prompt_packet_used: outputs/day1/image_generation/prompt_packets/day1_10_image_prompts_for_gpt/day1_03_page_03_evidence_board_money_prompt_for_gpt.md
candidate_filename:
candidate_path:
human_candidate_decision: keep / revise / reject / unsure
first_impression:
good_points:
concerns:
meaningless_depictions:
text_issues:
hand_prop_gaze_issues:
safety_check:
next_action_requested_for_codex:
```

## 最終化しないルール

最初の生成画像はcandidateです。視覚レビューと人間承認が終わるまでfinalにしません。

## 日本語テキストの扱い

日本語の見出し、本文、ラベルは画像生成で完成させない。画像には、後から正しい日本語を重ねるための余白と読みやすい配置だけを作る。生成画像に崩れた日本語や不要な英字が出た場合は、候補レビューで修正対象にする。

## 権利とスタイルの禁止事項

既存の漫画、アニメ、ゲーム、ブランド、ロゴ、マスコット、特定作家、特定スタジオのキャラクターや絵柄をまねない。人物、衣装、小物、UIはすべて完全オリジナルとして扱う。
