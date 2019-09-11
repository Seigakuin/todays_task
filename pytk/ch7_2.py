import tkinter as tk


def click_btn():
    text.insert(tk.END, "え〜〜〜！")


root = tk.Tk()

root.title("Window")

root.geometry("400x200")


button = tk.Button(text="Insert String!", command=click_btn)
button.pack()

text = tk.Text()
text.pack()


root.mainloop()
