"""
課題：　自分の好きな場所、好きな色でテキストを表示しよう！

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


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
