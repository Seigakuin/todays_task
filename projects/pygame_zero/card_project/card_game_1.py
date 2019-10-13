"""Cards 1 - カードのデータ構造を理解しよう！
テーマ：
- カードのデータ構造を理解
- Dictionaryを多用 (カード１枚にカードのpathとscoreを格納)

課題：　
- 別のカードを表示する

"""
import random

# Global 変数をここに記述
WIDTH = 800
HEIGHT = 600
TITLE = "CARDS!!!"
SCORE = 0

GAME_STATUS = 0

card_path = "cards/card_"


# カード一枚のデータ構造
# クラブのスーツ
#    [ カード名前 ]
#        [ card ]  - Actor()インスタンス
#        [ score ] - 点数 int

CARDS = {
    "clubs": {
        "a": {"card": Actor(card_path + "clubs_a"), "score": 1},
        2: {"card": Actor(card_path + "clubs2"), "score": 2},
        3: {"card": Actor(card_path + "clubs3"), "score": 3},
        4: {"card": Actor(card_path + "clubs4"), "score": 4},
        5: {"card": Actor(card_path + "clubs5"), "score": 5},
        6: {"card": Actor(card_path + "clubs6"), "score": 6},
        7: {"card": Actor(card_path + "clubs7"), "score": 7},
        8: {"card": Actor(card_path + "clubs8"), "score": 8},
        9: {"card": Actor(card_path + "clubs9"), "score": 9},
        10: {"card": Actor(card_path + "clubs10"), "score": 10},
        "j": {"card": Actor(card_path + "clubs_j"), "score": 11},
        "q": {"card": Actor(card_path + "clubs_q"), "score": 12},
        "k": {"card": Actor(card_path + "clubs_k"), "score": 13},
    },
    "diamonds": {
        "a": {"card": Actor(card_path + "diamonds_a"), "score": 1},
        2: {"card": Actor(card_path + "diamonds2"), "score": 2},
        3: {"card": Actor(card_path + "diamonds3"), "score": 3},
        4: {"card": Actor(card_path + "diamonds4"), "score": 4},
        5: {"card": Actor(card_path + "diamonds5"), "score": 5},
        6: {"card": Actor(card_path + "diamonds6"), "score": 6},
        7: {"card": Actor(card_path + "diamonds7"), "score": 7},
        8: {"card": Actor(card_path + "diamonds8"), "score": 8},
        9: {"card": Actor(card_path + "diamonds9"), "score": 9},
        10: {"card": Actor(card_path + "diamonds10"), "score": 10},
        "j": {"card": Actor(card_path + "diamonds_j"), "score": 11},
        "q": {"card": Actor(card_path + "diamonds_q"), "score": 12},
        "k": {"card": Actor(card_path + "diamonds_k"), "score": 13},
    },
    "hearts": {
        "a": {"card": Actor(card_path + "hearts_a"), "score": 1},
        2: {"card": Actor(card_path + "hearts2"), "score": 2},
        3: {"card": Actor(card_path + "hearts3"), "score": 3},
        4: {"card": Actor(card_path + "hearts4"), "score": 4},
        5: {"card": Actor(card_path + "hearts5"), "score": 5},
        6: {"card": Actor(card_path + "hearts6"), "score": 6},
        7: {"card": Actor(card_path + "hearts7"), "score": 7},
        8: {"card": Actor(card_path + "hearts8"), "score": 8},
        9: {"card": Actor(card_path + "hearts9"), "score": 9},
        10: {"card": Actor(card_path + "hearts10"), "score": 10},
        "j": {"card": Actor(card_path + "hearts_j"), "score": 11},
        "q": {"card": Actor(card_path + "hearts_q"), "score": 12},
        "k": {"card": Actor(card_path + "hearts_k"), "score": 13},
    },
    "spades": {
        "a": {"card": Actor(card_path + "spades_a"), "score": 1},
        2: {"card": Actor(card_path + "spades2"), "score": 2},
        3: {"card": Actor(card_path + "spades3"), "score": 3},
        4: {"card": Actor(card_path + "spades4"), "score": 4},
        5: {"card": Actor(card_path + "spades5"), "score": 5},
        6: {"card": Actor(card_path + "spades6"), "score": 6},
        7: {"card": Actor(card_path + "spades7"), "score": 7},
        8: {"card": Actor(card_path + "spades8"), "score": 8},
        9: {"card": Actor(card_path + "spades9"), "score": 9},
        10: {"card": Actor(card_path + "spades10"), "score": 10},
        "j": {"card": Actor(card_path + "spades_j"), "score": 11},
        "q": {"card": Actor(card_path + "spades_q"), "score": 12},
        "k": {"card": Actor(card_path + "spades_k"), "score": 13},
    },
    "joker": {"joker": {"card": Actor(card_path + "joker"), "score": 1}},
}


def draw():
    # 表示するカードのベース部分をcard変数に格納
    card = CARDS["clubs"]["j"]

    # card["card"] は CARDS["clubs"]["j"]["card"]と同じ
    # つまりcard["card"]の中身は　Actor()インスタンス！
    # だから .draw() を呼び出せる！
    card["card"].center = (300, 300)
    card["card"].draw()

    # カードの点数をカードの横に表示
    screen.draw.text(
        str(card["score"]), (500, 300), fontsize=80, anchor=(0.5, 0.5)
    )
