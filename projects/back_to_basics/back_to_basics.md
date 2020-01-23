# Target1900 クイズアプリを作ろう!

## Level 1:


### 課題：
ユーザーに４択問題を質問をし、
正解ならば「正解です。」
不正解ならば「不正解です。」
と答えるようなプログラムを作成しなさい。

質問は「(1) 現代の科学技術は私たちの生活を大いに[向上させた]。 〔p.18，1〕」
選択肢は ① considered  ② improved  ③ included  ④ concerned
（数字で答えさせる）

#### コードの骨格
```python
print(???)
print(???)
print(???)
response = input(???)

if response == ???:
    print("正解です")
else:
    print("不正解です")
```

#### ヒント：
- 使う ファンクションは `input()`
- ４択はDictionary に埋め込む

<details>

<summary> <b> Level 1 答え表示 </b> </summary>

<p>

```python
print("(1) 現代の科学技術は私たちの生活を大いに[向上させた]。 〔p.18，1〕")
print("Modern technology has greatly (     ) our lives.")
print("① considered  ② improved  ③ included  ④ concerned")
response = input("数字で答えなさい")

if response == "2":
    print("正解です")
else:
    print("不正解です")

```
</p>
</details>

---


## Level 2:

### 課題：

下記のDictionaryを使い、以下のようなユーザーとのやり取りができるようなプログラムを作りなさい。

#### 条件：
- `print()`の中に直接、文字を打ち込むのではなく、`question`Dictionaryを使うこと


#### ヒント：
- Dictionary要素の呼び出しの仕方を確認
`dict1["a"]`

#### コードの骨格
```python
print(??s??ここは問題番号を表示??)
print(??ここは日本語質問文を表示??)
print(??ここは英文を表示??)
print(??ここは選択肢を表示??)
response = ??ユーザーからの入力を得る??
if ??質問の答えと比較?? == ??ユーザーの入力をintに変換する??(response):
    print("----- That's right! -----\n")
else:
    print("----- You're wrong! Try again. -----\n")?

```


#### 使用するデータ(コピペで良い)

```python
question = {
    "jp": "(1) 現代の科学技術は私たちの生活を大いに[向上させた]。 〔p.18，1〕",
    "en": "Modern technology has greatly (     ) our lives.",
    "choices": "① considered  ② improved  ③ included  ④ concerned",
    "answer": 2,
    "q_num": 1,
}

```


#### ユーザーから見たプログラム
```
1
(1) 現代の科学技術は私たちの生活を大いに[向上させた]。 〔p.18，1〕
Modern technology has greatly (     ) our lives.
① considered  ② improved  ③ included  ④ concerned
4 <-- (ユーザーが答えたもの)
----- You're wrong! Try again. -----

```

<details>

<summary> <b> Level 2 答え表示 </b> </summary>

<p>

```python
print(question["q_num"])
print(question["jp"])
print(question["en"])
print(question["choices"])
response = input()
if question["answer"] == int(response):
    print("----- That's right! -----\n")
else:
    print("----- You're wrong! Try again. -----\n")




```

</p>
</details>

---


## Level 3:

### 課題：

下記のDictionaryを使い、以下のようなユーザーとのやり取りができるようなプログラムを作りなさい。

#### 条件：
- 正解するまで答えられるようにすること
- 質問文は直接文字を打ち込むのではなく、与えられたDictionaryから読み取ること


#### ヒント：
正解するまで答えられるようにするには
`while`文を使う(ネットで検索しよう) *`break`もうまく使う

Dictionary要素の呼び出しの仕方を確認
`dict1["a"]`


#### コードの骨格

```python
while True:
    print(??ここは問題番号を表示??)
    print(??ここは日本語質問文を表示??)
    print(??ここは英文を表示??)
    print(??ここは選択肢を表示??)
    response = ??ユーザーからの入力を得る??
    if ??質問の答えと比較?? == ??ユーザーの入力をintに変換する??(response)
        print("----- That's right! -----\n")
        ??正解したら抜け出したい??
    else:
        print("----- You're wrong! Try again. -----\n")

```


#### 使用するデータ(コピペで良い)

```python
question = {
    "jp": "(1) 現代の科学技術は私たちの生活を大いに[向上させた]。 〔p.18，1〕",
    "en": "Modern technology has greatly (     ) our lives.",
    "choices": "① considered  ② improved  ③ included  ④ concerned",
    "answer": 2,
    "q_num": 1,
}

```


#### ユーザーから見たプログラム
```
1
(1) 現代の科学技術は私たちの生活を大いに[向上させた]。 〔p.18，1〕
Modern technology has greatly (     ) our lives.
① considered  ② improved  ③ included  ④ concerned
1 <-- (ユーザーが答えたもの)
----- You're wrong! Try again. -----

1
(1) 現代の科学技術は私たちの生活を大いに[向上させた]。 〔p.18，1〕
Modern technology has greatly (     ) our lives.
① considered  ② improved  ③ included  ④ concerned
2 <-- (ユーザーが答えたもの)
----- That's right! -----

```

<details>

<summary> <b> Level 3 答え表示 </b> </summary>

<p>

```python
while True:
    print(question["q_num"])
    print(question["jp"])
    print(question["en"])
    print(question["choices"])
    response = input()
    if question["answer"] == int(response):
        print("----- That's right! -----\n")
        break
    else:
        print("----- You're wrong! Try again. -----\n")


```

</p>
</details>

---
























## Level 4:

### 課題：
複数の問題を解けるようにしよう

#### 条件：
- questionを一つのでなく、複数を表示できるようにする

#### ヒント：
- `for ?? in ???` を使いリストをループする

#### コードの骨格
```python
for ??ここはforループ構文を入れる??:
    while True:
        print(??ここは問題番号を表示??)
        print(??ここは日本語質問文を表示??)
        print(??ここは英文を表示??)
        print(??ここは選択肢を表示??)
        response = ??ユーザーからの入力を得る??
        if ??質問の答えと比較?? == ??ユーザーの入力をintに変換する??(response)
            print("----- That's right! -----\n")
            ??正解したら抜け出したい??
        else:
            print("----- You're wrong! Try again. -----\n")

```

#### 使用するデータ(コピペで良い)
```python
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



```

#### ユーザーから見たプログラム
```
1
(1) 現代の科学技術は私たちの生活を大いに[向上させた]。 〔p.18，1〕
Modern technology has greatly (     ) our lives.
① considered  ② improved  ③ included  ④ concerned
2
----- That's right! -----

2
(2) 生活の質はエネルギー使用に直接[関連し]てはいない。 〔p.18，2〕
The quality of life is not directly (     ) to energy use.
① produced  ② improved  ③ provided  ④ related
1
----- You're wrong! Try again. -----

2
(2) 生活の質はエネルギー使用に直接[関連し]てはいない。 〔p.18，2〕
The quality of life is not directly (     ) to energy use.
① produced  ② improved  ③ provided  ④ related
4
----- That's right! -----


```


<details>

<summary> <b> Level 4 答え表示 </b> </summary>

<p>

```python
for q in questions:
    while True:
        print(q["q_num"])
        print(q["jp"])
        print(q["en"])
        print(q["choices"])
        response = input()
        if q["answer"] == int(response):
            print("----- That's right! -----\n")
            break
        else:
            print("----- You're wrong! Try again. -----\n")

```

</p>
</details>


## Level 5:

### 課題：
ランダムに問題が出力されるようにしよう

#### 条件：
* 問題が重なっても良い
* 問題の出題回数を決められる

#### ヒント：
- `number_of_times` 変数を作り、出題回数を格納する
- `random_number` 変数を作り、呼び出すquestionの配列番号を格納する
- `for ?? in ???`ではなく、`for ?? in range(??)`を使う
    - 理由: questionオブジェクトそのものでなく、questionの配列番号を使うため
    - forループの中でquestionオブジェクトを呼び出す方法が変わるので注意！！

#### コードの骨格
```python
import random

# 出題する回数
number_of_times = 5

for ?? in range(??):
    while True:
        # 問題の範囲配列番号をランダムに取得
        random_number = random.randint(??)
        print("問題: " + str(??[??]["q_num"]))
        print(??[??]["jp"])
        print(??[??]["en"])
        print(??[??]["choices"])

        response = input("choose 1~4: ")
        if ??[??]["answer"] == int(response):
            print("----- That's right! -----\n")
            break
        else:
            print("----- You're wrong! -----\n")
```

#### 使用するデータ(Level 4 のものを使用)

#### ユーザーから見たプログラム
```
3
(3) 言語はすべて私たちに社会に関する貴重な情報を[与える]ことができる。 〔p.18，3〕
All languages can (     ) us with valuable information about society.
① concern  ② relate  ③ include  ④ provide
choose 1~4: 2
----- You're wrong! Try again. -----

3
(3) 言語はすべて私たちに社会に関する貴重な情報を[与える]ことができる。 〔p.18，3〕
All languages can (     ) us with valuable information about society.
① concern  ② relate  ③ include  ④ provide
choose 1~4: 4
----- That's right! -----

2
(2) 生活の質はエネルギー使用に直接[関連し]てはいない。 〔p.18，2〕
The quality of life is not directly (     ) to energy use.
① produced  ② improved  ③ provided  ④ related
choose 1~4: 
```


<details>

<summary> <b> Level 5 答え表示 </b> </summary>

<p>

```python

number_of_times = 5

for i in range(0, number_of_times):

    while True:
        random_number = random.randint(0, 3)
        print("問題: " + str(questions[random_number]["q_num"]))
        print(questions[random_number]["jp"])
        print(questions[random_number]["en"])
        print(questions[random_number]["choices"])

        response = input("choose 1~4: ")
        if questions[random_number]["answer"] == int(response):
            print("----- That's right! -----\n")
            break
        else:
            print("----- You're wrong! -----\n")

```

</p>
</details>




## Level 6:

### 課題：
ランダムに問題を出題し、問題が重ならないようにする
#### 条件：
- 出題される問題が重ならないようにする
- 間違えた問題は正解するまで出題される
#### ヒント：
- 出題された配列番号を記録しておく`chosen_q_nums`リストを作る
- `chosen_q_nums`にランダムに選ばれた番号があるかを確認する
- もしリストに含まれていなかったら問題を出題する
- `len(??)`を使って問題の数を取得する
- `randint`を使うときにはリストの配列番号に注意
    - リストは「0」から始まり「問題数-1」で終わる
    
#### コードの骨格
```python
import random
# 選ばれたquestion配列番号を記録しておくリスト
chosen_q_nums = []

# 問題の数、出題する
for i in range(0, len(??)):

    while True:
        # リストの配列番号に注意！ゼロから始まる！
        random_number = random.randint(0, ?? - ??)
        # if を使ってすでに出題されたかを確認する
        if ?? not in ??:
            print("問題: " + str(questions[random_number]["q_num"]))
            print(questions[random_number]["jp"])
            print(questions[random_number]["en"])
            print(questions[random_number]["choices"])

            response = input("choose 1~4: ")
            if questions[random_number]["answer"] == int(response):
                # もし出題されていなかった問題番号だとしたら、リストに追加する
                chosen_q_nums.append(??)
                print("----- That's right! -----\n")
                break
            else:
                print("----- You're wrong! Try again. -----\n")

```


#### 使用するデータ(Level 4 のものを使用)

#### ユーザーから見たプログラム
```
問題: 1
(1) 現代の科学技術は私たちの生活を大いに[向上させた]。 〔p.18，1〕
Modern technology has greatly (     ) our lives.
① considered  ② improved  ③ included  ④ concerned
choose 1~4: 2
----- That's right! -----

問題: 4
(4) なぜ政府はその難民たちを違法と[見なす]のか。 〔p.18，4〕
Why does the Government (     ) those refugees illegal?
① consider  ② encourage  ③ improve  ④ provide
choose 1~4: 1
----- That's right! -----

問題: 3
(3) 言語はすべて私たちに社会に関する貴重な情報を[与える]ことができる。 〔p.18，3〕
All languages can (     ) us with valuable information about society.
① concern  ② relate  ③ include  ④ provide
choose 1~4: 4
----- That's right! -----

問題: 2
(2) 生活の質はエネルギー使用に直接[関連し]てはいない。 〔p.18，2〕
The quality of life is not directly (     ) to energy use.
① produced  ② improved  ③ provided  ④ related
choose 1~4: 4
----- That's right! -----
```


<details>

<summary> <b> Level 6 答え表示 </b> </summary>

<p>

```python
import random
# 選ばれたquestion配列番号を記録しておくリスト
chosen_q_nums = []

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
                print("----- You're wrong! Try again. -----\n")

```

</p>
</details>




## Level 7:

### 課題：
questionを表示する機能をファンクションにまとめる
#### 条件：
* 自分のファンクションを定義する `show_question()`
#### ヒント：
* ファンクションの定義は `def hello()`

#### コードの骨格
```python
import random
# 1つのquestionを表示するファンクションを定義
def show_question(question):
    print("問題: " + str(??["q_num"]))
    print(??["jp"])
    print(??["en"])
    print(??["choices"])


# 選ばれたquestion配列番号を記録しておくリスト
chosen_q_nums = []

# 問題の数、出題する
for i in range(0, len(questions)):

    while True:
        random_number = random.randint(0, len(questions) - 1)
        # if を使ってすでに出題されたかを確認する
        if random_number not in chosen_q_nums:

            # 定義したファンクションを使用する
            show_question(??)

            response = input("choose 1~4: ")
            if questions[random_number]["answer"] == int(response):
                # もし出題されていなかった問題番号だとしたら、リストに追加する
                chosen_q_nums.append(random_number)
                print("----- That's right! -----\n")
                break
            else:
                print("----- You're wrong! -----\n")
```


#### 使用するデータ(Level 4 のものを使用)

#### ユーザーから見たプログラム
* Level 6 から変更なし


<details>

<summary> <b> Level 7 答え表示 </b> </summary>

<p>

```python
import random
# 1つのquestionを表示するファンクションを定義
def show_question(question):
    print("問題: " + str(question["q_num"]))
    print(question["jp"])
    print(question["en"])
    print(question["choices"])


# 選ばれたquestion配列番号を記録しておくリスト
chosen_q_nums = []

# 問題の数、出題する
for i in range(0, len(questions)):

    while True:
        random_number = random.randint(0, len(questions) - 1)
        # if を使ってすでに出題されたかを確認する
        if random_number not in chosen_q_nums:

            # 定義したファンクションを使用する
            show_question(questions[random_number])

            response = input("choose 1~4: ")
            if questions[random_number]["answer"] == int(response):
                # もし出題されていなかった問題番号だとしたら、リストに追加する
                chosen_q_nums.append(random_number)
                print("----- That's right! -----\n")
                break
            else:
                print("----- You're wrong! -----\n")
```

</p>
</details>





## Level 8:

### 課題：
クラスの導入、クラスのメンバーの呼び出し方


#### ヒント：

```python
# クラスを作成
class Question:
    # コンストラクタ __init__
    def __init__(self):
        self.??? = 1
        self.??? = "(1) 現代の科学技術は私たちの生活を大いに[向上させた]。 〔p.18，1〕"
        self.??? = "Modern technology has greatly (     ) our lives."
        self.??? = "① considered  ② improved  ③ included  ④ concerned"
        self.??? = 2


while True:
    # NEW!!
    # クラス Question を初期化、question インスタンスを作る
    question = ???()  # ここでコンストラクタ __init__ が呼ばれる
    print(question.???)  # questionインスタンスの属性q_numを使う
    print(question.???)
    print(question.???)
    print(question.???)
    response = input()
    if question.answer == int(response):
        print("----- That's right! -----\n")
        break
    else:
        print("----- You're wrong! Try again. -----\n")
```


#### ユーザーから見たプログラム
```
1
(1) 現代の科学技術は私たちの生活を大いに[向上させた]。 〔p.18，1〕
Modern technology has greatly (     ) our lives.
① considered  ② improved  ③ included  ④ concerned
1
----- You're wrong! Try again. -----
```


<details>

<summary> <b> Level 8 答え表示 </b> </summary>

<p>

```python
# クラスを作成
class Question:
    # コンストラクタ __init__
    def __init__(self):
        self.q_num = 1
        self.jp = "(1) 現代の科学技術は私たちの生活を大いに[向上させた]。 〔p.18，1〕"
        self.en = "Modern technology has greatly (     ) our lives."
        self.choices = "① considered  ② improved  ③ included  ④ concerned"
        self.answer = 2


while True:
    # NEW!!
    # クラス Question を初期化、question インスタンスを作る
    question = Question()  # ここでコンストラクタ __init__ が呼ばれる
    print(question.q_num)  # questionインスタンスの属性q_numを使う
    print(question.jp)
    print(question.en)
    print(question.choices)
    response = input()
    if question.answer == int(response):
        print("----- That's right! -----\n")
        break
    else:
        print("----- You're wrong! Try again. -----\n")
```

</p>
</details>





## Level 9:
### 課題：
クラスにメソッド（動作）をつけよう

#### ヒント：

```python
# クラスを作成
class Question:
    # 引数 question を クラス Question に渡す
    def __init__(self, question):
        self.jp = question["jp"]
        self.en = question["en"]
        self.choices = question["choices"]
        self.answer = question["answer"]
        self.q_num = question["q_num"]

    # NEW!!
    def show_question(self):
        ???
        ???
        ???
        ???


while True:
    # クラス Question を初期化、
    # その際、引数 my_questionを入れる
    # question インスタンスを作る
    question_instance = Question(???)  # ここでコンストラクタ __init__ が呼ばれる

    # NEW!!
    ???.???()  # ここでshow_questionを呼び出す

    response = input()
    if ???.??? == int(response):
        print("----- That's right! -----\n")
        break
    else:
        print("----- You're wrong! Try again. -----\n")
```


#### 使用するデータ(コピペで良い)
```python
my_question = {
    "jp": "(1) 現代の科学技術は私たちの生活を大いに[向上させた]。 〔p.18，1〕",
    "en": "Modern technology has greatly (     ) our lives.",
    "choices": "① considered  ② improved  ③ included  ④ concerned",
    "answer": 2,
    "q_num": 1,
}
```

#### ユーザーから見たプログラム
```
問題: 1
(1) 現代の科学技術は私たちの生活を大いに[向上させた]。 〔p.18，1〕
Modern technology has greatly (     ) our lives.
① considered  ② improved  ③ included  ④ concerned
2
----- That's right! -----
```


<details>

<summary> <b> Level 9 答え表示 </b> </summary>

<p>

```python

my_question = {
    "jp": "(1) 現代の科学技術は私たちの生活を大いに[向上させた]。 〔p.18，1〕",
    "en": "Modern technology has greatly (     ) our lives.",
    "choices": "① considered  ② improved  ③ included  ④ concerned",
    "answer": 2,
    "q_num": 1,
}


# クラスを作成
class Question:
    # 引数 question を クラス Question に渡す
    def __init__(self, question):
        self.jp = question["jp"]
        self.en = question["en"]
        self.choices = question["choices"]
        self.answer = question["answer"]
        self.q_num = question["q_num"]

    # NEW!!
    def show_question(self):
        print("問題: " + str(self.q_num))
        print(self.jp)
        print(self.en)
        print(self.choices)


while True:
    # クラス Question を初期化、
    # その際、引数 my_questionを入れる
    # question インスタンスを作る
    question_instance = Question(my_question)  # ここでコンストラクタ __init__ が呼ばれる

    # NEW!!
    question_instance.show_question()  # ここでshow_questionを呼び出す

    response = input()
    if question_instance.answer == int(response):
        print("----- That's right! -----\n")
        break
    else:
        print("----- You're wrong! Try again. -----\n")
```

</p>
</details>





## Level 10:
### 課題：
Questions クラスを作って、複数の問題を入れよう

#### 条件：

#### ヒント：

```python

# NEW!!
class Questions:
    def __init__(self, questions):
        # まずは複数のQuestionインスタンスを入れる空のリストを作る
        self.questions = []
        # ここでquestionsリストを一つひとつQuestionクラスに変換し、
        # self.questionsリストに足していく
        for ??? in ???:
            # 一つのquestion DictionaryをQuestionインスタンスに変換
            q_instance = Question(???)
            # できたQuestionインスタンスをself.questionsリストに付け足す
            self.questions.append(???)


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


# NEW!!
# my_questions変数の中にあるデータをQuestionsクラスに渡し、
# Questionsクラスのインスタンスを作る
my_questions_instances = Questions(???)

# NEW!!
# my_questions_instancesの中にあるquestionsのリストをfor ループで一つ一つ取り出す
for q in my_questions_instances.???:
    while True:
        # 質問を呼び出す
        ???.???()
        response = input()
        if ???.answer == int(response):
            print("----- That's right! -----\n")
            break
        else:
            print("----- You're wrong! Try again. -----\n")
```


#### 使用するデータ(コピペで良い)
```python

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

```

#### ユーザーから見たプログラム
```
問題: 1
(1) 現代の科学技術は私たちの生活を大いに[向上させた]。 〔p.18，1〕
Modern technology has greatly (     ) our lives.
① considered  ② improved  ③ included  ④ concerned
1
----- You're wrong! Try again. -----

問題: 1
(1) 現代の科学技術は私たちの生活を大いに[向上させた]。 〔p.18，1〕
Modern technology has greatly (     ) our lives.
① considered  ② improved  ③ included  ④ concerned
2
----- That's right! -----

問題: 2
(2) 生活の質はエネルギー使用に直接[関連し]てはいない。 〔p.18，2〕
The quality of life is not directly (     ) to energy use.
① produced  ② improved  ③ provided  ④ related
```


<details>

<summary> <b> Level 10 表示 </b> </summary>

<p>

```python

# NEW!!
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


# NEW!!
# my_questions変数の中にあるデータをQuestionsクラスに渡し、
# Questionsクラスのインスタンスを作る
my_questions_instances = Questions(my_questions)

# NEW!!
# my_questions_instancesの中にあるquestionsのリストをfor ループで一つ一つ取り出す
for q in my_questions_instances.questions:
    while True:
        # 質問を呼び出す
        q.show_question()
        response = input()
        if q.answer == int(response):
            print("----- That's right! -----\n")
            break
        else:
            print("----- You're wrong! Try again. -----\n")

```

</p>
</details>



## Level ??:
### 課題：


#### 条件：

#### ヒント：

```python

```


#### 使用するデータ(コピペで良い)
```python

```

#### ユーザーから見たプログラム
```

```


<details>

<summary> <b> Level ??表示 </b> </summary>

<p>

```python

```

</p>
</details>


## Level ??:
### 課題：


#### 条件：

#### ヒント：

```python

```


#### 使用するデータ(コピペで良い)
```python

```

#### ユーザーから見たプログラム
```

```


<details>

<summary> <b> Level ??表示 </b> </summary>

<p>

```python

```

</p>
</details>