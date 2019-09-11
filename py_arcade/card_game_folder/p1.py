import arcade
import random

# Global コンスタントをここに記述
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Dice!!!"

# サイコロの画像のリストを作成
# 2つ同じリストを用意するのは、２つ同時に同じリストから表示できないため
DICE_LIST1 = [
    arcade.Sprite("img/dieWhite1.png"),
    arcade.Sprite("img/dieWhite2.png"),
    arcade.Sprite("img/dieWhite3.png"),
    arcade.Sprite("img/dieWhite4.png"),
    arcade.Sprite("img/dieWhite5.png"),
    arcade.Sprite("img/dieWhite6.png"),
]

DICE_LIST2 = [
    arcade.Sprite("img/dieRed1.png"),
    arcade.Sprite("img/dieRed2.png"),
    arcade.Sprite("img/dieRed3.png"),
    arcade.Sprite("img/dieRed4.png"),
    arcade.Sprite("img/dieRed5.png"),
    arcade.Sprite("img/dieRed6.png"),
]


class MyGame(arcade.Window):
    """メインのクラス"""

    def __init__(self, width, height, title):
        """ここには初期化に必要な情報を書く"""
        super().__init__(width, height, title)

        # 背景の色を設定
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ここには初期化(リセット時)に必要な情報を書く"""
        # 勝ち数の変数
        self.wins = 0
        # 合計点の変数
        self.total = 0
        # 回数
        self.chances = 10

        # 勝負のメッセージ
        self.message = ""

        # 一つめのサイコロの画像が入っているSpriteList
        self.dice_list1 = arcade.SpriteList()
        # ２つめのサイコロの画像が入っているSpriteList
        self.dice_list2 = arcade.SpriteList()

        # SpriteListにサイコロSpriteを入れる
        for d in DICE_LIST1:
            self.dice_list1.append(d)
        for d in DICE_LIST2:
            self.dice_list2.append(d)

        # 画面に表示するサイコロ1
        self.chosen_dice1 = self.dice_list1[0]
        # 画面に表示するサイコロ2
        self.chosen_dice2 = self.dice_list2[5]

    def on_draw(self):
        """画面に1フレームごとに描く"""
        # なにかを描き始める前のメッセージ
        arcade.start_render()

        # タイトルを描画
        arcade.draw_text(
            "DICE!",
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT - 50,
            arcade.color.WHITE_SMOKE,
            52,
            anchor_x="center",
            anchor_y="center",
        )

        # SCORE: を描画
        arcade.draw_text(
            f"WINS:",
            SCREEN_WIDTH / 2 - 80,
            SCREEN_HEIGHT - 130,
            arcade.color.WHITE_SMOKE,
            36,
            anchor_x="center",
            anchor_y="center",
        )

        # スコアの数字を描画
        arcade.draw_text(
            f"{self.wins:4d}",
            SCREEN_WIDTH / 2 + 100,
            SCREEN_HEIGHT - 130,
            arcade.color.WHITE_SMOKE,
            36,
            anchor_x="center",
            anchor_y="center",
        )

        # 勝負のメッセージを描画
        arcade.draw_text(
            f" {self.message} ",
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT - 180,
            arcade.color.WHITE_SMOKE,
            36,
            anchor_x="center",
            anchor_y="center",
        )

        # chose_dice1の描画位置を設定
        self.chosen_dice1.center_x = SCREEN_WIDTH / 2 - 100
        self.chosen_dice1.center_y = SCREEN_HEIGHT / 2

        # chose_dice2の描画位置を設定
        self.chosen_dice2.center_x = SCREEN_WIDTH / 2 + 100
        self.chosen_dice2.center_y = SCREEN_HEIGHT / 2

        # chosen_dice1, chosen_dice2を描画
        self.chosen_dice1.draw()
        self.chosen_dice2.draw()

        # CHANCES: を描画
        arcade.draw_text(
            f"CHANCES:",
            SCREEN_WIDTH / 2 - 100,
            100,
            arcade.color.WHITE_SMOKE,
            36,
            anchor_x="center",
            anchor_y="center",
        )

        # 回数の数字を描画
        arcade.draw_text(
            f"{self.chances:4d}",
            SCREEN_WIDTH / 2 + 100,
            100,
            arcade.color.WHITE_SMOKE,
            36,
            anchor_x="center",
            anchor_y="center",
        )

    def update(self, delta_time):
        """ゲームロジックをここに描画"""
        pass

    def on_key_press(self, key, key_modifiers):
        """キーが押されてたと時に呼ばれるメソッド
        http://arcade.academy/arcade.key.html
        """
        if self.chances > 0:
            # 上キーが押されたら
            if key == arcade.key.UP:
                # ランダムな数字を 0 ~ 5の範囲で取得
                random_number1 = random.randint(0, 5)
                random_number2 = random.randint(0, 5)

                # サイコロを振った結果を比較する
                if random_number1 > random_number2:
                    # もしサイコロ1が勝ったら winsに1を足す
                    self.wins = self.wins + 1
                    # messageを変更する
                    self.message = "YOU WIN!!"
                elif random_number1 == random_number2:
                    # もし同じだったら数を減らす
                    self.chances = self.chances - 1
                    self.message = "DRAW!!"
                else:
                    # もし負けたら回数を減らす
                    self.chances = self.chances - 1
                    self.message = "YOU LOSE!!"

                # chosen_dice1, chosen_dice2にランダムに選ばれた数字にある
                # サイコロを入れる
                self.chosen_dice1 = self.dice_list1[random_number1]
                self.chosen_dice2 = self.dice_list2[random_number2]

                # もし回数が0になったらゲーム終了
        else:
            self.message = "GAME OVER..."

    def on_key_release(self, key, key_modifiers):
        """キーを離した時に呼ばれるメソッド"""
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """マウスが動いた時に呼ばれるメソッド"""
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """マウスがクリックされた時に呼ばれるメソッド"""
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """マウスが離された時に呼ばれるメソッド"""
        pass


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
