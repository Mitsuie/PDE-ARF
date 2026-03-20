# AI 入出力ログ

- **日時**: 2026-03-20 16:33:24
- **チャットタイトル**: customtkinter Install

---

## ユーザー入力

> このPCにcustomtkinterを使用できるようにしたい。
> コンソールに入力するコードを提案せよ。

---

## AI 出力

`customtkinter` のインストールは以下のコマンドで行えます。

```powershell
pip install customtkinter
```

インストール後、正しく動作するか確認したい場合は以下のコマンドも実行してみてください。

```powershell
python -c "import customtkinter; print(customtkinter.__version__)"
```

> **Note**
> もし `pip` コマンドが見つからない場合は、代わりに以下を試してください。
> ```powershell
> python -m pip install customtkinter
> ```

---

# AI 入出力ログ（追記）

- **日時**: 2026-03-20 16:35:12

---

## ユーザー入力

> このPCにライブラリ「docx」を使用できるようにしたい。
> コンソールに入力するコードを提案せよ。

---

## AI 出力

Pythonで `docx`（Word文書操作）を使うには、パッケージ名が `python-docx` となるため、以下のコマンドでインストールします。

```powershell
pip install python-docx
```

> **Important**
> インストール時のパッケージ名は **`python-docx`** ですが、コード内でのインポートは **`docx`** を使います。
> ```python
> from docx import Document
> ```

インストール確認は以下で行えます。

```powershell
python -c "import docx; print(docx.__version__)"
```
