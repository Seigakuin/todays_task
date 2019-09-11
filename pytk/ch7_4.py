import tkinter as tk
import tkinter.messagebox


def click_btn():
    tkinter.messagebox.showinfo("情報", "ボタンを押しました")


root = tk.Tk()

root.title("Window")

root.geometry("400x200")

btn = tk.Button(text="テスト", command=click_btn)
btn.pack()


root.mainloop()
