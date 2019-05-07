# アニメーションを作ろう!!
# updateメソッドを設定

import arcade


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # 背景の色を設定
        arcade.set_background_color(arcade.color.ASH_GREY)

        # Attribute(属性)を設定
        self.ball_x = 50
        self.ball_y = 50

    def on_draw(self):
        """ windowが描かれるたびに呼び出されるメソッド """
        arcade.start_render()

        # 画面に赤い点を描く(左したに)
        arcade.draw_circle_filled(self.ball_x, self.ball_y, 15,
                                  arcade.color.AUBURN)

    def update(self, delta_time):
        """ 画面上にあるもののデータを更新するために呼び出されるメソッド
        毎秒約60回呼び出される
        """
        self.ball_x += 1
        self.ball_y += 1


def main():
    # 以前までは
    # arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

    # しかし、Windowクラスを継承したMyGameクラスを使うと
    window = MyGame(640, 480, "Drawing Example")

    arcade.run()


main()
