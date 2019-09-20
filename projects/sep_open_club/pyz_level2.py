"""Pygame Zero Level 2 - 画面に色をつけよう！

1. draw()は「画面を描きなさい！」を意味する
2. その中に画面(screen)を赤(128, 0, 0)で埋めなさい(fill)という指示を出す
3. 上にある"プレイ"ボタンを押して実行しよう

4. 自分で色々な色に変えてみよう！

色の表現:
(RED[0~255], GREEN[0~255], BLUE[0~255])


"""
WIDTH = 800
HEIGHT = 600
TITLE = "HELLO"


def draw():
    screen.fill((128, 0, 0))
