""" Arcade Starter Code ver.01"""
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ arcade 組み込みのクラス """

    def __init__(self):
        """ コンストラクタ """
        # 親クラスのコンストラクタに画面幅、画面高さ、画面の名前を表示
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "ARCADE EXAMPLE")

    def on_draw(self):
        """ 描かれるものを定義 """
        arcade.start_render()

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
