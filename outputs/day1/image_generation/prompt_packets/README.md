# Day1 Prompt Packets For GPT Image Generation

## Purpose

Day1「働く・お金・価値 / Value Detective」の16:9画像を、ユーザーがChatGPT / GPT画像生成へ1ページずつ貼ってcandidate生成するためのprompt packet一覧です。

Codexは画像生成を実行しません。Codexはprompt packet、レビュー、修正prompt、保存先、candidate/final管理、後載せ文字設計を担当します。

## Packet List

| Page | Page Type | Purpose | Packet |
| --- | --- | --- | --- |
| Page 1 | Mission Board | 今日のミッションを開始する | `outputs/day1/image_generation/prompt_packets/day1_page_01_prompt_packet_for_gpt.md` |
| Page 2 | Case File - Work | 仕事をBefore/Afterで見る | `outputs/day1/image_generation/prompt_packets/day1_page_02_prompt_packet_for_gpt.md` |
| Page 3 | Evidence Board - Money | お金を「ありがとう」の見える形として見る | `outputs/day1/image_generation/prompt_packets/day1_page_03_prompt_packet_for_gpt.md` |
| Page 4 | Card Table - Value | 価値を相手の変化で見る | `outputs/day1/image_generation/prompt_packets/day1_page_04_prompt_packet_for_gpt.md` |
| Page 5 | Business Detective Case File | 3つの身近な仕事で誰がどう変わるかを見る | `outputs/day1/image_generation/prompt_packets/day1_page_05_prompt_packet_for_gpt.md` |
| Page 6 | Final Mission Sheet | 自分の言葉で1文にまとめる | `outputs/day1/image_generation/prompt_packets/day1_page_06_prompt_packet_for_gpt.md` |

## GPTへ貼る順番

1. Page 1を1枚だけ生成する。
2. Page 1のcandidateを保存し、人間の第一印象を記録する。
3. 問題がなければPage 2へ進む。
4. 同じ流れでPage 3、Page 4、Page 5、Page 6へ進む。

Page 1 / Page 2に既存の方向性画像がある場合は、先にrepoへcandidateとして配置してレビューできます。その場合は、再生成せずPage 3から始めてもよいです。

## One-By-One Rule

6ページを一括生成しません。ページごとにcandidateを作り、保存し、軽く確認してから次へ進みます。

理由:

- キャラクターの一貫性を守るため。
- 小物、手、視線、文字崩れを早めに直すため。
- ただの説明スライドやポスターに戻るのを防ぐため。
- Page 5の3例版が崩れて5例やランキングにならないようにするため。

## Candidate Save Paths

推奨:

```text
assets/generated/day1/page_01/candidates/day1_page_01_candidate_YYYYMMDD_01.png
assets/generated/day1/page_02/candidates/day1_page_02_candidate_YYYYMMDD_01.png
assets/generated/day1/page_03/candidates/day1_page_03_candidate_YYYYMMDD_01.png
assets/generated/day1/page_04/candidates/day1_page_04_candidate_YYYYMMDD_01.png
assets/generated/day1/page_05/candidates/day1_page_05_candidate_YYYYMMDD_01.png
assets/generated/day1/page_06/candidates/day1_page_06_candidate_YYYYMMDD_01.png
```

代替:

```text
outputs/day1/image_generation/candidates/day1_page_01_candidate_YYYYMMDD_01.png
```

どちらの場合も、最初から `final` には置きません。

## Return-To-Codex Template

共通テンプレート:

`outputs/day1/image_generation/user_handoff_template.md`

各ページのprompt packet末尾にも最小報告テンプレートがあります。

## Final Conditions

final化できる条件:

- candidate画像がrepoに保存されている。
- Codexまたは人間が視覚レビューしている。
- 手、小物、視線、文字崩れ、既存IP模倣、安全性の問題がない。
- 起業押し付け、お金煽り、勝敗、採点、ランキング、報酬化がない。
- exact Japanese copyは後載せで管理する方針が決まっている。
- 人間が採用を承認している。

Codexが画像を確認できない場合は、`human visual review required` としてfinal化しません。

## Next Process After Six Candidates

1. Page 1からPage 6までのcandidate reviewを作る。
2. 必要なら修正promptで再生成する。
3. Day1 16:9 final 6枚を人間承認で確定する。
4. final 6枚のcontact sheetを作る。
5. 後載せ文字の位置、サイズ、文言を設計する。
6. 16:9が承認されたら4:5へ展開する。
7. その後、台本、カード、ワークシートへ反映する。
