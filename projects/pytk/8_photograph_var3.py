import tkinter as tk
import random
from tkinter import ttk


# Create root
root = tk.Tk()

# Set title of Window
root.title("DICE!!!")

# Create Canvas Widget
canvas = tk.Canvas(root, width=800, height=600, bg="dark green")

# Add to the window
canvas.pack()

# Get Screen width and height
SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()
print(f"screen_width {SCREEN_WIDTH}")
print(f"screen_height {SCREEN_HEIGHT}")

root.update()
CANVAS_WIDTH = canvas.winfo_width()
CANVAS_HEIGHT = canvas.winfo_height()
print(f"canvas_width {CANVAS_WIDTH}")
print(f"canvas_height {CANVAS_HEIGHT}")


key = ""

# UPDATE FUNCTION
def update():
    global dice, key
    canvas.delete("dice1")
    canvas.create_image(100, 130, image=dice, tag="dice1")

    root.after(100, update)


def key_down(e):
    global key
    key = e.keysym
    stringvar.set(key)


def click_btn():
    global dice
    rand_idx = random.randint(1, 6)
    dice = dices[rand_idx]
    print(f"randomidx: {rand_idx}")
    print(f"dict {dice}")
    canvas.itemconfig("dice1", image=dice)


intvar = tk.IntVar()
stringvar = tk.StringVar()


dice = tk.PhotoImage(file="img/dieWhite6.png")

dices = {
    1: tk.PhotoImage(file="img/dieWhite1.png"),
    2: tk.PhotoImage(file="img/dieWhite2.png"),
    3: tk.PhotoImage(file="img/dieWhite3.png"),
    4: tk.PhotoImage(file="img/dieWhite4.png"),
    5: tk.PhotoImage(file="img/dieWhite5.png"),
    6: tk.PhotoImage(file="img/dieWhite6.png"),
}

label2 = tk.Label(root, font=("Times New Roman", 40), textvariable=stringvar)
# label2["text"] = intvar
label2.place(x=100, y=400)


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

root.bind("<KeyPress>", key_down)

update()
root.mainloop()

