# PDE-ARF アプリケーション インストーラ作成マニュアル

本マニュアルは、Pythonスクリプト（`main.py`）から単一の実行可能ファイル（`.exe`）を作成し、さらに「Inno Setup」を用いて配布用のインストーラを作成するまでの具体的な手順を記載しています。

## 1. 事前準備
以下のファイルが同じディレクトリ（例: `PDE-ARF`フォルダ）内に揃っていることを確認してください。
* `main.py` （プログラム本体）
* `PDM_ARF-001.docx` （同梱するテンプレートファイルなどのデータ）
* `icon_PDE-ARF.ico` （アプリアイコン画像）

また、以下のツールがWindowsにインストールされている必要があります。
* **PyInstaller** (`pip install pyinstaller` にてインストール)
* **Inno Setup** (公式サイト https://jrsoftware.org/isinfo.php より「Download Inno Setup」ページからインストーラをダウンロードして導入)

---

## 2. PyInstallerを使用した実行可能ファイル（.exe）の作成

PyInstallerの`--onefile`オプションを使用し、すべての関連ファイルとライブラリを1つの`.exe`ファイルとしてパッケージ化します。

### 手順
1. コマンドプロンプト、PowerShell、またはVSCodeなどのターミナルを開きます。
2. `cd` コマンドを使用して、対象の `main.py` が配置されているディレクトリ（`PDE-ARF`）へ移動します。
3. 以下のコマンドを実行します。

```bash
pyinstaller --noconsole --onefile --add-data "PDM_ARF-001.docx;." --icon "icon_PDE-ARF.ico" main.py
```

### コマンドの解説
* `--noconsole` : アプリ起動時に背後に黒いコンソール画面（コマンドプロンプト画面）を表示させないようにします。
* `--onefile` : 実行に必要なPython環境やライブラリ群を、すべて1つの`.exe`ファイルの中に圧縮して格納します。
* `--add-data "PDM_ARF-001.docx;."` : 指定したデータファイル（Wordドキュメント等）を`.exe`の内部に同梱します。`;.` は「実行時の解凍先ルート階層に配置する」ことを意味します。（Macの場合は `:` を区切り文字として使いますが、Windows環境の場合は `;` を用います）
* `--icon "icon_PDE-ARF.ico"` : 生成される`.exe`ファイル自体に設定するアイコン画像を指定します。

**ビルド完了後の確認**
処理が完了すると、ディレクトリ内に `dist` というフォルダが作成されます。その中に生成された `main.exe` が入っていることを確認してください。（これを後ほどのInno Setupで参照します）

---

## 3. Inno Setupを使用したインストーラの作成

PyInstallerで作成した `main.exe` を利用者に配布・インストールしやすい形式（`setup.exe`）にするため、Inno Setupのウィザードを使用します。

### 手順（スクリプトウィザードの設定項目）

1. インストール済みの **Inno Setup Compiler** を起動します。
2. 起動直後の画面で **「Create a new script file using the Script Wizard」** にチェックを入れ、[OK] をクリックします（ウィザードが開始します）。
3. 以降、[Next >] をクリックして進めながら、各項目を以下のように設定します。

#### ① Application Information (アプリケーション情報設定)
利用者のPCに表示される基本情報を入力します。
* **Application name**: アプリの名称（例: `PDE-ARF 会計要望書生成アプリ`）
* **Application version**: バージョン情報（例: `1.0`）
* **Application publisher**: 発行元や団体名（任意）
* **Application website**: ウェブサイトURL（任意・空欄可）

#### ② Application Folder (インストール先の指定)
アプリがどこにインストールされるかを設定します。
* **Application destination base folder**: デフォルトの `Program Files folder` のままで問題ありません。
* **Application folder name**: インストール先フォルダ名（基本はApplication nameが自動入力されます）。
* 「Allow user to change the application folder（利用者にインストール先の変更を許可する）」 はチェックを入れたままで進めます。

#### ③ Application Files (重要：ファイルの指定)
ここで、PyInstallerでビルドした実行ファイルを指定します。
* **Application main executable file**: 
  [Browse...] ボタンを活用し、先ほど作成された **`dist\main.exe`** を選択します。
* 「Allow user to start the application after Setup has finished」はチェックしたままで問題ありません。
* **Other application files**:
  【重要】今回はPyInstallerの `--onefile` および `--add-data` オプションを使用しており、必要なファイル（`PDM_ARF-001.docx` や関連モジュール等）は既に `main.exe` の内部に同梱・圧縮されています。そのため、**ここでの追加指定は一切不要です（空欄のままでOK）。**

#### ④ Application Shortcuts (ショートカットの作成)
* **Start Menu folder name**: スタートメニューに作成されるプログラムフォルダ名です（自動入力のままで可）。
* 利用者の利便性を考慮し、以下のチェック項目を推奨します：
  * 「Create a shortcut to the main executable in the Start Menu folder」 （チェック推奨：スタートメニューへの登録）
  * 「Allow user to create a desktop shortcut」 （チェック推奨：利用者にデスクトップショートカット作成の選択肢を提供）

#### ⑤ Application Documentation (ドキュメント設定)
* アプリのライセンス条項（License file）や、インストール前（Information file: Before installation）、インストール後（Information file: After installation）に表示させたいテキストファイルがあれば指定します。通常はすべて空欄のままで [Next] に進んで問題ありません。

#### ⑥ Setup Languages (言語設定)
* インストーラが起動した際の表示言語を設定します。`Japanese` にチェックを入れます（Englishと併用も可能です）。

#### ⑦ Compiler Settings (出力ファイルの設定)
完成した「セットアップ用のインストーラ本体」自体の設定を行います。
* **Custom compiler output folder**: 完成したインストーラを出力する場所（例: デスクトップや `PDE-ARF` フォルダ内などアクセスしやすい場所）を選択します。
* **Compiler output base file name**: 出力されるインストーラファイル名を指定します（例: `PDE-ARF_Setup_v1` など。拡張子`.exe`は自動補完されます）。
* **Custom Setup icon file**: インストーラ自体のアイコンを設定します。[Browse...] からプロジェクト内の `icon_PDE-ARF.ico` を指定すると、インストーラのアイコンがアプリと同じものになります。
* **Setup password**: インストール時にパスワードを要求する場合は設定します（通常は空欄）。

#### ⑧ Inno Setup Preprocessor と コンパイルの実行
* 「Inno Setup Preprocessor (ISPP)」を利用するか聞かれることがありますが、デフォルトで [Next] をそのまま進め、最後に [Finish] をクリックします。
* ウィザード終了直後、**「Would you like to compile the new script now? (今すぐコンパイルを開始しますか？)」** と聞かれますので、**「はい (Yes)」** を選択します。
* 「コンパイル前にスクリプト（設定ファイル）を保存するか」聞かれます。次回以降、同じ設定でインストーラを再作成したい場合に備え「はい」を選び、プロジェクトフォルダ内に適当な名前（例: `setup_script.iss`）で保存しておくことをお勧めします。

### 完了
コンパイル処理が自動的に開始され、指定した出力先にセットアップ用の実行ファイル（例: `PDE-ARF_Setup_v1.exe`）が生成されます。

他の利用者に配布する際は、ソースコードや追加ファイル、`dist`フォルダ内のものを渡す必要はありません。**この生成された「セットアップ用exeファイル」を1つだけ配布すれば完了です。** 利用者が実行すると、一般的なソフトウェアのインストールと同様の画面が立ち上がり、ご自身のPCにアプリを導入することができます。
