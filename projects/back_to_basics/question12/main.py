from src.questions import Questions


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

if __name__ == "__main__":
    # my_questions変数の中にあるデータをQuestionsクラスに渡し、
    # Questionsクラスのインスタンスを作る
    questions_instance = Questions(my_questions)

    questions_instance.start_quiz()
