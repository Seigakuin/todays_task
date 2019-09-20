"""Pygame Zero Level 4 - 画像を表示しよう！

1. alien変数にActor()を作ろう
2. alien.pos でalienの場所(pos)を(x, y)で設定しよう
3. draw()ファンクションの中にalien変数のdraw()ファンクションを呼び出そう
4. 上にある"プレイ"ボタンを押して実行しよう

5. 色々ば場所にalienを移動させよう

"""
WIDTH = 800
HEIGHT = 600
TITLE = "HELLO"

alien = Actor("alien")
alien.pos = (300, 200)


def draw():
    screen.fill((255, 255, 255))
    alien.draw()
