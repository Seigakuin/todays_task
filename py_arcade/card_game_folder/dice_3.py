"""Dice 3 - 画面に画像を表示しよう！
テーマ：
- 画像を表示するための手順を理解
- 画像が読み取られる場所を確認

画像を表示する手順：
1. `__init__`に画像の変数を入れておく変数を作成 `self.dice`
2. `self.dice`の`center_x`と`center_y`を決め、表示する位置を設定する
3. `on_draw`ファンクションに`self.dice.draw()`を呼ぶ

課題：　
1. diceを画面の真ん中に表示しよう！
2. 画面に複数、好きな画像を表示しよう！


"""
import arcade

# Global コンスタントをここに記述
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Dice!!!"


class MyGame(arcade.Window):
    """メインのクラス"""

    def __init__(self, width, height, title):
        """ここには初期化に必要な情報を書く"""
        super().__init__(width, height, title)

        # 背景の色を設定
        arcade.set_background_color(arcade.color.AMAZON)

        # 画像を自分(self)につける
        self.dice = arcade.Sprite("img/dieWhite1.png")

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
