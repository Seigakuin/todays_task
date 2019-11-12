question = {
    "question": "What is the color of the sky?",
    "choices": {"a": "black", "b": "blue", "c": "red", "d": "yellow"},
    "answer": "b",
}


while True:
    response = input(question["question"])
    if question["answer"] == response:
        print("That's right!")
        break
    else:
        print("You're wrong! Try again.")
