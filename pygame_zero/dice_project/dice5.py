"""Dice 5 - randomモジュールを使ってランダムにサイコロを表示しよう！
テーマ：
- python組み込みのrandomモジュールを使ってランダムにサイコロを表示する
- randomモジュールの中のrandintを使って0~5までの数値をランダムに出力する
https://docs.python.org/ja/3/library/random.html#random.randint
- number1変数の中に出力されたランダムな数値を格納する
- number1変数をDICE_LIST1の配列番号に置き換える

手順：
- randomモジュールをインストールする


課題：　
- 赤いサイコロもランダムに表示されるようにする(number2を作成)

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


# ランダムな数値を入れておく変数
number1 = random.randint(0, 5)


# DICE_LIST1の①番目にある画像を表示
dice1 = DICE_LIST1[number1]
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


