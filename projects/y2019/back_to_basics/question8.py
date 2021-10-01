# Level : 8
# クラスの導入、クラスのメンバーの呼び方
import random


# クラスを作成
class Question:
    # コンストラクタ __init__
    def __init__(self):
        self.q_num = 1
        self.jp = "(1) 現代の科学技術は私たちの生活を大いに[向上させた]。 〔p.18，1〕"
        self.en = "Modern technology has greatly (     ) our lives."
        self.choices = "① considered  ② improved  ③ included  ④ concerned"
        self.answer = 2


while True:
    # NEW!!
    # クラス Question を初期化、question インスタンスを作る
    question = Question()  # ここでコンストラクタ __init__ が呼ばれる
    print(question.q_num)  # questionインスタンスの属性q_numを使う
    print(question.jp)
    print(question.en)
    print(question.choices)
    response = input()
    if question.answer == int(response):
        print("----- That's right! -----\n")
        break
    else:
        print("----- You're wrong! Try again. -----\n")
