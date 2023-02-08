import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkcalendar import Calendar, DateEntry

# トップページ
class MainPage(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)

        self.label = ttk.Label(self, text="メモ帳へようこそ！")

        # メモ作成ページに遷移するボタン
        self.button_new_page = ttk.Button(self, text="症状を記録する", command=lambda:changePage(master.new_page))
        self.button_new_page.pack()

        # メモ読み返しに遷移するボタン
        self.button_change_page = ttk.Button(self, text="記録を見返す", command=lambda:changePage(master.read_page))
        self.button_change_page.pack()

# メモ作成ページ
class NewPage(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)

        # ラベル
        self.label = ttk.Label(self, text="症状を記録しましょう")
        self.label.pack()

        # 日付選択
        self.date = DateEntry(self)
        self.date.pack();

        # テキスト
        self.text_memo = tk.Text(self, width=40, height=3)
        self.text_memo.pack()

        # 結果
        self.label_result = ttk.Label(self, text="")
        self.label_result.pack()

        # 保存ボタン
        self.button_save_file = ttk.Button(self, text="保存", command=self.save_file)
        self.button_save_file.pack()

        self.button_back = ttk.Button(self, text="戻る", command=lambda:changePage(master.main_page))
        self.button_back.pack()

    # ファイル保存
    def save_file(self):
#         ftypes = [("テキスト", ".txt")]
        ini_fname = self.date.get_date().strftime('%Y-%m-%d') + ".txt"
        file = filedialog.asksaveasfile(defaultextension=".txt", initialfile=ini_fname)

        if file:
            # テキストの内容を読み込む
            text_content = self.text_memo.get("1.0", tk.END)
            file.write(text_content)
            file.close()
            self.text_memo.delete("1.0", tk.END)
            self.label_result['text'] = '保存しました！'

# メモ読込ページ
class ReadPage(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)

        self.label = ttk.Label(self, text="症状を読み込みます")
        self.label.pack()

        self.button_read_file = ttk.Button(self, text="読み込む", command=self.open_file)
        self.button_read_file.pack()

        # テキスト
        self.text_memo = tk.Text(self, width=40, height=3)
        self.text_memo.pack()

        self.button_back = ttk.Button(self, text="戻る", command=lambda:changePage(master.main_page))
        self.button_back.pack()

    def open_file(self):
        file = filedialog.askopenfile(defaultextension=".txt")
        if file:
            self.text_memo.delete("1.0", tk.END)
            self.text_memo.insert("1.0", file.read())
            file.close()

# アプリケーションクラス
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # ウィンドウサイズの設定
        self.geometry("640x480")

        self.title("メモ帳アプリ")

        # ウィンドウのグリッドを 1x1 にする
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # メインページ
        self.main_page = MainPage(self)
        self.main_page.grid(row=0, column=0, sticky="nsew")

        # メモ作成ページ
        self.new_page = NewPage(self)
        self.new_page.grid(row=0, column=0, sticky="nsew")

        # メモ読込ページ
        self.read_page = ReadPage(self)
        self.read_page.grid(row=0, column=0, sticky="nsew")

        # メインページを前面に出しておく
        self.main_page.tkraise()

# ページの移動
def changePage(page):
    page.tkraise()

if __name__ == "__main__":
    # アプリケーションを開始
    app = App()
    app.mainloop()