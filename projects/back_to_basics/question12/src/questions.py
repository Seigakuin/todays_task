from src.question import Question


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
