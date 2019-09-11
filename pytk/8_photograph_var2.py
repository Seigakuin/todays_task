import tkinter as tk
import random
from tkinter import ttk


# UPDATE FUNCTION
def update():
    global dice
    canvas.delete("dice1")
    canvas.create_image(100, 130, image=dice, tag="dice1")

    # canvas.delete("card2")
    # canvas.create_image(400, 130, image=card_new, tag="card2")

    # loop this function once in 100ms
    root.after(100, update)


def click_btn():
    global dice
    rand_idx = random.randint(1, 6)
    dice = dices[rand_idx]
    print(f"randomidx: {rand_idx}")
    print(f"dict {dice}")
    canvas.itemconfig("dice1", image=dice)


root = tk.Tk()
root.title("DICE!!!")

intvar = tk.IntVar()

canvas = tk.Canvas(root, width=800, height=600, bg="dark green")
canvas.pack()
dice = tk.PhotoImage(file="img/dieWhite6.png")

dices = {
    1: tk.PhotoImage(file="img/dieWhite1.png"),
    2: tk.PhotoImage(file="img/dieWhite2.png"),
    3: tk.PhotoImage(file="img/dieWhite3.png"),
    4: tk.PhotoImage(file="img/dieWhite4.png"),
    5: tk.PhotoImage(file="img/dieWhite5.png"),
    6: tk.PhotoImage(file="img/dieWhite6.png"),
}


button = tk.Button(
    root,
    text="Roll The Dice!",
    font=("Times New Roman", 24),
    command=click_btn,
    bg="blue",
)

button.place(x=150, y=600 - 50)

label = ttk.Label(root, text="Test")

label.place(x=250, y=400)

update()
root.mainloop()

