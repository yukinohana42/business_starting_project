# Day1 16:9 v3 Prototype Review

## Pre-Production Stop Check

| Page | Screen Type | Character Action | Game Element | Learner Action | Visible Change | Stop Check |
| ---- | ----------- | ---------------- | ------------ | -------------- | -------------- | ---------- |
| Page 1 | Mission Board | Yuu writes in a detective note and holds visible tools: pen, notebook, mission card, magnifier. | Mission Card, Detective Note, Quest Map, Discovery Stamp slot. | Confirm today's mission and the final sentence. | Work shifts from "getting money" to "seeing someone's change." | PASS |
| Page 4 | Card Table - Value | Yuu points at a card while Sora writes or places a sticky note on the card table. | Value Change Cards, Card Table, Quest Map, Discovery Stamp. | Match the Before state with the After state. | Troubled -> helped, confused -> can try, bored -> fun. | PASS |
| Page 5 | Business Detective Case File | Yuu checks the case file with a magnifier while Sora pins an evidence card. | Case File, Evidence Cards, Business Detective Note, Quest Map, Discovery Stamp. | Pick one case and say who changes and how. | Rushed person -> can buy quickly, confused person -> can try, bored time -> fun time. | PASS |

No page proceeds with a round icon, face-only character, label-only game element, plain heading/body/card layout, unclear learner action, missing change, scoring, ranking, reward bait, or money hype.

## 1. v2からの改善点

- キャラクターを丸顔アイコンから、頭・髪・体・腕・手・服装・小物・ポーズを持つinline SVG人物へ変更した。
- Page 1ではユウが探偵ノートにメモする場面にした。
- Page 4ではユウとソラが机の上で価値変換カードを操作する場面にした。
- Page 5ではユウとソラがCase FileにEvidence Cardを貼る場面にした。
- Quest Map、Mission Card、Detective Note、Value Change Card、Case File、Evidence Cardを学習行動に結びつけた。
- 説明カードを並べる構成ではなく、学習画面の中で「見る・選ぶ・言う」が起きる構成にした。

## 2. ページ別合格基準表

| Page | Character Action | Game Element | Learner Action | Visible Change | Pass/Fail | Notes |
| ---- | ---------------- | ------------ | -------------- | -------------- | --------- | ----- |
| Page 1 | ユウが探偵ノートにメモし、ペン・ノート・カード・虫眼鏡が見える。 | Mission Board, Mission Card, Detective Note, Quest Map, Discovery Stamp slot. | 今日のミッションと最後に書く文を確認する。 | 仕事=お金をもらう？ -> 仕事=誰かの変化を見る。 | PASS | 普通の表紙ではなく、ミッション開始画面として設計。 |
| Page 4 | ユウがカードを指差し、ソラが付箋とペンでカード作成に参加している。 | Card Table, Value Change Cards, Quest Map, Discovery Stamp. | Before/Afterを組み合わせて声に出す。 | 困った -> 助かった、わからない -> できそう、退屈 -> 楽しい。 | PASS | 3枚カードの横並びではなく、机上作業として構成。 |
| Page 5 | ユウがCase Fileを観察し、ソラがEvidence Cardを貼っている。 | Case File, Evidence Cards, Business Detective Note, Quest Map, Discovery Stamp. | 3例から1つ選び、誰がどう変わるかを言う。 | 急いでいる人 -> すぐ買えて助かる、わからない人 -> できそうになる、退屈な時間 -> 楽しい時間になる。 | PASS | スマホゲームは価値変化として扱い、礼賛・課金・依存表現は入れていない。 |

## 3. ユーザー確認ポイント

- キャラクターの絵柄・年齢感が中学2年生向けとして幼すぎないか。
- inline SVG / CSS表現で十分か、画像生成素材が必要か。
- Page 4のカード作成場面が明確に見えるか。
- Page 5がCase File / Evidence Boardに見えるか。
- スマホゲーム例を正式版にも残すか。
- この方向性で6ページ正式版へ進めるか。

## 4. 次に進める条件

以下がすべてOKなら、次のタスクで正式版6ページを作成してよい。

- Page 1がMission Boardに見える。
- Page 4がCard Tableに見える。
- Page 5がCase Fileに見える。
- キャラクターが行動している。
- 丸アイコンに見えない。
- ゲーム要素が学習行動と結びついている。
- Zoomで読める。
- 勝敗・採点・報酬・金儲け煽りがない。

## PNG生成結果

生成完了。

- `outputs/day1/rendered/session_01_infographic_16x9_v3_prototype_page_01.png`
- `outputs/day1/rendered/session_01_infographic_16x9_v3_prototype_page_04.png`
- `outputs/day1/rendered/session_01_infographic_16x9_v3_prototype_page_05.png`

レンダリング条件:

- Chrome headless
- 1920x1080
- 16:9 Zoom共有想定
- 対象はPage 1 / Page 4 / Page 5のみ

今回あえてPage 2 / Page 3 / Page 6は作成していない。
v3正式版6ページ化の前に、この3ページの方向性を人間確認する。

## Contact Sheet

生成完了。

- `outputs/day1/rendered/session_01_infographic_16x9_v3_prototype_contact_sheet.png`

3枚を横並びにし、Mission Board -> Card Table -> Case Fileの流れ、文字量、キャラクター行動、ゲーム要素の統一感を確認できるようにした。

## 表示確認結果

| Page | PNG確認結果 | Notes |
| ---- | ----------- | ----- |
| Page 1 | PASS | Mission Board、Mission Card、Detective Note、ユウの行動、最後に書く文が見える。文字の重なりなし。 |
| Page 4 | PASS | Card Table上でBefore/Afterカードを操作する画面になっている。説明文を短くして、机・人物との干渉を解消。 |
| Page 5 | PASS | Case Fileと3つのEvidence Cardが見える。大見出しの改行を調整し、Case Fileとの重なりを解消。 |

## 修正内容

- Page 4の短い説明を「Before と After をつなげる。」に短縮した。
- Page 5の大見出しを3行改行にし、見出しとCase Fileの余白を確保した。
- Page 4 / Page 5 のPNGを再生成した。
- contact sheetを再生成した。

## 未確認の点

- キャラクターの年齢感が中学2年生向けとして幼すぎないか。
- inline SVG / CSS表現のままv3正式版6ページへ進めてよいか。
- Page 4の「価値変換カード」が、単なる説明カードではなく作業物として見えるか。
- Page 5の「スマホゲーム」例が、価値変化の観察例として適切か。
- Page 2 / Page 3 / Page 6を同じ視覚言語で作る際、画面が説明スライドに戻らないか。

## 次工程判断

- この方向でDay1 v3正式版6ページへ進めることは可能。
- ただし、正式6ページ化の前にcontact sheetを人間確認する。
- 4:5展開は、Day1 v3正式版6ページと16:9 PNG確認後に進める。
- 台本・カード・ワークシート反映は、正式6ページの表現が確定してから進める。
