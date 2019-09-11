import tkinter as tk
import random

cnum = 0


# UPDATE FUNCTION
def draw():
    global cnum, card_new
    canvas.delete("card")
    canvas.create_image(100, 130, image=cards[cnum], tag="card")

    canvas.delete("card2")
    canvas.create_image(400, 130, image=card_new, tag="card2")

    # loop this function once in 100ms
    root.after(100, draw)


def click_btn():
    global cnum
    cnum = random.randint(0, len(cards) - 1)


def click_btn2():
    global card_new
    # card_new = tk.PhotoImage(file="img/cardBack_green5.png")
    rand_idx = random.randint(0, len(cards) - 1)
    card_new = cards[rand_idx]
    canvas.itemconfig("card2", image=card_new)


root = tk.Tk()
root.title("Card Game!")
canvas = tk.Canvas(root, width=800, height=600, bg="dark green")
canvas.pack()
card_new = tk.PhotoImage(file="img/cardBack_blue5.png")

card2 = tk.PhotoImage(file="img/cardBack_blue5.png")
cards = [
    tk.PhotoImage(file="img/cardBack_blue5.png"),
    tk.PhotoImage(file="img/cardBack_green5.png"),
    tk.PhotoImage(file="img/cardBack_red5.png"),
    tk.PhotoImage(file="img/cardClubs4.png"),
    tk.PhotoImage(file="img/cardClubsQ.png"),
    tk.PhotoImage(file="img/cardDiamondsJ.png"),
    tk.PhotoImage(file="img/cardHeartsQ.png"),
    tk.PhotoImage(file="img/cardSpadesJ.png"),
]

button = tk.Button(
    root,
    text="Get a card!",
    font=("Times New Roman", 24),
    command=click_btn,
    bg="blue",
)

button.place(x=150, y=600 - 50)

button2 = tk.Button(
    root,
    text="Get a card2!",
    font=("Times New Roman", 24),
    command=click_btn2,
    bg="blue",
)

button2.place(x=450, y=600 - 50)

draw()
root.mainloop()

