# Level : 9
# クラスにメンバーを
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
    # NEW!!
    # 引数 question を クラス Question に渡す
    def __init__(self, question):
        self.jp = question["jp"]
        self.en = question["en"]
        self.choices = question["choices"]
        self.answer = question["answer"]
        self.q_num = question["q_num"]


while True:
    # NEW!!
    # クラス Question を初期化、
    # その際、引数 my_questionを入れる
    # question インスタンスを作る
    question_instance = Question(my_question)  # ここでコンストラクタ __init__ が呼ばれる
    print(question_instance.q_num)  # questionインスタンスの属性q_numを使う
    print(question_instance.jp)
    print(question_instance.jp)
    print(question_instance.en)
    print(question_instance.choices)
    response = input()
    if question_instance.answer == int(response):
        print("----- That's right! -----\n")
        break
    else:
        print("----- You're wrong! Try again. -----\n")
