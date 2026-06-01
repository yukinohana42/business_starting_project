# Day1インフォグラフィックPNGレンダリング

第1回「働くって何？ お金って何？ 価値って何？」の6枚構成インフォグラフィックを、Zoom共有用PNGとして出力するための手順フォルダです。

## 元にしたファイル

- `outputs/day1/session_01_infographic_zoom.md`
- `outputs/day1/session_01_infographic_copy.md`
- `outputs/day1/session_01_infographic_spec.md`
- `DESIGN.md`

## 出力先

- `outputs/day1/rendered/session_01_infographic_16x9_page_01.png` から `page_06.png`
- `outputs/day1/rendered/session_01_infographic_4x5_page_01.png` から `page_06.png`
- `outputs/day1/rendered/session_01_infographic_16x9_contact_sheet.png`

## レンダリング方法

HTML/CSSで各ページを固定サイズの `.page` として作り、Chromeのheadless screenshotで各ページをPNG化しています。一覧画像はPNGを読み込んで縮小合成しています。

詳しい手順は `render_day1_infographic.md` を見てください。
