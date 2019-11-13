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

```python
print("世界で最も長い川はどこでしょうか。")
print("(a) 長江 (b) アマゾン川 (c) ナイル川 (d) メコン川")
response = input("アルファベットで答えなさい")

if response == "c":
    print("正解です")
else:
    print("不正解です")

```


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

####

```python
question = {
    "question": "What is the color of the sky?",
    "choices": {"a": "black", "b": "blue", "c": "red", "d": "yellow"},
    "answer": "b",
}

```


```
What is the color of the sky?
(a) black   (b) blue    (c) red    (d) yellow
choose a ~ d
> c

You're wrong...

> b

You're right!

```