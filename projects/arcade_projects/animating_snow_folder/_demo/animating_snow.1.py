# type: ignore

""" Animating Snow """
import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Snow(arcade.ShapeElementList):
    def __init__(self, center_x, center_y):
        super().__init__()
        self.center_x = center_x
        self.center_y = center_y
        box_raw = arcade.create_rectangle_filled(
            self.center_x, self.center_y, 10, 10, arcade.color.WHITE
        )
        self.shape_list = []

        self.shape_list.append(box_raw)
        group = (box_raw.mode, box_raw.line_width)
        self.batches[group].items.append(box_raw)
        self.dirties.add(group)

    def update(self):
        self.center_y -= 1
        if self.center_y < 0:
            self.center_y = SCREEN_HEIGHT


class Box:
    def __init__(self, center_x, center_y, size):
        self.center_x = center_x
        self.center_y = center_y
        self.size = size
        raw_shape = arcade.create_ellipse_filled(
            self.center_x, self.center_y, self.size, self.size, arcade.color.WHITE
        )
        self.shape = arcade.ShapeElementList()
        self.shape.append(raw_shape)

    def draw(self):
        # arcade.start_render()
        self.shape.draw()

    def update(self):
        self.shape.move(0, -1)

        if self.shape.center_y < 0:
            self.shape.center_y = SCREEN_HEIGHT


class MyGame(arcade.Window):
    """ arcade 組み込みのクラス """

    def __init__(self) -> None:
        """ コンストラクタ """
        # 親クラスのコンストラクタに画面幅、画面高さ、画面の名前を表示
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Snow Animation")

        # self.snow_list = arcade.ShapeElementList()
        self.box_list = []

        self.box = Box(SCREEN_WIDTH // 2, SCREEN_HEIGHT, 50)

        # for _ in range(1000):
        #     x = random.randrange(0, SCREEN_WIDTH)
        #     y = random.randrange(0, SCREEN_HEIGHT)
        #     box_raw = arcade.create_rectangle_filled(x, y, 10, 10, arcade.color.WHITE)
        #     box = arcade.ShapeElementList()
        #     box.append(box_raw)
        #     self.box_list.append(box)

        for _ in range(100):
            x = random.randrange(0, SCREEN_WIDTH)
            y = random.randrange(0, SCREEN_HEIGHT)
            box = Box(x, y, 10)
            self.box_list.append(box)

        # for _ in range(50):
        #     x = random.randrange(0, SCREEN_WIDTH)
        #     y = random.randrange(0, SCREEN_HEIGHT)
        #     # speed = random.randrange(1, 3)
        #     size = random.randrange(3, 10)
        #     snow = arcade.create_ellipse_filled(x, y, size, size, arcade.color.WHITE)
        #     self.snow_list.append(snow)

    def on_draw(self):
        """ 描かれるものを定義 """
        arcade.start_render()
        arcade.draw_text(
            f"box_list: {len(self.box_list)}",
            20,
            SCREEN_HEIGHT - 20,
            arcade.color.WHITE_SMOKE,
            font_size=16,
        )

        # self.snow_list.draw()
        for b in self.box_list:
            b.draw()

        self.box.draw()

        # for box in self.box_list:
        #     box.draw()

        # for snow in self.snow_list:
        #     arcade.draw_circle_filled(snow[0], snow[1], snow[3], arcade.color.WHITE)

    def on_update(self, delta_time):
        """ 動きとゲームロジック """
        # self.snow_list.center_y -= 1

        for b in self.box_list:
            b.update()

        self.box.update()

        # for snow in self.snow_list:
        #     snow.center_y -= 1

        #     if snow.center_y < 0:
        #         snow.center_y = random.randrange(0, SCREEN_WIDTH)
        #         snow.center_x = SCREEN_HEIGHT

    def on_key_press(self, key, modifiers):
        """ キーが押されたら """

        if key == arcade.key.DOWN:
            self.box.center_y = 400

    #         for _ in range(5):
    #             x = random.randrange(0, SCREEN_WIDTH)
    #             y = random.randrange(0, SCREEN_HEIGHT)

    #             sn = Snow(x, y)
    #             self.box_list.append(sn)

    # speed = random.randrange(1, 3)
    # size = random.randrange(3, 10)
    # self.snow_list.append([x, y, speed, size])

    def on_key_release(self, key, modifiers):
        """ キーが離されたら """
        pass


def main():
    """ main method """
    window = MyGame()
    arcade.run()


if __name__ == "__main__":
    main()
