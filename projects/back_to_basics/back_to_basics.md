# ４択クイズを作ろう

## Level 1:

### 課題：
ユーザーに４択問題を質問をし、
正解ならば「正解です。」
不正解ならば「不正解です。」
と答えるようなプログラムを作成しなさい。

質問は「世界で最も長い川はどこでしょうか。」
選択肢は (a) 長江 (b) アマゾン川 (c) ナイル川 (d) メコン川
（アルファベットで答えさせる）

#### ヒント：
- 使う ファンクションは `input()`
- ４択はDictionary に埋め込む

<details>

<summary> <b> Level 1 答え表示 </b> </summary>

<p>

```python
print("世界で最も長い川はどこでしょうか。")
print("(a) 長江 (b) アマゾン川 (c) ナイル川 (d) メコン川")
response = input("アルファベットで答えなさい")

if response == "c":
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
- 正解するまで答えられるようにすること
- 質問文は直接文字を打ち込むのではなく、与えられたDictionaryから読み取ること


#### ヒント：
正解するまで答えられるようにするには
`while`文を使う(ネットで検索しよう)

Dictionary要素の呼び出しの仕方を確認
`dict1["a"]`


#### 使用するデータ(コピペで良い)

```python
question = {
    "question": "What is the color of the sky?",
    "choices": {"a": "black", "b": "blue", "c": "red", "d": "yellow"},
    "answer": "b",
}

```


#### ユーザーから見たプログラム
```
What is the color of the sky?
(a) black   (b) blue    (c) red    (d) yellow
choose a ~ d
> c

You're wrong...

> b

You're right!

```

<details>

<summary> <b> Level 2 答え表示 </b> </summary>

<p>

```python
while True:
    print(q["question"])
    response = input("choose a~d")
    if q["answer"] == response:
        print("That's right!")
        break
    else:
        print("You're wrong! Try again.")


```

</p>
</details>

---




## Level 3:

### 課題：
４択の選択肢をキレイに表示しよう。

#### 条件：
Level 2 の答えのコードに４択をキレイに表示するコードを追加すること

#### ヒント：

```python
# ??? をうめなさい
for key, item in ???:
    print(???)

```

* dictionary の KeyとValueを取得するには...
* string(文字列)をつなげるには...
```python
d = {"key1": "value1", "key2": "value2", "key3": "value3"}

# dictionsryに.items()をつけることによって、
# dictionaryのkeyとvalueを同時に取得できる
for key, value in d.items():
    # stringは "+" でつなげることができる
    print(key + " - " + value)

```


#### 使用するデータ(コピペで良い)
```python
question = {
    "question": "What is the color of the sky?",
    "choices": {"a": "black", "b": "blue", "c": "red", "d": "yellow"},
    "answer": "b",
}


```

#### ユーザーから見たプログラム
```
What is the color of the sky?
* a - black
* b - blue
* c - red
* d - yellow
choose a~d:

> b

You're right!!

```


<details>

<summary> <b> Level 3 答え表示 </b> </summary>

<p>

```python
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
```

</p>
</details>