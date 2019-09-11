import tkinter as tk
import tkinter.messagebox

root = tk.Tk()
root.title("Window")

root.resizable(False, False)

canvas = tk.Canvas(root, width=800, height=600, bg="darkgreen")
canvas.pack()

gazou = tk.PhotoImage(file="img/cardJoker.png")
canvas.create_image(150, 200, image=gazou)

button = tk.Button(text="診断する", font=("Times New Roman", 32), bg="lightgreen")
button.place(x=400, y=480)

text = tk.Text(width=40, height=5, font=("Times New Roman", 16))
text.place(x=320, y=30)

root.mainloop()
