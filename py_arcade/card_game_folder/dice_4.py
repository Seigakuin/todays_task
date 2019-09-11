"""Dice 4 - たくさんの画像をListに入れよう！
テーマ：
- たくさんの画像をListに格納する利点を理解

手順：
1. Global変数を作成する(`DICE_LIST`)
2. `DICE_LIST`の中にサイコロのSpriteをたくさん入れる
3. `DICE_LIST`の中のものを配列番号で表示するものを指定する

課題：　
1. `DICE_LIST2`を作り、それに赤いサイコロの画像を入れる
2. `DICE_LIST2`の中の画像を表示する


"""
import arcade

# Global コンスタントをここに記述
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Dice!!!"


# サイコロの画像のリストを作成
DICE_LIST1 = [
    arcade.Sprite("img/dieWhite1.png"),
    arcade.Sprite("img/dieWhite2.png"),
    arcade.Sprite("img/dieWhite3.png"),
    arcade.Sprite("img/dieWhite4.png"),
    arcade.Sprite("img/dieWhite5.png"),
    arcade.Sprite("img/dieWhite6.png"),
]


class MyGame(arcade.Window):
    """メインのクラス"""

    def __init__(self, width, height, title):
        """ここには初期化に必要な情報を書く"""
        super().__init__(width, height, title)

        # 背景の色を設定
        arcade.set_background_color(arcade.color.AMAZON)

        # DICE_LIST1の中にある0番目の画像をself.diceに格納する
        self.dice = DICE_LIST1[0]

        # 画像を表示する位置を設定する
        self.dice.center_x = 100
        self.dice.center_y = 100

    def setup(self):
        """ここには初期化(リセット時)に必要な情報を書く"""

    def on_draw(self):
        """画面に1フレームごとに描く"""
        # なにかを描き始める前のメッセージ
        arcade.start_render()

        # タイトルを描画
        arcade.draw_text(
            "DICE!",  # 表示するテキスト
            SCREEN_WIDTH / 2,  # x 位置
            SCREEN_HEIGHT - 50,  # y 位置
            arcade.color.WHITE_SMOKE,  # 色
            52,  # フォントの大きさ
            anchor_x="center",  # どこを基準に場所を設定するのか
            anchor_y="center",  # どこを基準に場所を設定するのか
        )

        # Spriteを表示する
        self.dice.draw()


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
