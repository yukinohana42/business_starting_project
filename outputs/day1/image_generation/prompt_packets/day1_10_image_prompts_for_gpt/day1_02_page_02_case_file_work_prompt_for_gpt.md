# Day1 02 Page 02 Case File Work Prompt For GPT

## 使う目的

Day1 Page2「仕事は、誰かの状態を少し良くすること」を、Before / Afterで見せるcandidate画像を作る。

## GPT画像生成に貼り付ける最終プロンプト

```text
Create a 16:9 horizontal warm hand-drawn educational illustration for a Japanese junior high school grade 8 workshop.

This is a discovery-game learning screen, not a generic explanation slide and not a business poster.

Use fully original characters only. Do not imitate any existing anime, manga, game, mascot, brand, logo, artist, studio, or franchise.

Page type: Case File - Work.

Scene:
A warm Case File board shows two large panels: Before Card and After Card. In the Before Card, a same-age student is mildly troubled by a small everyday inconvenience. In the After Card, the same student looks slightly relieved because the situation became easier.

Yuu observes, points from Before to After, or writes in a detective notebook.

Show:
- Case File board
- Before Card
- After Card
- Detective Note
- Discovery Stamp slot as a learning record
- Quest Map with the Observation step emphasized
- clean blank areas for later Japanese headline: "仕事は、誰かの状態を少し良くすること"

Character action:
Yuu's hand, gaze, pen, notebook, and cards connect naturally. Yuu is comparing the two states, not standing still.

Visible change:
Mildly troubled same-age student -> slightly relieved same-age student. Do not mock the Before state. After is a small believable improvement, not victory.

Text handling:
Do not generate long Japanese text. Important Japanese body text, labels, and question will be added later. Leave clean overlay areas.

Safety:
No startup pressure. No money hype. No ranking, score, trophy, winner/loser, prize, or reward-like elements.

Negative prompt:
existing anime, manga, game, mascot, brand, logo, specific artist style, studio style, face-only character, Yuu standing still, floating magnifying glass, duplicate props, props emerging from face or body, broken hands, impossible fingers, Before person mocked, After victory celebration, money hype, ranking, score, trophy, reward, broken Japanese paragraphs.
```

## 生成後チェック

- Case Fileに見えるか。
- Before / Afterが「困っている -> 少し助かった」と読めるか。
- Beforeを笑いものにしていないか。
- Afterが大成功、勝利、報酬に見えないか。
- Yuuが観察、指差し、メモの行動をしているか。
- 手、ノート、ペン、カードが自然につながっているか。
- 日本語を後載せできる余白があるか。
- 既存IP模倣、起業押し付け、お金煽りがないか。

## 修正プロンプトテンプレート

```text
Revise the Day1 Page2 Case File image while keeping the warm discovery-game educational style.

Keep: Case File board, Before Card, After Card, Yuu observing or comparing, Detective Note, Quest Map, Discovery Stamp slot, 16:9 layout.
Fix: [specific issue]
Clarify: Before is mild and respectful. After is a small helpful change, not a victory. Yuu points or writes naturally.
Remove: floating props, duplicate props, broken Japanese text, money hype, ranking, score, trophy, reward-like elements, IP resemblance.
Text: leave clean blank areas for exact Japanese overlay.
```

## 候補保存先

```text
assets/generated/day1/page_02/candidates/day1_page_02_candidate_YYYYMMDD_01.png
```

代替:

```text
outputs/day1/image_generation/candidates/day1_page_02_candidate_YYYYMMDD_01.png
```

## Codexへ戻すテンプレート

```text
page_id: day1_page_02
prompt_packet_used: outputs/day1/image_generation/prompt_packets/day1_10_image_prompts_for_gpt/day1_02_page_02_case_file_work_prompt_for_gpt.md
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
