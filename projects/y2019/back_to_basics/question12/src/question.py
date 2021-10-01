# クラスを作成
class Question:
    # 引数 question を クラス Question に渡す
    def __init__(self, question):
        self.jp = question["jp"]
        self.en = question["en"]
        self.choices = question["choices"]
        self.answer = question["answer"]
        self.q_num = question["q_num"]

    def show_question(self):
        print("問題: " + str(self.q_num))
        print(self.jp)
        print(self.en)
        print(self.choices)
