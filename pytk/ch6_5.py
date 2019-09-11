import tkinter as tk

root = tk.Tk()

root.title("My Window")

root.resizable(False, False)

canvas = tk.Canvas(root, width=400, height=600, bg="green")
canvas.pack()


button = tk.Button(root, text="Get a card!", font=("Times New Roman", 24))

button.place(x=150, y=600 - 50)


card1 = tk.PhotoImage(file="img/cardClubs2.png")
card2 = tk.PhotoImage(file="img/cardDiamonds10.png")
canvas.create_image(100, 130, image=card1)
canvas.create_image(300, 130, image=card2)


root.mainloop()

