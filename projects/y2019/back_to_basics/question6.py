# Level : 6 ランダムに問題を出題し、問題が重ならないようにする
import random

questions = [
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

# 選ばれたquestion配列番号を記録しておくリスト
chosen_q_nums = []


# 問題の数、出題する
for i in range(0, len(questions)):
    while True:
        random_number = random.randint(0, len(questions) - 1)
        # if を使ってすでに出題されたかを確認する
        if random_number not in chosen_q_nums:
            print("問題: " + str(questions[random_number]["q_num"]))
            print(questions[random_number]["jp"])
            print(questions[random_number]["en"])
            print(questions[random_number]["choices"])

            response = input("choose 1~4: ")
            if questions[random_number]["answer"] == int(response):
                # もし出題されていなかった問題番号だとしたら、リストに追加する
                chosen_q_nums.append(random_number)
                print("----- That's right! -----\n")
                break
            else:
                print("----- You're wrong! -----\n")

