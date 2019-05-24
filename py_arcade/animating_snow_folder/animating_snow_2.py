""" 
Animating Snow 02
Goal:
- 雪の粒のステータスを入れておくDictionaryを作り、それで呼び出す

Exercises:
- circleではなく、別の形を使ってみよう。
    - `draw_circle_filled()`では`center_x`, `center_y`, `radius`という属性の順番だけど、他の関数ではそうとは限らない！
    - http://arcade.academy/quick_index.html で他の関数を確認

"""
import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ arcade 組み込みのクラス """

    def __init__(self):
        """ コンストラクタ """
        # 親クラスのコンストラクタに画面幅、画面高さ、画面の名前を表示
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "ARCADE EXAMPLE")

        # snowのステータスを作る
        self.snow_status = {
            "center_x": random.randrange(0, SCREEN_WIDTH),
            "center_y": random.randrange(0, SCREEN_HEIGHT),
            "radius": random.randrange(10, 50),
        }

    def on_draw(self):
        """ 描かれるものを定義 """
        arcade.start_render()

        # snow_statusを使って、snowを作る
        arcade.draw_circle_filled(
            self.snow_status["center_x"],
            self.snow_status["center_y"],
            self.snow_status["radius"],
            arcade.color.WHITE,
        )

    def on_update(self, delta_time):
        """ 動きとゲームロジック """
        pass

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
