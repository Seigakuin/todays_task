import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Snow(arcade.Sprite):
    def __init__(self, center_x, center_y, radius, speed):
        super().__init__()

        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.speed = speed

        self.texture = arcade.make_soft_circle_texture(
            self.radius,
            (
                random.randrange(256),
                random.randrange(256),
                random.randrange(256),
            ),
        )

    def update(self):
        self.center_y -= self.speed

        if self.center_y < -50:
            self.center_y = SCREEN_HEIGHT + 50
            self.center_x = random.randrange(SCREEN_WIDTH)


class MyGame(arcade.Window):
    """ arcade 組み込みのクラス """

    def __init__(self):
        """ コンストラクタ """
        # 親クラスのコンストラクタに画面幅、画面高さ、画面の名前を表示
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "ARCADE EXAMPLE")

        # snow一粒一粒を入れておくlistを作成
        self.snow_list = arcade.SpriteList()

        # 仮のsnowのステータスを作る
        # 一回限りだからselfが取れているのに注意!!!
        # for ループでたくさん作る
        for i in range(200):
            # 各Snowインスタンスのステータスを作る
            x = random.randrange(0, SCREEN_WIDTH)
            y = random.randrange(0, SCREEN_HEIGHT)
            radius = random.randrange(10, 50)
            speed = random.randrange(1, 5)

            # Snowクラスを上記で作ったステータスでインスタンス化する
            snow = Snow(x, y, radius, speed)
            # 上で作った仮のSnowインスタンスをsnow_listに付け加える
            self.snow_list.append(snow)

    def on_draw(self):
        """ 描かれるものを定義 """
        arcade.start_render()

        self.snow_list.draw()

    def on_update(self, delta_time):
        """ 動きとゲームロジック """

        self.snow_list.update()

    def on_key_press(self, key, modifiers):
        """ キーが押されたら """
        pass

    def on_key_release(self, key, modifiers):
        """ キーが離されたら """
        pass


def main():
    """ main method """
    window = MyGame()
    arcade.run()


if __name__ == "__main__":
    main()
