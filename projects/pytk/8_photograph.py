import tkinter as tk

cnum = 0


def draw():
    global cnum
    canvas.delete("card")
    canvas.create_image(100, 130, image=cards[cnum], tag="card")
    cnum = cnum + 1
    if cnum >= len(cards):
        cnum = 0
    root.after(2000, draw)


root = tk.Tk()
root.title("Card Game!")
canvas = tk.Canvas(root, width=800, height=600, bg="dark green")
canvas.pack()

cards = [
    tk.PhotoImage(file="img/cardBack_blue5.png"),
    tk.PhotoImage(file="img/cardBack_green5.png"),
    tk.PhotoImage(file="img/cardBack_red5.png"),
]

draw()
root.mainloop()

