import json


# これは青写真
class Questions:
    def __init__(self, questions):
        # まずは複数のQuestionインスタンスを入れる空のリストを作る
        self.questions = []
        # ここでquestionsリストを一つひとつQuestionクラスに変換し、
        # self.questionsリストに足していく
        for q in questions:
            print(f"q: {type(q)}")
            # 一つのquestion DictionaryをQuestionインスタンスに変換
            q_instance = Question(q)
            # できたQuestionインスタンスをself.questionsリストに付け足す
            self.questions.append(q_instance)

    def start_quiz(self):
        for q in self.questions:
            while True:
                # 質問を呼び出す
                q.show_question()
                response = input()
                if q.answer == int(response):
                    print("----- That's right! -----\n")
                    break
                else:
                    print("----- You're wrong! Try again. -----\n")


# これも青写真
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


# ここから実行が始まる

# 1. 同じフォルダにあるtarget.jsonを開く
with open("./target.json", "r") as f:
    # 2. questions 変数に読み込んだデータを格納
    questions = json.load(f)
    # このデータの中身を見たければ以下のコードをコメントアウトして見てみる
    # print(questions)

# questions変数の中にあるデータをQuestionsクラスに渡し、
# Questionsクラスのインスタンスを作る
questions_instance = Questions(questions)

questions_instance.start_quiz()
