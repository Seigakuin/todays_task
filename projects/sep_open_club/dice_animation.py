"""Dice 5
テーマ：


手順：


課題：　

https://pygame-zero.readthedocs.io/en/stable/hooks.html#buttons-and-keys

"""
import random

# Global 変数をここに記述
WIDTH = 800
HEIGHT = 600
TITLE = "Dice!!!"

DICE_LIST1 = [
    Actor("dice/die_white1"),
    Actor("dice/die_white2"),
    Actor("dice/die_white3"),
    Actor("dice/die_white4"),
    Actor("dice/die_white5"),
    Actor("dice/die_white6")
]


DICE_LIST2 = [
    Actor("dice/die_red1"),
    Actor("dice/die_red2"),
    Actor("dice/die_white3"),
    Actor("dice/die_white4"),
    Actor("dice/die_white5"),
    Actor("dice/die_white6")
]


# DICE_LIST1の①番目にある画像を表示
dice1 = DICE_LIST1[0]

dice2 = DICE_LIST2[0]



def draw():
    screen.fill((80, 148, 75))
    screen.draw.text(
        "DICE!!!",
        (WIDTH // 2, 100),
        fontsize=60,
        anchor=(0.5, 0.5)

    )

    # Actorインスタンスのcenter位置を設定
    dice1.center = (WIDTH // 2 - 100, HEIGHT // 2)
    dice2.center = (WIDTH // 2 + 100, HEIGHT // 2)
    dice1.draw()
    dice2.draw()

def on_key_down(key):
    global dice1






    if key == keys.UP:
        dice1.angle = 0
        animate(dice1, tween="bounce_end",duration=0.9, angle=(360), on_finished=choose_dice)






def choose_dice():
    global dice1
    number = random.randint(0, 5)
    dice1 = DICE_LIST1[number]
    dice1.angle=0


