import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

import docx
from tkinter import filedialog
import time
import os

ctk.set_appearance_mode("dork")
ctk.set_default_color_theme("blue")

# 関連変数の定義
flag_mode = 0
flag_use = 1
ward_use = ""
va1 = ["購入", "使用"]

font_body = ("FOT-筑紫B丸ゴシック Std R", 16)
main_bg_color = "aliceblue"
main_fg_color = "white"


def button_end():
    me_end = tk.messagebox.askyesno("終了の確認", "プログラムを終了しますか？")
    if me_end:
        root.destroy()


def button_enter():
    global ward_use
    if flag_use == 1:
        ward_use = "購入"
    elif flag_use == 2:
        ward_use = "使用"
    else:
        tk.messagebox.showerror("エラー", "コンボボックス内をすべて揃えてください。")
        return 0

    # 使用するPDMを指定
    doc = docx.Document("PDM_ARF-001.docx")

    # 会計要望書の追記
    # 日付出力
    doc.paragraphs[0].text = en0_1.get()
    # 団体名出力
    doc.paragraphs[5].text = "東京電機大学東京千住キャンパス" + en0_2.get()
    # 代表者名出力
    doc.paragraphs[7].text = "代表　　" + en0_3_1.get() + "　" + en0_3_2.get()
    # 会計担当者名出力
    doc.paragraphs[8].text = "会計　　" + en0_4_1.get() + "　" + en0_4_2.get()
    # チェックボックス出力
    if cb0_1.get() == 1:
        t = doc.paragraphs[12].text
        t = t.replace("□", "☑")
        doc.paragraphs[12].text = t
    if cb0_2.get() == 1:
        t = doc.paragraphs[13].text
        t = t.replace("□", "☑")
        doc.paragraphs[13].text = t
    if cb0_3.get() == 1:
        t = doc.paragraphs[14].text
        t = t.replace("□", "☑")
        doc.paragraphs[14].text = t
    if cb0_4.get() == 1:
        t = doc.paragraphs[15].text
        t = t.replace("□", "☑")
        doc.paragraphs[15].text = t
    if cb0_5.get() == 1:
        t = doc.paragraphs[16].text
        t = t.replace("□", "☑")
        doc.paragraphs[16].text = t
    if cb0_6.get() == 1:
        t = doc.paragraphs[17].text
        t = t.replace("□", "☑")
        doc.paragraphs[17].text = t
    if cb0_7.get() == 1:
        t = doc.paragraphs[18].text
        t = t.replace("□", "☑")
        doc.paragraphs[18].text = t
    # 要件出力
    doc.paragraphs[20].text = te0_1.get("1.0", "end-1c")

    if flag_mode == 0:
        # 品名出力
        doc.paragraphs[25].text = "　　　　　　　　　　　品名　　　" + en1_1.get()
        # 金額出力
        doc.paragraphs[26].text = "　　　　　　　　　　　金額　　　\\" + en1_2.get() + "-"
        # 購入予定日出力
        doc.paragraphs[27].text = "　　　　　　　　　" + ward_use + "予定日　　" + en1_3.get()
        # 購入理由出力
        doc.paragraphs[28].text = "　　　　　　　　　" + ward_use + "理由　　　" + te1_1.get("1.0", "end-1c")
    elif flag_mode == 1:
        # 見積金額（往復）出力
        doc.paragraphs[25].text = "　　　　見積金額（往復）　　　　\\" + en2_1.get() + "-"
        # 使用月日出力
        doc.paragraphs[26].text = "　　　　使用月日　　　　　　　　" + en2_2.get()
        # 使用経路（往復）出力
        doc.paragraphs[27].text = "　　　　使用理由　　　　　　　　" + te2_1.get("1.0", "end-1c")
        doc.paragraphs[28].text = "　　　　使用経路（往復）　　　　" + en2_3.get()
        doc.paragraphs[29].insert_paragraph_before("　　　　　　　　　　　　　　　　" + en2_4.get())
        doc.paragraphs[29].insert_paragraph_before("　　　　　　　　　　　　　　　　" + en2_5.get())
        doc.paragraphs[29].insert_paragraph_before("　　　　　　　　　　　　　　　　" + en2_6.get())
        doc.paragraphs[29].insert_paragraph_before("　　　　　　　　　　　　　　　　" + en2_7.get())
    elif flag_mode == 2:
        # 車種出力
        doc.paragraphs[25].text = "　　　　　　　　　　　車種　　　　　" + en3_1.get()
        # 見積金額出力
        doc.paragraphs[26].text = "　　　　　　　　　見積金額　　　　　\\" + en3_2.get() + "-"
        # ガソリン代出力
        doc.paragraphs[27].text = "　　　　　　　　　ガソリン代　　　　\\" + en3_3.get() + "-"
        # 高速道路代出力
        doc.paragraphs[28].text = "　　　　　　　　　高速道路代　　　　\\" + en3_4.get() + "-"
        # 使用予定日出力
        doc.paragraphs[29].insert_paragraph_before("　　　　　　　　　使用予定日　　　　" + en3_5.get())
        # 使用経路出力
        doc.paragraphs[29].insert_paragraph_before("　　　　　　　　　使用経路（往復）　" + en3_6.get())
        # 使用理由
        doc.paragraphs[29].insert_paragraph_before("　　　　　　　　　使用理由　　　　　" + te3_1.get("1.0", "end-1c"))
    else:
        tk.messagebox.showerror("エラー", "エラーが発生しました。設定を変更してください。")
        return 0

    # 文書の保存
    file_name = filedialog.asksaveasfilename(title="作成する文書の保存",
                                             initialfile=time.strftime("%Y_%m%d_") + "会計要望書",
                                             defaultextension=".docx",
                                             filetypes=[("Word 文書", ".docx")])
    doc.save(file_name)

    # 保存した文書を開く（.docxを開く設定を行っているアプリケーションで）
    os.startfile(file_name)

    root.destroy()


# ウィンドウの様式を変更する関数（汎用仕様）
def button_change1():
    global flag_mode
    flag_mode = 0
    bu_change1.configure(fg_color="black", hover_color="black", state="disabled")
    bu_change2.configure(fg_color="white", hover_color="whitesmoke", text_color="black", state="normal")
    bu_change3.configure(fg_color="white", hover_color="whitesmoke", text_color="black", state="normal")

    fr_mode2.grid_forget()
    fr_mode3.grid_forget()
    fr_mode1.grid(column=0, row=14, columnspan=3, padx=20, pady=10)

    cb0_1.configure(state=tk.NORMAL)
    # cb0_2.configure(state=tk.DISABLED, text_color_disabled="gray")
    cb0_2.configure(state=tk.DISABLED)
    cb0_3.configure(state=tk.NORMAL)
    cb0_4.configure(state=tk.NORMAL)
    cb0_5.configure(state=tk.NORMAL)
    cb0_6.configure(state=tk.NORMAL)

    cb0_2.deselect()


# ウィンドウの様式を変更する関数（交通費（電車・バス）仕様）
def button_change2():
    global flag_mode
    flag_mode = 1
    bu_change1.configure(fg_color="white", hover_color="whitesmoke", text_color="black", state="normal")
    bu_change2.configure(fg_color="black", hover_color="black", state="disabled")
    bu_change3.configure(fg_color="white", hover_color="whitesmoke", state="normal")

    fr_mode1.grid_forget()
    fr_mode3.grid_forget()
    fr_mode2.grid(column=0, row=14, columnspan=3, padx=20, pady=10)

    cb0_1.configure(state=tk.DISABLED)
    # cb0_2.configure(state=tk.DISABLED, text_color_disabled="black")
    cb0_2.configure(state=tk.DISABLED)
    cb0_3.configure(state=tk.DISABLED)
    cb0_4.configure(state=tk.DISABLED)
    cb0_5.configure(state=tk.DISABLED)
    cb0_6.configure(state=tk.DISABLED)

    cb0_1.deselect()
    cb0_2.select()
    cb0_3.deselect()
    cb0_4.deselect()
    cb0_5.deselect()
    cb0_6.deselect()


# ウィンドウの様式を変更する関数（交通費（レンタカー）仕様）
def button_change3():
    global flag_mode
    flag_mode = 2
    bu_change1.configure(fg_color="white", hover_color="whitesmoke", text_color="black", state="normal")
    bu_change2.configure(fg_color="white", hover_color="whitesmoke", state="normal")
    bu_change3.configure(fg_color="black", hover_color="black", state="disabled")

    fr_mode1.grid_forget()
    fr_mode2.grid_forget()
    fr_mode3.grid(column=0, row=14, columnspan=3, padx=20, pady=10)

    cb0_1.configure(state=tk.DISABLED)
    # cb0_2.configure(state=tk.DISABLED, text_color_disabled="black")
    cb0_2.configure(state=tk.DISABLED)
    cb0_3.configure(state=tk.DISABLED)
    cb0_4.configure(state=tk.DISABLED)
    cb0_5.configure(state=tk.DISABLED)
    cb0_6.configure(state=tk.DISABLED)

    cb0_1.deselect()
    cb0_2.select()
    cb0_3.deselect()
    cb0_4.deselect()
    cb0_5.deselect()
    cb0_6.deselect()


# コンボボックスを選択すると起動する関数
def combo_select(e):
    global flag_use
    co1_int = co2_int = co3_int = co4_int = 0
    for i in range(0, len(va1)):
        if co1_1.get() == va1[i]:
            co1_int = i
        if co1_2.get() == va1[i]:
            co2_int = i
        if co1_3.get() == va1[i]:
            co3_int = i
        if co1_4.get() == va1[i]:
            co4_int = i
    if co1_int == co2_int == co3_int == co4_int == 0:
        flag_use = 1
    elif co1_int == co2_int == co3_int == co4_int == 1:
        flag_use = 2
    else:
        flag_use = 0


# ウィンドウ上でマウスホイールを回すとスクロールバーが移動する関数
def mouse_y_scroll(event):
    if event.delta < 0:
        canvas.yview_scroll(1, "units")
    else:
        canvas.yview_scroll(-1, "units")


# 汎用会計要望書入力要求ウィンドウの仕様設定
root = ctk.CTk()
root.title("会計要望書生成")
root.geometry("800x800")
root.resizable(False, True)
root.bind("<MouseWheel>", mouse_y_scroll)

# スクロールバー関連
frame = tk.Frame(root, bg=main_bg_color)
frame.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(frame, bg=main_bg_color)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar_y = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar_y.set)

scrollable_frame = ctk.CTkFrame(canvas, fg_color=main_bg_color, width=800, height=1250)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

scrollable_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# ボタンを配置するフレーム
fr_button = ctk.CTkFrame(scrollable_frame, fg_color=main_bg_color, width=800, height=50)
fr_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

# 入力関連ウィジェット（共通部分）を配置するフレーム
fr_body = ctk.CTkFrame(scrollable_frame, fg_color=main_fg_color, width=600, corner_radius=10)
fr_body.place(relx=0.5, y=120, anchor=tk.N)

# 入力関連ウィジェット（汎用仕様部分）を配置するフレーム
fr_mode1 = ctk.CTkFrame(fr_body, fg_color=main_fg_color)
fr_mode1.grid(column=0, row=14, columnspan=3, padx=20, pady=10)

# 入力関連ウィジェット（交通費（電車・バス）仕様部分）を配置するフレーム
fr_mode2 = ctk.CTkFrame(fr_body, fg_color=main_fg_color)
# 入力関連ウィジェット（交通費（レンタカー）仕様部分）を配置するフレーム
fr_mode3 = ctk.CTkFrame(fr_body, fg_color=main_fg_color)

# タイトル
la_title = ctk.CTkLabel(scrollable_frame, text="会計要望書生成", font=("FOT-筑紫B丸ゴシック Std R", 60))
la_title.place(relx=0.5, y=50, anchor=tk.CENTER)

# fr_bodyに配置する入力関連ウィジェットの作成
la0_1 = ctk.CTkLabel(fr_body, text="要望書生成を提出する日付を入力してください。", font=font_body)
en0_1 = ctk.CTkEntry(fr_body, width=200, placeholder_text="例：令和6年1月1日")
la0_2 = ctk.CTkLabel(fr_body, text="団体名を入力してください。", font=font_body)
en0_2 = ctk.CTkEntry(fr_body, width=200, placeholder_text="例：新聞委員会")
la0_3 = ctk.CTkLabel(fr_body, text="代表者名を入力してください。", font=font_body)
en0_3_1 = ctk.CTkEntry(fr_body, width=100, placeholder_text="代表者の名字")
en0_3_2 = ctk.CTkEntry(fr_body, width=100, placeholder_text="代表者の名前")
la0_4 = ctk.CTkLabel(fr_body, text="会計担当者名を入力してください。", font=font_body)
en0_4_1 = ctk.CTkEntry(fr_body, width=100, placeholder_text="担当者の名字")
en0_4_2 = ctk.CTkEntry(fr_body, width=100, placeholder_text="担当者の名前")
la0_5 = ctk.CTkLabel(fr_body, text="要望書の用件を以下から選んでください。", font=font_body)
cb0_1 = ctk.CTkCheckBox(fr_body, text="遠征等で資材などの運搬を依頼する時", font=font_body)
cb0_2 = ctk.CTkCheckBox(fr_body, text="交通機関を用いた移動費として使用する時（電車・バス等）", font=font_body, state=tk.DISABLED)
cb0_3 = ctk.CTkCheckBox(fr_body, text="領収書単位で税抜き５万円を超えている場合", font=font_body)
cb0_4 = ctk.CTkCheckBox(fr_body, text="銀行振り込み等で領収証が発行できないとき恐れがある場合", font=font_body)
cb0_5 = ctk.CTkCheckBox(fr_body, text="三部会四委員会が郵送代・飲食費を交際費として使用したい場合", font=font_body)
cb0_6 = ctk.CTkCheckBox(fr_body, text="自治会費で購入してよいか迷ったとき", font=font_body)
cb0_7 = ctk.CTkCheckBox(fr_body, text="その他", font=font_body)
la0_6 = ctk.CTkLabel(fr_body, text="要望内容を入力してください。", font=font_body)
te0_1 = ctk.CTkTextbox(fr_body, width=600, height=75, font=font_body)

# fr_mode1に配置する入力関連ウィジェットの作成
co1_1 = ctk.CTkComboBox(fr_mode1, state="readonly", values=va1, font=font_body, width=75, command=combo_select)
la1_1 = ctk.CTkLabel(fr_mode1, text="する物の品名を入力してください。", font=font_body)
en1_1 = ctk.CTkEntry(fr_mode1, width=200, placeholder_text="例：カメラ")
co1_2 = ctk.CTkComboBox(fr_mode1, state="readonly", values=va1, font=font_body, width=75, command=combo_select)
la1_2 = ctk.CTkLabel(fr_mode1, text="する物の合計金額を入力してください。", font=font_body)
en1_2 = ctk.CTkEntry(fr_mode1, width=200, placeholder_text="例：350,000")
co1_3 = ctk.CTkComboBox(fr_mode1, state="readonly", values=va1, font=font_body, width=75, command=combo_select)
la1_3 = ctk.CTkLabel(fr_mode1, text="予定日を入力してください。", font=font_body)
en1_3 = ctk.CTkEntry(fr_mode1, width=200, placeholder_text="例：1月31日")
co1_4 = ctk.CTkComboBox(fr_mode1, state="readonly", values=va1, font=font_body, width=75, command=combo_select)
la1_4 = ctk.CTkLabel(fr_mode1, text="する理由を入力してください。", font=font_body)
te1_1 = ctk.CTkTextbox(fr_mode1, width=600, height=60, font=font_body)

# fr_mode1のコンボボックス関連設定
co1_1.set(va1[0])
co1_2.set(va1[0])
co1_3.set(va1[0])
co1_4.set(va1[0])

# fr_mode2に配置する入力関連ウィジェットの作成
la2_1 = ctk.CTkLabel(fr_mode2, text="往復分の合計見積金額を入力してください。", font=font_body)
en2_1 = ctk.CTkEntry(fr_mode2, width=200, placeholder_text="例：10,000")
la2_2 = ctk.CTkLabel(fr_mode2, text="使用予定日を入力してください。", font=font_body)
en2_2 = ctk.CTkEntry(fr_mode2, width=200, placeholder_text="例：1月31日")
la2_3 = ctk.CTkLabel(fr_mode2, text="使用理由を入力してください。", font=font_body)
te2_1 = ctk.CTkTextbox(fr_mode2, width=600, height=60, font=font_body)
la2_4 = ctk.CTkLabel(fr_mode2, text="往復分の乗車経路を入力してください。", font=font_body)
en2_3 = ctk.CTkEntry(fr_mode2, width=280, placeholder_text="例：北千住→日暮里→池袋→高坂")
en2_4 = ctk.CTkEntry(fr_mode2, width=280)
en2_5 = ctk.CTkEntry(fr_mode2, width=280)
en2_6 = ctk.CTkEntry(fr_mode2, width=280)
en2_7 = ctk.CTkEntry(fr_mode2, width=600)

# fr_mode3に配置する入力関連ウィジェットの作成
la3_1 = ctk.CTkLabel(fr_mode3, text="使用する車種を入力してください。", font=font_body)
en3_1 = ctk.CTkEntry(fr_mode3, width=200, placeholder_text="例：乗用自動車")
la3_2 = ctk.CTkLabel(fr_mode3, text="合計見積金額を入力してください。", font=font_body)
en3_2 = ctk.CTkEntry(fr_mode3, width=200, placeholder_text="例：50,000")
la3_3 = ctk.CTkLabel(fr_mode3, text="ガソリン代の見積金額を入力してください。", font=font_body)
en3_3 = ctk.CTkEntry(fr_mode3, width=200, placeholder_text="例：20,000")
la3_4 = ctk.CTkLabel(fr_mode3, text="高速道路代の見積金額を入力してください。", font=font_body)
en3_4 = ctk.CTkEntry(fr_mode3, width=200, placeholder_text="例：5,000")
la3_5 = ctk.CTkLabel(fr_mode3, text="使用予定日を入力してください。", font=font_body)
en3_5 = ctk.CTkEntry(fr_mode3, width=200, placeholder_text="例：1月31日")
la3_6 = ctk.CTkLabel(fr_mode3, text="乗車経路（往復）を入力してください。", font=font_body)
en3_6 = ctk.CTkEntry(fr_mode3, width=600, placeholder_text="例：北千住→東京電機大学埼玉鳩山キャンパス")
la3_7 = ctk.CTkLabel(fr_mode3, text="使用理由を入力してください。", font=font_body)
te3_1 = ctk.CTkTextbox(fr_mode3, width=600, height=60, font=font_body)

# fr_bodyに配置する入力関連ウィジェットの配置
la0_1.grid(column=0, row=0, sticky="w", padx=20, pady=10)
en0_1.grid(column=1, row=0, columnspan=2, padx=20, pady=10)
la0_2.grid(column=0, row=1, sticky="w", padx=20, pady=10)
en0_2.grid(column=1, row=1, columnspan=2, padx=20, pady=10)
la0_3.grid(column=0, row=2, sticky="w", padx=20, pady=10)
en0_3_1.grid(column=1, row=2, padx=0, pady=10)
en0_3_2.grid(column=2, row=2, padx=20, pady=10)
la0_4.grid(column=0, row=3, sticky="w", padx=20, pady=10)
en0_4_1.grid(column=1, row=3, padx=0, pady=10)
en0_4_2.grid(column=2, row=3, padx=20, pady=10)
la0_5.grid(column=0, row=4, sticky="w", columnspan=3, padx=20, pady=10)
cb0_1.grid(column=0, row=5, sticky="w", columnspan=3, padx=50, pady=5)
cb0_2.grid(column=0, row=6, sticky="w", columnspan=3, padx=50, pady=5)
cb0_3.grid(column=0, row=7, sticky="w", columnspan=3, padx=50, pady=5)
cb0_4.grid(column=0, row=8, sticky="w", columnspan=3, padx=50, pady=5)
cb0_5.grid(column=0, row=9, sticky="w", columnspan=3, padx=50, pady=5)
cb0_6.grid(column=0, row=10, sticky="w", columnspan=3, padx=50, pady=5)
cb0_7.grid(column=0, row=11, sticky="w", columnspan=3, padx=50, pady=5)
la0_6.grid(column=0, row=12, sticky="w", padx=20, pady=10)
te0_1.grid(column=0, row=13, sticky="w", columnspan=3, padx=20, pady=10)

# fr_mode1に配置する入力関連ウィジェットの配置
co1_1.grid(column=0, row=0, sticky="w", pady=10)
la1_1.grid(column=1, row=0, sticky="w", pady=10)
en1_1.grid(column=2, row=0, sticky="e", pady=10)
co1_2.grid(column=0, row=1, sticky="w", pady=10)
la1_2.grid(column=1, row=1, sticky="w", pady=10)
en1_2.grid(column=2, row=1, sticky="e", pady=10)
co1_3.grid(column=0, row=2, sticky="w", pady=10)
la1_3.grid(column=1, row=2, sticky="w", pady=10)
en1_3.grid(column=2, row=2, sticky="e", pady=10)
co1_4.grid(column=0, row=3, sticky="w", pady=10)
la1_4.grid(column=1, row=3, sticky="w", pady=10)
te1_1.grid(column=0, row=4, sticky="w", columnspan=3, pady=10)

# fr_mode2に配置する入力関連ウィジェットの配置
la2_1.grid(column=0, row=0, sticky="w", pady=10)
en2_1.grid(column=1, row=0, sticky="e", pady=10)
la2_2.grid(column=0, row=1, sticky="w", pady=10)
en2_2.grid(column=1, row=1, sticky="e", pady=10)
la2_3.grid(column=0, row=2, sticky="w", pady=10)
te2_1.grid(column=0, row=3, sticky="w", columnspan=2, pady=5)
la2_4.grid(column=0, row=4, sticky="w", pady=5)
en2_3.grid(column=0, row=5, sticky="w", pady=5)
en2_4.grid(column=1, row=5, sticky="e", pady=5)
en2_5.grid(column=0, row=6, sticky="w", pady=5)
en2_6.grid(column=1, row=6, sticky="e", pady=5)
en2_7.grid(column=0, row=7, sticky="w", columnspan=2, pady=5)

# fr_mode3に配置する入力関連ウィジェットの配置
la3_1.grid(column=0, row=0, sticky="w", pady=5)
en3_1.grid(column=1, row=0, sticky="e", pady=5)
la3_2.grid(column=0, row=1, sticky="w", pady=5)
en3_2.grid(column=1, row=1, sticky="e", pady=5)
la3_3.grid(column=0, row=2, sticky="w", pady=5)
en3_3.grid(column=1, row=2, sticky="e", pady=5)
la3_4.grid(column=0, row=3, sticky="w", pady=5)
en3_4.grid(column=1, row=3, sticky="e", pady=5)
la3_5.grid(column=0, row=4, sticky="w", pady=5)
en3_5.grid(column=1, row=4, sticky="e", pady=5)
la3_6.grid(column=0, row=5, sticky="w", pady=5)
en3_6.grid(column=0, row=6, sticky="e", columnspan=2, pady=5)
la3_7.grid(column=0, row=7, sticky="w", pady=5)
te3_1.grid(column=0, row=8, sticky="w", columnspan=2, pady=5)


# 各種ボタンの作成
bu_change1 = ctk.CTkButton(fr_button, text="汎用",
                           font=("游ゴシック", 20, "bold"), text_color="white",
                           width=70, height=40, corner_radius=0, border_width=1,
                           fg_color="black", hover_color="black", text_color_disabled="white",
                           command=button_change1, state="disabled")
bu_change2 = ctk.CTkButton(fr_button, text="交通費(電車・バス)",
                           font=("游ゴシック", 20, "bold"), text_color="black",
                           width=200, height=40, corner_radius=0, border_width=1,
                           fg_color="white", hover_color="whitesmoke", text_color_disabled="white",
                           command=button_change2)
bu_change3 = ctk.CTkButton(fr_button, text="交通費(レンタカー)",
                           font=("游ゴシック", 20, "bold"), text_color="black",
                           width=200, height=40, corner_radius=0,  border_width=1,
                           fg_color="white", hover_color="whitesmoke", text_color_disabled="white",
                           command=button_change3)
bu_enter = ctk.CTkButton(fr_button, text="入力",
                         font=("游ゴシック", 20, "bold"), text_color="white",
                         width=70, height=40,
                         fg_color="mediumseagreen", hover_color="seagreen",
                         command=button_enter)
bu_end = ctk.CTkButton(fr_button, text="終了",
                       font=("游ゴシック", 20, "bold"), text_color="white",
                       width=70, height=40,
                       fg_color="red", hover_color="crimson",
                       command=button_end)

# 各種ボタンの配置
bu_change1.grid(column=0, row=0, padx=10)
bu_change2.grid(column=1, row=0, padx=10)
bu_change3.grid(column=2, row=0, padx=10)
bu_enter.grid(column=3, row=0, padx=10)
bu_end.grid(column=4, row=0, padx=10)

root.mainloop()
