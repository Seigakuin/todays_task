# Ballクラスを定義しよう
import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class Ball:
    def __init__(self, radius, color, pos_x, pos_y):
        """ コンストラクタ """
        self.radius = radius
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y

    def draw(self):
        """ 画面上に与えられた引数でボールを描く"""
        arcade.draw_circle_filled(
            self.pos_x, self.pos_y, self.radius, self.color
        )


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # 背景の色を設定
        arcade.set_background_color(arcade.color.ASH_GREY)

        # Ballクラスのインスタンスを作成
        self.ball = Ball(15, arcade.color.AUBURN, 50, 50)

    def on_draw(self):
        """ windowが描かれるたびに呼び出されるメソッド """
        arcade.start_render()
        self.ball.draw()


def main():
    # Windowクラスを継承したMyGameクラスを使うと
    window = MyGame(640, 480, "Drawing Example")

    arcade.run()


main()
