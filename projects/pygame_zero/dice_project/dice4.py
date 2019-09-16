"""Dice 4 - たくさんの画像をListに入れよう！
テーマ：
- たくさんの画像をListに格納する利点を理解

手順：
1. Global変数を作成する(`DICE_LIST1`)
2. `DICE_LIST1`の中にサイコロのActorをたくさん入れる
3. `DICE_LIST1`の中のものを配列番号で表示するものを指定する

課題：　
1. `DICE_LIST2`を作り、それに赤いサイコロの画像を入れる
2. `DICE_LIST2`の中の画像を表示する
3. 表示するサイコロをListの配列番号を変更して変更しよう

"""
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



# DICE_LIST1の①番目にある画像を表示
dice1 = DICE_LIST1[0]

# Actorインスタンスのcenter位置を設定
dice1.center = (WIDTH // 2, HEIGHT // 2)

def draw():
    screen.fill((80, 148, 75))
    screen.draw.text(
        "DICE!!!",
        (WIDTH // 2, HEIGHT // 2),
        fontsize=60,
        anchor=(0.5, 0.5)

    )
    dice1.draw()


