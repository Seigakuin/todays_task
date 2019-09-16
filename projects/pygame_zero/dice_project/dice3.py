"""Dice 3 - 画面に画像を表示しよう！
テーマ：
- 画像を表示するための手順を理解
- 画像が読み取られる場所を確認

画像を表示する手順：
1. Global変数に`dice1`を作成する
2. dice1にActor()クラスのインスタンスを作成し、格納する
3. Actor()の引数1にimagesフォルダにあるパスを通す
4. Actor()の引数2に画像の中心を画面のどこに配置するかを設定する
5. draw()ファンクションの中にdice1.draw()を呼ぶ

課題：　
1. dice1がテキストと重なっているので、重ならないように配置しよう！
2. dice2を画面に表示しよう！


"""

# Global 変数をここに記述
WIDTH = 800
HEIGHT = 600
TITLE = "Dice!!!"

dice1 = Actor("dice/die_white1", center=(WIDTH // 2, HEIGHT // 2))

def draw():
    screen.fill((80, 148, 75))
    screen.draw.text(
        "DICE!!!",
        (WIDTH // 2, HEIGHT // 2),
        fontsize=60,
        anchor=(0.5, 0.5)

    )
    dice1.draw()


