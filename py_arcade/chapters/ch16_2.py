# ユーザーインプットを受け取る
# 上下左右キーで動かす
import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 3


class Ball:
    def __init__(self, pos_x, pos_y, change_x, change_y, radius, color):
        """ コンストラクタ """
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ 画面上に与えられた引数でボールを描く"""
        arcade.draw_circle_filled(
            self.pos_x, self.pos_y, self.radius, self.color
        )

    def update(self):
        """ ボールのデータの更新に使うメソッド """

        # ボールを動かす
        self.pos_x += self.change_x
        self.pos_y += self.change_y

        # 壁にあたっているかの衝突判定
        if self.pos_x < self.radius:
            self.change_x *= -1  # つまり逆方向に移動するということ

        if self.pos_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1

        if self.pos_y < self.radius:
            self.change_y *= -1

        if self.pos_y > SCREEN_HEIGHT - self.radius:
            self.change_y *= -1


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # 背景の色を設定
        arcade.set_background_color(arcade.color.ASH_GREY)

        # マウスを見えないようにする
        self.set_mouse_visible(False)

        # 3つのボールを足す
        self.ball = Ball(50, 50, 3, 3, 15, arcade.color.AUBURN)

    def on_draw(self):
        """ windowが描かれるたびに呼び出されるメソッド """
        arcade.start_render()

        # ボールを描く
        self.ball.draw()

    def update(self, delta_time):
        """ 画面上にあるもののデータを更新するために呼び出されるメソッド
        毎秒約60回呼び出される
        """
        # ボールをアップデート
        self.ball.update()

    def on_mouse_motion(self, x, y, dx, dy):
        self.ball.pos_x = x
        self.ball.pos_y = y

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED


def main():
    # Windowクラスを継承したMyGameクラスを使うと
    window = MyGame(640, 480, "Drawing Example")

    arcade.run()


main()
