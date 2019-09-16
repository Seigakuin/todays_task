import tkinter as tk


key = ""


def key_down(e):
    global key
    key = e.keysym


def key_up(e):
    global key
    key = ""


cx = 400
cy = 300


def main_proc():
    global cx, cy
    if key == "Up":
        cy = cy - 20
    if key == "Down":
        cy = cy + 20
    if key == "Left":
        cx = cx - 20
    if key == "Right":
        cx = cx + 20

    canvas.coords("MYCHR", cx, cy)

    root.after(100, main_proc)


root = tk.Tk()
root.title("Window")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
canvas = tk.Canvas(width=800, height=600, bg="darkgreen")
canvas.pack()

img2 = tk.PhotoImage(file="img/cardClubsA.png")
img = tk.PhotoImage(file="img/cardJoker.png")
canvas.create_image(cx, cy, image=img, tag="MYCHR")
main_proc()


root.mainloop()
