# Level 2
question = {
    "jp": "(1) 現代の科学技術は私たちの生活を大いに[向上させた]。 〔p.18，1〕",
    "en": "Modern technology has greatly (     ) our lives.",
    "choices": "① considered  ② improved  ③ included  ④ concerned",
    "answer": 2,
    "q_num": 1,
}


print(question["q_num"])
print(question["jp"])
print(question["en"])
print(question["choices"])
response = input()
if question["answer"] == int(response):
    print("----- That's right! -----\n")
else:
    print("----- You're wrong! Try again. -----\n")

