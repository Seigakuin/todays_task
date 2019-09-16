"""Dice 6 - キーが押されたらサイコロの数字を変えよう！
テーマ：
- pygame zeroのon_key_down()ファンクションを設定する
- global というキーワードの意味を理解する

手順：
- pygame zeroのon_key_down()ファンクションを書く
- global dice1 と記述
- key変数とkeys.UPを比較し、上ボタンが押されたかを判定する
(その他のキー　https://pygame-zero.readthedocs.io/en/stable/hooks.html#buttons-and-keys)


課題：　
- 赤いサイコロも同様の処理をする
    - global にdice2を追加
    - on_key_down()の中のif構文の下にnumber2変数を作り、ランダム数値を格納
    - DICE_LIST2を表示

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
    # globalを設定することによって、コードの上に書いたdice1変数を「読む」だけでなく
    # 内容を「書く」(書き換える)ことができる
    global dice1

    if key == keys.UP:
        # ランダムな数値を入れておく変数
        number1 = random.randint(0, 5)
        dice1 = DICE_LIST1[number1]