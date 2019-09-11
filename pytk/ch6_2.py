import tkinter as tk

root = tk.Tk()

root.title("First Window")

root.geometry("800x600")

label = tk.Label(root, text="Hello!!!", font=("System", 24))
label.place(x=200, y=100)

root.mainloop()

