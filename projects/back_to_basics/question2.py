question1 = {
    "question": "What is the color of the sky?",
    "choices": {"a": "black", "b": "blue", "c": "red", "d": "yellow"},
    "answer": "b",
}

question2 = {
    "question": "How old is our school?",
    "choices": {"a": "110", "b": "98", "c": "113", "d": "109"},
    "answer": "c",
}

questions = [question1, question2]


for q in questions:
    while True:
        response = input(q["question"])
        if q["answer"] == response:
            print("That's right!")
            break
        else:
            print("You're wrong! Try again.")
