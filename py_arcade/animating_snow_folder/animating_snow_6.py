""" 
Animating Snow 06
Goal:
- Snow クラスを作成し、Snowクラスのインスタンスでステータスを管理する

Exercises:
- Snowインスタンスの数に変化をつけよう(動きが鈍くなるはず！)
- これを解決するためには根本的になにかを変えないといけない

"""
import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Snow:
    def __init__(self, center_x, center_y, radius, speed):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.speed = speed


class MyGame(arcade.Window):
    """ arcade 組み込みのクラス """

    def __init__(self):
        """ コンストラクタ """
        # 親クラスのコンストラクタに画面幅、画面高さ、画面の名前を表示
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "ARCADE EXAMPLE")

        # snow一粒一粒を入れておくlistを作成
        self.snow_list = []

        # 仮のsnowのステータスを作る
        # 一回限りだからselfが取れているのに注意!!!
        # for ループでたくさん作る
        for i in range(50):
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

        for snow in self.snow_list:
            # snow_listにある一つ一つのsnowを取り出す
            # 注意: snowはSnowクラスのインスタンスなので
            # 　　　各ステータスの呼び方が違う
            arcade.draw_circle_filled(
                snow.center_x, snow.center_y, snow.radius, arcade.color.WHITE
            )

            if snow.center_y < 0:
                snow.center_y = SCREEN_HEIGHT

    def on_update(self, delta_time):
        """ 動きとゲームロジック """

        # Snowインスタンスのステータスにあるspeedを利用して
        # 各インスタンスに速度の変化をつける
        for snow in self.snow_list:
            snow.center_y -= snow.speed

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
