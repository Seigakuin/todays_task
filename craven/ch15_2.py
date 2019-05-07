# arcadeのWindow Classを作ろう!
# 今までopen_windowを使ってきたけど、Window Classを使おう

import arcade


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # 背景の色を設定
        arcade.set_background_color(arcade.color.ASH_GREY)

    def on_draw(self):
        """ windowが描かれるたびに呼び出されるメソッド """
        arcade.start_render()

        # 画面に赤い点を描く(左したに)
        arcade.draw_circle_filled(50, 50, 15, arcade.color.AUBURN)


def main():
    # 以前までは
    # arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

    # しかし、Windowクラスを継承したMyGameクラスを使うと
    window = MyGame(640, 480, "Drawing Example")

    arcade.run()


main()
