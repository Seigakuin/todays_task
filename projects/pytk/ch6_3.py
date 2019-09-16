import tkinter as tk


def click_btn():
    button["text"] = "Clicked!!!"


root = tk.Tk()

root.title("First Window")

root.geometry("800x600")


button = tk.Button(
    root,
    text="This is a button!",
    font=("Times New Roman", 24),
    command=click_btn,
)

button.place(x=200, y=100)

root.mainloop()

