""" 
Animating Snow 10 

- Goal:
    - キーに合わせてBoxを動かす

- Exercises:
    - 衝突判定を工夫する
        - ex. 衝突した雪のスピードを下げる

"""
import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Box(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.make_soft_square_texture(100, arcade.color.GOLD, 255, 200)

    def update(self):
        # フレームのたびに右に1ピクセル, 上にピクセル移動
        # つまり、右斜め上に移動
        self.center_x += self.change_x
        self.center_y += self.change_y

        # 端っこ対策
        if self.center_y < 0:
            self.center_y = SCREEN_HEIGHT
        if self.center_y > SCREEN_HEIGHT:
            self.center_y = 0
        if self.center_x < 0:
            self.center_x = SCREEN_WIDTH
        if self.center_x > SCREEN_WIDTH:
            self.center_x = 0

    def move_up(self):
        self.change_y += 5

    def move_down(self):
        self.change_y -= 5

    def move_right(self):
        self.change_x += 5

    def move_left(self):
        self.change_x -= 5


# ここでarcade.Spriteを継承する
class Snow(arcade.Sprite):
    def __init__(self, center_x, center_y, radius, speed):
        # 継承したクラスを初期化呼び出す
        super().__init__()

        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.speed = speed

        # 継承したSpriteクラスにはtextureというステータスがある
        # このtextureにcircle入れる
        self.texture = arcade.make_soft_circle_texture(self.radius, arcade.color.WHITE)

    # 継承したSpriteクラスにはupdateという動き(Method)がある
    # ここに下に動くアニメーションを設定する
    def update(self):
        self.center_y -= self.speed

        # 画面下に移動してしまった場合
        # 画面上に移動させる
        if self.center_y < 0:
            self.center_y = SCREEN_HEIGHT


class MyGame(arcade.Window):

    """ arcade 組み込みのクラス """

    def __init__(self):
        """ コンストラクタ """
        # 親クラスのコンストラクタに画面幅、画面高さ、画面の名前を表示
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "ARCADE EXAMPLE")

        # Box, Snow インスタンスすべてのSpriteを入れておくためのSpriteList
        self.all_list = arcade.SpriteList()

        # Box インスタンスを作成
        self.box = Box()
        # all_listにBoxインスタンスを追加
        self.all_list.append(self.box)

        # snow一粒一粒を入れておくSpritelistを作成
        self.snow_list = arcade.SpriteList()

        # 仮のsnowのステータスを作る
        # 一回限りだからselfが取れているのに注意!!!
        # for ループでたくさん作る
        for i in range(500):
            # 各Snowインスタンスのステータスを作る
            x = random.randrange(0, SCREEN_WIDTH)
            y = random.randrange(0, SCREEN_HEIGHT)
            radius = random.randrange(10, 50)
            speed = random.randrange(1, 5)

            # Snowクラスを上記で作ったステータスでインスタンス化する
            snow = Snow(x, y, radius, speed)
            # 上で作った仮のSnowインスタンスをsnow_listに付け加える
            self.snow_list.append(snow)
            # all_listにもSnowインスタンスを入れる
            self.all_list.append(snow)

    def on_draw(self):
        """ 描かれるものを定義 """
        arcade.start_render()

        # snow_listでなく、all_listのdraw()を呼び出し、Boxも含めてdrawする
        self.all_list.draw()

    def on_update(self, delta_time):
        """ 動きとゲームロジック """

        # snow_listでなく、all_listのupdate()を呼び出し、Boxも含めてdrawする
        self.all_list.update()
        # BoxインスタンスとSnowインスタンスのリストと衝突したSnowをhit_listに加える
        hit_list = arcade.check_for_collision_with_list(self.box, self.snow_list)
        # hit_listにあるSnowインスタンス(衝突したもの)を取り除く
        for snow in hit_list:
            snow.remove_from_sprite_lists()

    def on_key_press(self, key, modifiers):
        """ キーが押されたら """
        # キーが押されたらSnowのインスタンスを追加
        self.add_snow()

        if key == arcade.key.UP:
            self.box.move_up()
        if key == arcade.key.DOWN:
            self.box.move_down()
        if key == arcade.key.RIGHT:
            self.box.move_right()
        if key == arcade.key.LEFT:
            self.box.move_left()

    def on_key_release(self, key, modifiers):
        """ キーが離されたら """
        pass

    def add_snow(self):
        """ Snowクラスのインスタンスを作成し、描画する"""
        # 描く位置(x)を設定
        x = random.randrange(0, SCREEN_WIDTH)

        # 縦位置(y)は画面の一番上に描く
        y = SCREEN_HEIGHT
        # 雪の大きさをランダムで設定
        radius = random.randrange(1, 20)
        # 雪の降るスピードをランダムで設定
        speed = random.randrange(1, 5)

        # インスタンスを作成し、SpriteListに追加
        snow = Snow(x, y, radius, speed)
        self.snow_list.append(snow)


def main():
    """ main method """
    window = MyGame()
    arcade.run()


if __name__ == "__main__":
    main()
