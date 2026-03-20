# AI入出力ログ
**ファイル名**: 20260320_181700_frame_centering_implementation.md
**タイムスタンプ**: 2026-03-20 18:17:00

---

## ユーザーの入力

> 方法Bに従い、実装を行え。

---

## AIの出力

`main.py` の321〜324行目（`canvas.create_window` 周辺）を以下の通り変更した。

### 変更前

```python
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

scrollable_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))
```

### 変更後

```python
window_id = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")


# Canvasのサイズ変更時にscrollable_frameを横方向中央に配置する関数
def on_canvas_configure(event):
    canvas_width = event.width
    canvas.coords(window_id, canvas_width // 2, 0)
    canvas.itemconfig(window_id, anchor="n")
    canvas.config(scrollregion=canvas.bbox("all"))


canvas.bind("<Configure>", on_canvas_configure)

scrollable_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))
```

### 変更の概要

1. `canvas.create_window(...)` の戻り値を `window_id` 変数に保存
2. `on_canvas_configure` 関数を追加:
   - Canvasの横幅（`event.width`）を取得
   - `canvas.coords(window_id, canvas_width // 2, 0)` でフレームを横中央位置に移動
   - `canvas.itemconfig(window_id, anchor="n")` でアンカーを「上中央」に変更
   - スクロール領域を再計算
3. `canvas.bind("<Configure>", on_canvas_configure)` でCanvasリサイズ時に自動実行されるよう登録
