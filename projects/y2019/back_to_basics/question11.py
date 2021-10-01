# Level : 11
# Questions クラスにstart_quizメソッドを作る
import random

my_questions = [
    {
        "jp": "(1) 現代の科学技術は私たちの生活を大いに[向上させた]。 〔p.18，1〕",
        "en": "Modern technology has greatly (     ) our lives.",
        "choices": "① considered  ② improved  ③ included  ④ concerned",
        "answer": 2,
        "q_num": 1,
    },
    {
        "jp": "(2) 生活の質はエネルギー使用に直接[関連し]てはいない。 〔p.18，2〕",
        "en": "The quality of life is not directly (     ) to energy use.",
        "choices": "① produced  ② improved  ③ provided  ④ related",
        "answer": 4,
        "q_num": 2,
    },
    {
        "jp": "(3) 言語はすべて私たちに社会に関する貴重な情報を[与える]ことができる。 〔p.18，3〕",
        "en": "All languages can (     ) us with valuable information about society.",
        "choices": "① concern  ② relate  ③ include  ④ provide",
        "answer": 4,
        "q_num": 3,
    },
    {
        "jp": "(4) なぜ政府はその難民たちを違法と[見なす]のか。 〔p.18，4〕",
        "en": "Why does the Government (     ) those refugees illegal?",
        "choices": "① consider  ② encourage  ③ improve  ④ provide",
        "answer": 1,
        "q_num": 4,
    },
]


class Questions:
    def __init__(self, questions):
        # まずは複数のQuestionインスタンスを入れる空のリストを作る
        self.questions = []
        # ここでquestionsリストを一つひとつQuestionクラスに変換し、
        # self.questionsリストに足していく
        for q in questions:
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


# my_questions変数の中にあるデータをQuestionsクラスに渡し、
# Questionsクラスのインスタンスを作る
questions_instance = Questions(my_questions)

questions_instance.start_quiz()
