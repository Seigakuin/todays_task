"""Dice 7 - サイコロの数値を表示しよう！
テーマ：
- サイコロ画像の下にそのサイコロの数値を表示する

手順：
- Global変数の中にdice1_number, dice2_numberを作成
- draw()ファンクションの中にscreen.draw.textを使い、dice1_numberを表示
    - 数値はテキストでないのでstr()で文字に変換していることに注意！
- on_key_downの中
    - globalの中にdice1_numberを追加
    - if構文の中にdice1_numberを変更するコードを記述

課題：　
- 赤いサイコロも同様の処理をする

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

dice1_number = 1
dice2_number = 1

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

    screen.draw.text(
        str(dice1_number),
        (WIDTH // 2 - 100, HEIGHT // 2 + 80),
        fontsize=80,
        anchor=(0.5, 0.5)
    )


def on_key_down(key):
    # globalを設定することによって、コードの上に書いたdice1変数を「読む」だけでなく
    # 内容を「書く」(書き換える)ことができる
    global dice1, dice1_number

    if key == keys.UP:
        # ランダムな数値を入れておく変数
        number1 = random.randint(0, 5)
        dice1 = DICE_LIST1[number1]
        dice1_number = number1 + 1