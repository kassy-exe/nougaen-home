# NougÆn 公式サイト

人工言語 NougÆn（ヌウゲン）の公式サイト。スローガンは **Simplified, Glorious, Logical**。

- Live: https://nougaen-home.aokassy.workers.dev/
- NougÆn IS: https://nougaen-is.vercel.app

## 構成

- `index.html` — サイト本体（単一ファイル）。編集はここだけ
- `worker.js` — Cloudflare Worker。`index.html` を文字列として埋め込んで返すだけ（自動生成）
- `build.py` — `index.html` から `worker.js` を再生成する
- `font-b64.txt` — 砮文字フォント (Nougaen.woff2) の base64

## デプロイ

```sh
python3 build.py
# Cloudflare API 経由で Worker "nougaen-home" に worker.js をデプロイ
```

スクロールに連れて深海へ潜っていく演出、12進数のモチーフ、語幹字リングなどが入っている。
キャッシュは `max-age=300` なので、デプロイ直後は最大5分ほど旧版が見えることがある。
