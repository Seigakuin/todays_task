# type: ignore

""" Animating Snow 
- created Snow2
- Snow2 inherits Sprite Class but doesn't use a png or jpg
- it uses a Buffered Draw Command
- it sets it to the self.texture (from Sprite Class)
- 19/05/21
    - added framecout in MyGame
    - framecount % ?? == 0 can be used to update only on certain 
"""
import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Snow2(arcade.Sprite):
    def __init__(self, center_x, center_y):
        self.size = random.randrange(1, 30)
        super().__init__()
        self.center_x = center_x
        self.center_y = center_y
        self.speed = random.uniform(1, 5)

        self.texture = arcade.make_soft_square_texture(
            self.size, arcade.color.GHOST_WHITE
        )

    def update(self):
        self.center_y -= self.speed
        self.turn_right(5)

        if self.center_y < 0:
            self.center_x = random.randrange(0, SCREEN_WIDTH)
            self.center_y = SCREEN_HEIGHT


class MyGame(arcade.Window):
    """ arcade 組み込みのクラス """

    def __init__(self) -> None:
        """ コンストラクタ """
        # 親クラスのコンストラクタに画面幅、画面高さ、画面の名前を表示
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Snow Animation")

        self.snow_list = arcade.SpriteList()
        self.ADD_SNOW = False
        self.framecount = 0

        for _ in range(100):
            x = random.randrange(0, SCREEN_WIDTH)
            y = random.randrange(0, SCREEN_HEIGHT)
            snow2 = Snow2(x, y)
            self.snow_list.append(snow2)

    def add_snow(self, run):
        if run:
            for _ in range(100):
                x = random.randrange(0, SCREEN_WIDTH)
                y = SCREEN_HEIGHT
                snow = Snow2(x, y)
                self.snow_list.append(snow)

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
        self.snow_list.draw()

    def on_update(self, delta_time):
        """ 動きとゲームロジック """
        self.framecount += 1
        if self.framecount % 10 == 0:
            self.add_snow(self.ADD_SNOW)
        self.snow_list.update()

    def on_key_press(self, key, modifiers):
        """ キーが押されたら """
        if key == arcade.key.DOWN:
            self.ADD_SNOW = True

    def on_key_release(self, key, modifiers):
        """ キーが離されたら """
        if key == arcade.key.DOWN:
            self.ADD_SNOW = False


def main():
    """ main method """
    window = MyGame()
    arcade.run()


if __name__ == "__main__":
    main()
