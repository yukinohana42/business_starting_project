# Day1 Image Generation User Handoff Template

## Purpose

ユーザーがChatGPT / GPT画像生成で作ったDay1画像をrepoへ戻し、Codexにcandidate reviewや修正prompt作成を依頼するためのテンプレートです。

Codexは画像を勝手に生成しません。ユーザーが生成し、repoへ置き、見た印象を返します。

## 1. 基本情報

```text
page_id:
page_title:
prompt_packet_used:
generation_tool: ChatGPT / GPT image generation / other
generation_date:
aspect_ratio: 16:9
candidate_filename:
candidate_path:
```

## 2. ファイル配置

推奨保存先:

```text
assets/generated/day1/page_XX/candidates/day1_page_XX_candidate_YYYYMMDD_01.png
```

代替保存先:

```text
outputs/day1/image_generation/candidates/day1_page_XX_candidate_YYYYMMDD_01.png
```

注意:

- `final` には置かない。
- ファイル名に `candidate` を入れる。
- 画像が複数ある場合は `_01`, `_02` のように番号を付ける。
- 既存v1/v2/v3 PNGを上書きしない。

## 3. 人間の第一印象

```text
first_impression:
```

例:

- この方向でよい。
- 雰囲気はよいが説明スライドっぽい。
- キャラクターはよいが小物が意味不明。
- 文字が多すぎる。

## 4. 良い点

```text
good_points:
- (記入)
- (記入)
- (記入)
```

## 5. 気になる点

```text
concerns:
- (記入)
- (記入)
- (記入)
```

## 6. 意味不明な描写

```text
meaningless_depictions:
- floating props:
- duplicated props:
- props emerging from face/body:
- props covering face/hands/text area:
- confusing scene logic:
```

## 7. 文字崩れ

```text
text_issues:
- broken Japanese:
- tiny unreadable text:
- text that should be covered by overlay:
- text that may confuse the learner:
```

## 8. 手・小物・視線の破綻

```text
hand_prop_gaze_issues:
- hands/fingers:
- pen/notebook/card connection:
- gaze direction:
- character posture:
- object placement:
```

## 9. 安全性チェック

```text
safety_check:
- entrepreneurship pressure: none / concern
- money hype: none / concern
- scoring/ranking/reward framing: none / concern
- existing IP/style imitation risk: none / concern
- parent/teacher judgment framing: none / concern
```

## 10. Candidate判定

```text
human_candidate_decision: keep / revise / reject / unsure
reason:
```

判定目安:

- `keep`: Codex reviewへ進めたい。
- `revise`: 修正promptがほしい。
- `reject`: 方向性が違うので作り直したい。
- `unsure`: Codexの視覚レビューを先に見たい。

## 11. 次アクション

```text
next_action_requested_for_codex:
- review candidate
- create correction prompt
- compare candidates
- plan overlay text
- mark human visual review required
- other:
```

## 12. Codexへの戻し方

Codexへ依頼するときは、次を貼ってください。

```text
Day1 image candidateをレビューしてください。

page_id:
prompt_packet_used:
candidate_filename:
candidate_path:
human_candidate_decision:
first_impression:
good_points:
concerns:
meaningless_depictions:
text_issues:
hand_prop_gaze_issues:
safety_check:
next_action_requested_for_codex:
```

Codexが画像ファイルを読めない場合は、見たふりをせず `human visual review required` と記録します。
