# Level : 9
# クラスにメソッド（動作）をつけよう
import random

my_question = {
    "jp": "(1) 現代の科学技術は私たちの生活を大いに[向上させた]。 〔p.18，1〕",
    "en": "Modern technology has greatly (     ) our lives.",
    "choices": "① considered  ② improved  ③ included  ④ concerned",
    "answer": 2,
    "q_num": 1,
}


# クラスを作成
class Question:
    # 引数 question を クラス Question に渡す
    def __init__(self, question):
        self.jp = question["jp"]
        self.en = question["en"]
        self.choices = question["choices"]
        self.answer = question["answer"]
        self.q_num = question["q_num"]

    # NEW!!
    def show_question(self):
        print("問題: " + str(self.q_num))
        print(self.jp)
        print(self.en)
        print(self.choices)


while True:
    # クラス Question を初期化、
    # その際、引数 my_questionを入れる
    # question インスタンスを作る
    question_instance = Question(my_question)  # ここでコンストラクタ __init__ が呼ばれる

    # NEW!!
    question_instance.show_question()  # ここでshow_questionを呼び出す

    response = input()
    if question_instance.answer == int(response):
        print("----- That's right! -----\n")
        break
    else:
        print("----- You're wrong! Try again. -----\n")
