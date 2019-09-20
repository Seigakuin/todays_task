"""Pygame Zero Level 3 - 図形を描こう！

1. draw()関数の中にscreen.draw.circle()を使って円を描こう
2. screen.draw.circle()の中には３つの引数が入るよ
    -(場所, 半径, 色)  ex. ((30, 30), 40, (255, 255, 100))
3. 場所は (x, y) で配置されるよ x は横位置、 y は縦の位置
    - (0, 0)は画面の左上　(800, 600)は画面の右下
4. 色々な場所に円を描こう

"""
WIDTH = 800
HEIGHT = 600
TITLE = "HELLO"


def draw():
    screen.fill((255, 255, 255))
    screen.draw.filled_circle((400, 300), 20, (0, 0, 200))