# クラスをarcadeで使うとなぜ便利？
# 1. 画面に描く
# 2. 画面の中のitemの位置をupdate
# 3. keyboardからの入力に反応
# 4. mouseからの入力に反応

# arcadeのWindow Classを作ろう!
# 今までopen_windowを使ってきたけど、Window Classを使おう

import arcade


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)


def main():
    # 以前までは
    # arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

    # しかし、Windowクラスを継承したMyGameクラスを使うと
    window = MyGame(640, 480, "Drawing Example")

    arcade.run()


main()
