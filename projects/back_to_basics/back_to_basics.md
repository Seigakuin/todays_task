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
- print()の中に直接、文字を打ち込むのではなく、`question`Dictionaryを使うこと


#### ヒント：
Dictionary要素の呼び出しの仕方を確認
`dict1["a"]`

#### コードの骨格
```python
print(??ここは問題番号を表示??)
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
- `for ?? in ???` を使いリストをループする

#### ヒント：
- `for`ループの文法を検索すること

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

<summary> <b> Level 4 答え表示 </b> </summary>

<p>

```python

```

</p>
</details>



