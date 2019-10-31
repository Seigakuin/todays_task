# type: ignore
# flake8: noqa

"""Cards 9 - カードが動くアニメーションをつける
テーマ：
-

手順：
-

課題：　
-

"""
from functools import partial
import random

# Global 変数をここに記述
WIDTH = 1000
HEIGHT = 1000
TITLE = "CARDS!!!"

NUM_CARDS = 0

CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2

CARD1_BACK = {"card": Actor("cards/card_back_blue5"), "score": 0}
CARD2_BACK = {"card": Actor("cards/card_back_red5"), "score": 0}


CARD1 = CARD1_BACK
CARD2 = CARD2_BACK


DECK1 = []
DECK2 = []

SCORE1 = 0
SCORE2 = 0

GAME_STATE = 0
FLIP_STATE = False


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
    global SCORE1, SCORE2, CARD1, CARD2
    print("in choose winner")

    c1 = create_copy(card1)
    c2 = create_copy(card2)

    def func1(c1):
        global DECK1, CARD1
        DECK1.append(c1)

        func_draw_back_cards()

    def func2(c2):
        global DECK2, CARD2
        DECK2.append(c2)

        func_draw_back_cards()

    def func_draw_back_cards():
        global CARD1, CARD2
        CARD1 = CARD1_BACK
        CARD2 = CARD2_BACK
        CARD1["card"].center = (CENTER_X - 150, CENTER_Y - 50)
        CARD1["card"].draw()
        CARD2["card"].center = (CENTER_X + 150, CENTER_Y - 50)
        CARD2["card"].draw()

    if card1["score"] > card2["score"]:
        animate(
            CARD1["card"],
            pos=(CENTER_X - 400, CENTER_Y + 250),
            tween="accelerate",
            on_finished=lambda: func1(c1=c1),
        )
        animate(
            CARD2["card"],
            pos=(CENTER_X - 400, CENTER_Y + 250),
            tween="accelerate",
            on_finished=lambda: func1(c1=c2),
        )
        SCORE1 += 1

    elif card1["score"] < card2["score"]:
        animate(
            CARD1["card"],
            pos=(CENTER_X - 400, CENTER_Y - 300),
            tween="accelerate",
            on_finished=lambda: func2(c2=c1),
        )
        animate(
            CARD2["card"],
            pos=(CENTER_X - 400, CENTER_Y - 300),
            tween="accelerate",
            on_finished=lambda: func2(c2=c2),
        )
        SCORE2 += 1


def create_copy(card):
    c = {"card": Actor(card["card"].image), "score": card["score"]}
    return c


def on_key_down(key):
    global CARD1, CARD2, GAME_STATE, FLIP_STATE

    if GAME_STATE == 0:
        GAME_STATE = 1

    elif GAME_STATE == 1:
        # スペースキーが押されたのを確認する
        if key == keys.SPACE:
            # 現在デッキにあるカードを数える
            count_cards()
            print("flip ", FLIP_STATE)

            if FLIP_STATE is False:
                # 表示するカードのベース部分をcard変数に格納
                # デッキからカードがなくなったら初期カードを表示
                if NUM_CARDS > 0:
                    CARD1 = choose_card()
                    CARD1["card"].center = (CENTER_X - 150, CENTER_Y - 50)
                else:
                    CARD1 = CARD1_BACK
                # 2枚目のカード
                if NUM_CARDS > 0:
                    CARD2 = choose_card()
                    CARD2["card"].center = (CENTER_X + 150, CENTER_Y - 50)
                else:
                    CARD2 = CARD2_BACK
                FLIP_STATE = True
            else:
                choose_winner(CARD1, CARD2)
                FLIP_STATE = False
            if NUM_CARDS == 0:
                GAME_STATE = 2

    elif GAME_STATE == 2:
        GAME_STATE = 0


def draw_start_screen():
    text1 = "WAR"
    text2 = "Let's play the game of war!"
    text3 = "Press any button to play!"
    draw_text(text1, (CENTER_X, CENTER_Y - 110), 300)
    draw_text(text2, (CENTER_X, CENTER_Y + 20), 80)
    draw_text(text3, (CENTER_X, CENTER_Y + 90), 60)


def draw_end_screen():
    if SCORE1 > SCORE2:
        text1 = "You WIN!!"
    elif SCORE1 < SCORE2:
        text1 = "You LOSE..."
    else:
        text1 = "It was a tie!"
    text2 = "Thank you for playing!"
    text3 = "Press any button to play!"

    draw_text(text1, (CENTER_X, CENTER_Y - 50), 100)
    draw_text(text2, (CENTER_X, CENTER_Y + 20), 80)
    draw_text(text3, (CENTER_X, CENTER_Y + 80), 70)


def fn():
    print("hello")


def start():
    global CARDS, CARD1, CARD2, SCORE1, SCORE2, DECK1, DECK2

    CARDS = read_cards()
    CARD1 = {"card": Actor("cards/card_back_blue5"), "score": 0}
    CARD2 = {"card": Actor("cards/card_back_red5"), "score": 0}
    SCORE1 = 0
    SCORE2 = 0
    DECK1 = []
    DECK2 = []
    CARD1["card"].center = CENTER_X - 150, CENTER_Y - 50
    CARD2["card"].center = CENTER_X + 150, CENTER_Y - 50


def draw():
    global CARD1, CARD2
    screen.fill((80, 148, 75))

    if GAME_STATE == 0:
        start()
        draw_start_screen()

    elif GAME_STATE == 1:

        # カードを描く
        CARD1["card"].draw()
        CARD2["card"].draw()
        draw_deck(DECK1, CENTER_X - 400, CENTER_Y + 250)
        draw_deck(DECK2, CENTER_X - 400, CENTER_Y - 300)

        # プレイヤーの点数表示
        draw_text(str(SCORE1), (CENTER_X - 150, CENTER_Y + 100), 80)
        draw_text(str(SCORE2), (CENTER_X + 150, CENTER_Y + 100), 80)

    elif GAME_STATE == 2:
        draw_end_screen()


card_path = "cards/card_"


def read_cards():
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
    return CARDS


def read_cards2():
    CARDS = {
        "clubs": {
            "a": {
                "card": Actor(card_path + "clubs_a"),
                "score": 1,
                "path": card_path + "clubs_a",
            },
            2: {
                "card": Actor(card_path + "clubs2"),
                "score": 2,
                "path": card_path + "clubs2",
            },
            3: {
                "card": Actor(card_path + "clubs3"),
                "score": 3,
                "path": card_path + "clubs3",
            },
            4: {
                "card": Actor(card_path + "clubs4"),
                "score": 4,
                "path": card_path + "clubs4",
            },
            5: {
                "card": Actor(card_path + "clubs5"),
                "score": 5,
                "path": card_path + "clubs5",
            },
            6: {
                "card": Actor(card_path + "clubs6"),
                "score": 6,
                "path": card_path + "clubs6",
            },
            7: {
                "card": Actor(card_path + "clubs7"),
                "score": 7,
                "path": card_path + "clubs7",
            },
            8: {
                "card": Actor(card_path + "clubs8"),
                "score": 8,
                "path": card_path + "clubs8",
            },
            9: {
                "card": Actor(card_path + "clubs9"),
                "score": 9,
                "path": card_path + "clubs9",
            },
            10: {
                "card": Actor(card_path + "clubs10"),
                "score": 10,
                "path": card_path + "clubs10",
            },
            "j": {
                "card": Actor(card_path + "clubs_j"),
                "score": 11,
                "path": card_path + "clubs_j",
            },
            "q": {
                "card": Actor(card_path + "clubs_q"),
                "score": 12,
                "path": card_path + "clubs_q",
            },
            "k": {
                "card": Actor(card_path + "clubs_k"),
                "score": 13,
                "path": card_path + "clubs_k",
            },
        },
        "diamonds": {
            "a": {
                "card": Actor(card_path + "diamonds_a"),
                "score": 1,
                "path": card_path + "diamonds_a",
            },
            2: {
                "card": Actor(card_path + "diamonds2"),
                "score": 2,
                "path": card_path + "diamonds2",
            },
            3: {
                "card": Actor(card_path + "diamonds3"),
                "score": 3,
                "path": card_path + "diamonds3",
            },
            4: {
                "card": Actor(card_path + "diamonds4"),
                "score": 4,
                "path": card_path + "diamonds4",
            },
            5: {
                "card": Actor(card_path + "diamonds5"),
                "score": 5,
                "path": card_path + "diamonds5",
            },
            6: {
                "card": Actor(card_path + "diamonds6"),
                "score": 6,
                "path": card_path + "diamonds6",
            },
            7: {
                "card": Actor(card_path + "diamonds7"),
                "score": 7,
                "path": card_path + "diamonds7",
            },
            8: {
                "card": Actor(card_path + "diamonds8"),
                "score": 8,
                "path": card_path + "diamonds8",
            },
            9: {
                "card": Actor(card_path + "diamonds9"),
                "score": 9,
                "path": card_path + "diamonds9",
            },
            10: {
                "card": Actor(card_path + "diamonds10"),
                "score": 10,
                "path": card_path + "diamonds10",
            },
            "j": {
                "card": Actor(card_path + "diamonds_j"),
                "score": 11,
                "path": card_path + "diamonds_j",
            },
            "q": {
                "card": Actor(card_path + "diamonds_q"),
                "score": 12,
                "path": card_path + "diamonds_q",
            },
            "k": {
                "card": Actor(card_path + "diamonds_k"),
                "score": 13,
                "path": card_path + "diamonds_k",
            },
        },
        "hearts": {
            "a": {
                "card": Actor(card_path + "hearts_a"),
                "score": 1,
                "path": card_path + "hearts_a",
            },
            2: {
                "card": Actor(card_path + "hearts2"),
                "score": 2,
                "path": card_path + "hearts2",
            },
            3: {
                "card": Actor(card_path + "hearts3"),
                "score": 3,
                "path": card_path + "hearts3",
            },
            4: {
                "card": Actor(card_path + "hearts4"),
                "score": 4,
                "path": card_path + "hearts4",
            },
            5: {
                "card": Actor(card_path + "hearts5"),
                "score": 5,
                "path": card_path + "hearts5",
            },
            6: {
                "card": Actor(card_path + "hearts6"),
                "score": 6,
                "path": card_path + "hearts6",
            },
            7: {
                "card": Actor(card_path + "hearts7"),
                "score": 7,
                "path": card_path + "hearts7",
            },
            8: {
                "card": Actor(card_path + "hearts8"),
                "score": 8,
                "path": card_path + "hearts8",
            },
            9: {
                "card": Actor(card_path + "hearts9"),
                "score": 9,
                "path": card_path + "hearts9",
            },
            10: {
                "card": Actor(card_path + "hearts10"),
                "score": 10,
                "path": card_path + "hearts10",
            },
            "j": {
                "card": Actor(card_path + "hearts_j"),
                "score": 11,
                "path": card_path + "hearts_j",
            },
            "q": {
                "card": Actor(card_path + "hearts_q"),
                "score": 12,
                "path": card_path + "hearts_q",
            },
            "k": {
                "card": Actor(card_path + "hearts_k"),
                "score": 13,
                "path": card_path + "hearts_k",
            },
        },
        "spades": {
            "a": {
                "card": Actor(card_path + "spades_a"),
                "score": 1,
                "path": card_path + "spades_a",
            },
            2: {
                "card": Actor(card_path + "spades2"),
                "score": 2,
                "path": card_path + "spades2",
            },
            3: {
                "card": Actor(card_path + "spades3"),
                "score": 3,
                "path": card_path + "spades3",
            },
            4: {
                "card": Actor(card_path + "spades4"),
                "score": 4,
                "path": card_path + "spades4",
            },
            5: {
                "card": Actor(card_path + "spades5"),
                "score": 5,
                "path": card_path + "spades5",
            },
            6: {
                "card": Actor(card_path + "spades6"),
                "score": 6,
                "path": card_path + "spades6",
            },
            7: {
                "card": Actor(card_path + "spades7"),
                "score": 7,
                "path": card_path + "spades7",
            },
            8: {
                "card": Actor(card_path + "spades8"),
                "score": 8,
                "path": card_path + "spades8",
            },
            9: {
                "card": Actor(card_path + "spades9"),
                "score": 9,
                "path": card_path + "spades9",
            },
            10: {
                "card": Actor(card_path + "spades10"),
                "score": 10,
                "path": card_path + "spades10",
            },
            "j": {
                "card": Actor(card_path + "spades_j"),
                "score": 11,
                "path": card_path + "spades_j",
            },
            "q": {
                "card": Actor(card_path + "spades_q"),
                "score": 12,
                "path": card_path + "spades_q",
            },
            "k": {
                "card": Actor(card_path + "spades_k"),
                "score": 13,
                "path": card_path + "spades_k",
            },
        },
        "joker": {
            "joker": {
                "card": Actor(card_path + "joker"),
                "score": 1,
                "path": card_path + "joker",
            }
        },
    }
    return CARDS
