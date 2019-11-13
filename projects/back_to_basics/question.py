question = {
    "question": "What is the color of the sky?",
    "choices": {"a": "black", "b": "blue", "c": "red", "d": "yellow"},
    "answer": "b",
}


while True:
    print(question["question"])
    for key, value in question["choices"].items():
        print(f"{key} - {value}", end="   ")
    print()
    response = input("answer:  ")

    if question["answer"] == response:
        print("That's right!")
        break
    else:
        print("You're wrong! Try again.")
