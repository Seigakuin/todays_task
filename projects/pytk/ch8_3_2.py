import tkinter as tk


key = ""


def key_down(e):
    global key
    key = e.keysym


def main_proc():
    label["text"] = key
    root.after(100, main_proc)


root = tk.Tk()
root.title("Window")
root.bind("<KeyPress>", key_down)
label = tk.Label(font=("Times New Roman", 80))
label.pack()
main_proc()


root.mainloop()
