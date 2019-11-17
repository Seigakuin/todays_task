questions = [
    {
        "question": "What is the color of the sky?",
        "choices": {"a": "black", "b": "blue", "c": "red", "d": "yellow"},
        "answer": "b",
    },
    {
        "question": "How old is our school?",
        "choices": {"a": "110", "b": "98", "c": "113", "d": "109"},
        "answer": "c",
    },
    {
        "question": "How old is Earth?",
        "choices": {
            "a": "4.5 billion years old",
            "b": "35 thousand years old",
            "c": "100 million years old",
            "d": "2.1 trillion years",
        },
        "answer": "a",
    },
]


for q in questions:
    while True:
        print(q["question"])

        for key, item in q["choices"].items():
            print("* " + key + " - " + item)

        response = input("choose a~d: ")
        if q["answer"] == response:
            print("That's right!")
            break
        else:
            print("You're wrong! Try again.")

