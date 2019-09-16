"""Dice 2 - 画面にテキストを表示しよう！

テーマ：
- テキストを表示するためのファンクション`screen.draw.text()`を理解しよう
- 位置の決め方を理解
- `anchor`を理解

課題：　
- 自分の好きな場所、好きな色でテキストを表示しよう！

ドキュメント: https://pygame-zero.readthedocs.io/en/stable/ptext.html
"""
# Global 変数をここに記述
WIDTH = 800
HEIGHT = 600
TITLE = "Dice!!!"

def draw():
    screen.fill((80, 148, 75))
    screen.draw.text(
        "DICE!!!",
        (WIDTH // 2, HEIGHT // 2),
        fontsize=60,
        anchor=(0.5, 0.5)

    )


