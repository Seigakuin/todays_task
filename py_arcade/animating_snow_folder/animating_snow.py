# type: ignore

""" Animating Snow """
import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ arcade 組み込みのクラス """

    def __init__(self) -> None:
        """ コンストラクタ """
        # 親クラスのコンストラクタに画面幅、画面高さ、画面の名前を表示
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Snow Animation")

        self.snow_list = []

        for _ in range(50):
            x = random.randrange(0, SCREEN_WIDTH)
            y = random.randrange(0, SCREEN_HEIGHT)
            speed = random.randrange(1, 3)
            size = random.randrange(3, 10)
            self.snow_list.append([x, y, speed, size])

    def on_draw(self):
        """ 描かれるものを定義 """
        arcade.start_render()
        arcade.draw_text(
            f"snowflakes: {len(self.snow_list)}",
            20,
            SCREEN_HEIGHT - 20,
            arcade.color.WHITE_SMOKE,
            font_size=16,
        )
        ell = arcade.create_ellipse(300, 300, 40, 40, arcade.color.GOLD)

        for snow in self.snow_list:
            arcade.draw_circle_filled(snow[0], snow[1], snow[3], arcade.color.WHITE)

    def on_update(self, delta_time):
        """ 動きとゲームロジック """
        for snow in self.snow_list:
            snow[1] -= snow[2]

            if snow[1] < 0:
                snow[0] = random.randrange(0, SCREEN_WIDTH)
                snow[1] = SCREEN_HEIGHT

    def on_key_press(self, key, modifiers):
        """ キーが押されたら """
        if key == arcade.key.DOWN:
            for _ in range(5):
                x = random.randrange(0, SCREEN_WIDTH)
                y = SCREEN_HEIGHT
                speed = random.randrange(1, 3)
                size = random.randrange(3, 10)
                self.snow_list.append([x, y, speed, size])

    def on_key_release(self, key, modifiers):
        """ キーが離されたら """
        pass


def main():
    """ main method """
    window = MyGame()
    arcade.run()


if __name__ == "__main__":
    main()
