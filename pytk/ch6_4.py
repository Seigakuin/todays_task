import tkinter as tk


root = tk.Tk()

root.title("My Window")

canvas = tk.Canvas(root, width=400, height=600, bg="skyblue")

canvas.pack()

gazou = tk.PhotoImage(file="img/cardClubs2.png")

canvas.create_image(200, 300, image=gazou)

root.mainloop()

