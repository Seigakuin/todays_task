# type: ignore
# flake8: noqa

"""Cards 6 - 勝敗を判定するアルゴリズムを組み込む
テーマ：
- 自分と相手のカードを比較し、勝敗を判定する
- SCOREを数える

手順：
- choose_winner()
    - 勝った方のDECKに２枚のカードをappendする
    - 勝ったらSCOREに１を足す
- on_key_down()のDECK.append()を消す
- SCORE1, SCORE2グローバル変数を定義する
- draw()にあるdraw_text()でスコアを表示できるように変更する

課題：　
- 勝敗のスコアによって画面の色が変わるようにしよう

"""

import random

# Global 変数をここに記述
WIDTH = 1000
HEIGHT = 1000
TITLE = "CARDS!!!"

NUM_CARDS = 0

CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2

CARD1 = {"card": Actor("cards/card_back_blue5"), "score": 0}
CARD2 = {"card": Actor("cards/card_back_red5"), "score": 0}

DECK1 = []
DECK2 = []

SCORE1 = 0
SCORE2 = 0


def draw_text(text, pos, fontsize):
    screen.draw.text(text, pos, fontsize=fontsize, anchor=(0.5, 0.5))


# card はActor()インスタンス
def draw_card(card, x, y):
    card.center = (x, y)
    card.draw()


# 手持ちカードを複数表示
def draw_deck(deck, x, y):
    for idx, d in enumerate(deck):
        draw_card(d["card"], x + (30 * idx), y)


def count_cards():
    global NUM_CARDS, CARDS
    NUM_CARDS = 0

    for s in CARDS:
        for c in CARDS[s]:
            NUM_CARDS += 1
    print(NUM_CARDS)


def choose_card():
    global CARDS

    suit_key = random.choice(list(CARDS))
    card_key = random.choice(list(CARDS[suit_key]))
    card = CARDS[suit_key][card_key]  # Actor()インスタンス

    # カードを選んだあと、そのカードをCARDSから消す
    CARDS[suit_key].pop(card_key)
    # NUM_CARDSをアップデートする
    count_cards()

    # もしあるスーツのカードがなくなったらそのスーツを消す
    if len(CARDS[suit_key]) == 0:
        CARDS.pop(suit_key)

    # 選ばれたカードをreturnする
    return card


def choose_deck():
    global CARDS
    deck = []
    for _ in range(5):
        deck.append(choose_card())


def choose_winner(card1, card2):
    global SCORE1, SCORE2
    if card1["score"] > card2["score"]:
        DECK1.append(card1)
        DECK1.append(card2)
        SCORE1 += 1
    elif card1["score"] < card2["score"]:
        DECK2.append(card1)
        DECK2.append(card2)
        SCORE2 += 1


def on_key_down(key):
    global CARD1, CARD2

    # スペースキーが押されたのを確認する
    if key == keys.SPACE:
        # 現在デッキにあるカードを数える
        count_cards()
        # 表示するカードのベース部分をcard変数に格納
        # デッキからカードがなくなったら初期カードを表示
        if NUM_CARDS > 0:
            CARD1 = choose_card()
        else:
            CARD1 = {"card": Actor("cards/card_back_blue5"), "score": 0}
        # 2枚目のカード
        if NUM_CARDS > 0:
            CARD2 = choose_card()
        else:
            CARD2 = {"card": Actor("cards/card_back_red5"), "score": 0}

        choose_winner(CARD1, CARD2)


def draw():
    screen.fill((80, 148, 75))

    # カードを描く
    draw_deck(DECK1, CENTER_X - 400, CENTER_Y + 250)
    draw_deck(DECK2, CENTER_X - 400, CENTER_Y - 300)
    draw_card(CARD1["card"], CENTER_X - 150, CENTER_Y - 50)
    draw_card(CARD2["card"], CENTER_X + 150, CENTER_Y - 50)

    # プレイヤーの点数表示
    draw_text(str(SCORE1), (CENTER_X - 150, CENTER_Y + 100), 80)
    draw_text(str(SCORE2), (CENTER_X + 150, CENTER_Y + 100), 80)


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

