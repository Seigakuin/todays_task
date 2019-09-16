import tkinter as tk


def click_btn():
    txt = entry.get()
    button["text"] = txt


root = tk.Tk()

root.title("Window")

root.geometry("400x200")

entry = tk.Entry(width=20)
entry.place(x=10, y=10)

button = tk.Button(text="Get String!", command=click_btn)
button.place(x=20, y=100)


root.mainloop()
