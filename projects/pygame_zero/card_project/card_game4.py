# type: ignore
# flake8: noqa

"""Cards 4 - カードを１枚引くアルゴリズムを定義しよう
テーマ：
- カードを１枚引くとデッキから１枚消さなければならない

手順：
- choose_card()関数を定義する
- プレイヤーカードと相手カードを表す CARD1, CARD2 グローバル変数を作成

課題：　
- print()を使って、消されているカードをコンソールに表示使用
    - ex. print(card)

"""
import random

# Global 変数をここに記述
WIDTH = 800
HEIGHT = 600
TITLE = "CARDS!!!"

CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2

CARD1 = Actor("cards/card_back_blue5")
CARD2 = Actor("cards/card_back_red5")


def draw_text(text, pos, fontsize):
    screen.draw.text(text, pos, fontsize=fontsize, anchor=(0.5, 0.5))


# card はActor()インスタンス
def draw_card(card, pos):
    card.center = pos
    card.draw()


def choose_card():
    global CARDS

    suit_key = random.choice(list(CARDS))
    card_key = random.choice(list(CARDS[suit_key]))
    card = CARDS[suit_key][card_key]  # Actor()インスタンス

    # カードを選んだあと、そのカードをCARDSから消す
    CARDS[suit_key].pop(card_key)

    # 選ばれたカードをreturnする
    return card


def draw():
    # 表示するカードのベース部分をcard変数に格納
    CARD1 = choose_card()

    # 2枚目のカード
    CARD2 = choose_card()

    # カードを描く
    draw_card(CARD1["card"], (CENTER_X - 150, CENTER_Y - 50))
    draw_card(CARD2["card"], (CENTER_X + 150, CENTER_Y - 50))

    # カードの点数をカードの横に表示
    draw_text(str(CARD1["score"]), (CENTER_X - 150, CENTER_Y + 100), 80)
    draw_text(str(CARD2["score"]), (CENTER_X + 150, CENTER_Y + 100), 80)


# カード一枚のデータ構造
# クラブのスーツ
#    [ カード名前 ]
#        [ card ]  - Actor()インスタンス
#        [ score ] - 点数 int

card_path = "cards/card_"

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
