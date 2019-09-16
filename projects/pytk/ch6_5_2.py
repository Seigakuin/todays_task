import tkinter as tk

cards = {
    "d7": "cardDiamonds7.png",
    "s8": "cardSpades8.png",
    "c2": "cardClubs2.png",
    "d10": "cardDiamonds10.png",
}


def click_btn():
    # canvas.delete("all")
    card1 = tk.PhotoImage(file="img/" + cards["s8"])
    canvas.itemconfig("card1", image=card1)

    # canvas.create_image(200, 130, image=card1)
    # canvas.update()
    print("Clicked")


def draw():
    canvas.delete("card1")
    card1 = tk.PhotoImage(file="img/" + cards["c2"])
    canvas.create_image(100, 130, image=card1, tag="card1")
    root.after(100, draw)


root = tk.Tk()

root.title("Card Game!")

# root.resizable(False, False)

canvas = tk.Canvas(root, width=400, height=600, bg="dark green")
canvas.pack()

# card1 = tk.PhotoImage(file="img/" + cards["d7"])
# card2 = tk.PhotoImage(file="img/" + cards["s8"])


button = tk.Button(
    root,
    text="Get a card!",
    font=("Times New Roman", 24),
    command=click_btn,
    bg="blue",
)

button.place(x=150, y=600 - 50)


# canvas.create_image(100, 130, image=card1, tag="card1")
# canvas.create_image(300, 130, image=card2, tag="card2")

# label = tk.Label(root, image=card1)
# label.pack()


# card1 = tk.PhotoImage(file="img/" + cards["d7"])
# card2 = tk.PhotoImage(file="img/" + cards["s8"])
# canvas.create_image(100, 130, image=card1)
# canvas.create_image(300, 130, image=card2)
# click_btn()

draw()
root.mainloop()

