# type: ignore
# flake8: noqa

"""Cards 5 - キーを押したらカードを選ぶ
テーマ：
- スペースキーを押してカードを引く機能をつける

手順：
- カードの総数を管理するNUM_CARDSグローバル変数を作成
- NUM_CARDSを数えるcount_cards()関数を定義する
- on_key_down()関数（組み込み関数）を定義する
    - choose_card()をon_key_down()に移動する
- choose_card()関数にifで条件をつける
    - もし、あるスーツのカードがなくなったらそのスーツを消す
- draw()にifで条件をつける
    - もし、カードを全て引ききったらカードをえらべないようにする
- draw()の中にscreen.fill()を入れる（画面を複数回描画すると、画像が重なってしまう）

課題：　
- print()を使ってコンソールに残りのカードの枚数を表示しよう

"""
import random

# Global 変数をここに記述
WIDTH = 800
HEIGHT = 600
TITLE = "CARDS!!!"

NUM_CARDS = 0

CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2

CARD1 = {"card": Actor("cards/card_back_blue5"), "score": 0}
CARD2 = {"card": Actor("cards/card_back_red5"), "score": 0}


def draw_text(text, pos, fontsize):
    screen.draw.text(text, pos, fontsize=fontsize, anchor=(0.5, 0.5))


# card はActor()インスタンス
def draw_card(card, pos):
    card.center = pos
    card.draw()


def count_cards():
    global NUM_CARDS, CARDS
    NUM_CARDS = 0

    for s in CARDS:
        for c in CARDS[s]:
            NUM_CARDS += 1


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


def draw():
    screen.fill((80, 148, 75))

    # カードを描く

    for idx, c in enumerate([CARD1, CARD2]):
        draw_card(c["card"], (CENTER_X - 150 + (35 * idx), CENTER_Y - 150))

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

