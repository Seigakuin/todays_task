""" 19_5 Rotating Ghosts
"""
import random
import math
import arcade

# プレイヤー、ゴーストの大きさの比率
SPRITE_SCALING_PLAYER = 0.2
SPRITE_SCALING_GHOST = 0.02
# ゴーストの出現数
GHOST_COUNT = 80

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Ghost(arcade.Sprite):
    """ Ghost Class
    """

    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

        # NEW 19_5
        # 角度を示すラジアン
        self.circle_angle = 0

        # NEW 19_5
        # 中心からの距離（半径）
        self.circle_radius = 0

        # NEW 19_5
        # 周る速さ（ラジアン）
        self.circle_speed = 0.02

        # NEW 19_5
        # Ghostの初期位置を設定し、動かす
        self.circle_center_x = 0
        self.circle_center_y = 0

    def update(self):
        # Ghostの初期位置を設定し、動かす
        # NEW 19_5
        self.center_x = (
            self.circle_radius * math.sin(self.circle_angle) + self.circle_center_x
        )
        self.center_y = (
            self.circle_radius * math.cos(self.circle_angle) + self.circle_center_y
        )

        # NEW 19_5
        # 角度を足す
        self.circle_angle += self.circle_speed


class MyGame(arcade.Window):
    """ arcade 組み込みのクラス """

    def __init__(self):
        """ コンストラクタ """
        # 親クラスのコンストラクタに画面幅、画面高さ、画面の名前を表示
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # プレイヤーのリスト、ゴーストリストの空を作成
        self.player_list = None
        self.ghost_list = None

        # プレイヤーのスプライトの空を作成
        self.player_sprite = None
        # スコアを0点で初期化
        self.score = 0

        # マウスを画面上で非表示にする
        self.set_mouse_visible(False)

        # バックグラウンド色を緑に
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ ゲームの変数を初期化し、ゲームを設定する """

        # スプライトの空リストを作成
        self.player_list = arcade.SpriteList()
        self.ghost_list = arcade.SpriteList()

        # スコアも０に設定
        self.score = 0

        # プレイヤーを設定
        # プレイヤーの大きさはSPRITE_SCALING_PLAYERで小さく
        self.player_sprite = arcade.Sprite("./player.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        # プレイヤースプライトリストに作ったプレイヤースプライトを追加
        self.player_list.append(self.player_sprite)

        # Ghostの作成
        for _ in range(GHOST_COUNT):
            # ゴーストのイメージを作成
            ghost = Ghost("ghost.png", SPRITE_SCALING_GHOST)

            # ゴーストの位置をランダムに設定
            # NEW 19_5
            ghost.circle_center_x = random.randrange(SCREEN_WIDTH)
            ghost.circle_center_y = random.randrange(SCREEN_HEIGHT)

            # NEW 19_5
            # 開始半径をランダム
            ghost.circle_radius = random.randrange(10, 200)

            # NEW 19_5
            # 開始角度をランダム
            ghost.circle_angle = random.random() * 2 * math.pi

            # ゴーストのスプライトリストにスプライトをたくさん追加
            self.ghost_list.append(ghost)

    def on_draw(self):
        # 描くのを始める
        arcade.start_render()
        # スプライトリスト全体をdraw()ファンクションで描く
        self.ghost_list.draw()
        self.player_list.draw()

        # 　スコアを描く
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ マウスの動きを制御 """
        # プレイヤースプライトの位置をマウスのx, y位置に移動
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ 動きとゲームロジック """
        # 全てのスプライトのupdate()ファンクションを呼び出す
        self.ghost_list.update()

        # プレイヤーと衝突したスプライトのリストを作成する
        # 衝突したものになにかをする時に便利！
        ghost_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.ghost_list
        )

        # 衝突したものリストをforループでさらい、消す(kill())
        # 衝突したら、スコアに足す
        for ghost in ghost_hit_list:
            ghost.kill()
            self.score += 1


def main():
    """ Main method """
    window = MyGame()
    # NEW!! ch18_2
    # MyGameクラスに追加した setup()ファンクションを呼び出し、
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
