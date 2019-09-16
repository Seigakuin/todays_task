# 課題 Level 13

## テーマ： Dictionary

<br></br>

### 1

#### 課題： Dictionary に要素を足しましょう。

<br></br>

```python:
mydict = {}

????

print(mydict)
```

**出力**

```python:
{'Tom': 30}
```

<br></br>
<br></br>

### 2

#### 課題：　 Dictionary を使って、生徒の好きな数字を貯められるプログラムを作りましょう。

<br></br>

### pseudo code (疑似コード)

1. `What is your name?`とユーザーに聞く
2. ユーザーが名前を入力する
3. `What is your favorite number?`とユーザーに聞く
4. ユーザーが数字を入力する
5. 1-4 の手順を繰り返したいかどうか `Do you want to contine? (y/n)` とユーザーに聞く
6. ユーザーは`y`か`n`と入力する
7. `n`の場合のみ、`print()`を使ってデータすべてを出力する

\
\
以下のスケルトンからはじめましょう。（????の部分を埋めましょう)

```python:
favorite_nums = {}

?????
?????
?????
?????

print(favorite_nums)
```

\
\
プログラムは以下のよう出力になるはずです。

```python:
What is your name? Tom
What is your favorite number? 12
Do you want to continue? (y/n) y
What is your name? John
What is your favorite number? 34
Do you want to continue? (y/n) y
What is your name? Greg
What is your favorite number? 98
Do you want to continue? (y/n) n
{'Tom': '12', 'John': '34', 'Greg': '98'}
```

<br></br>
<br></br>
<br></br>

#### ヒント

1. `range()` `len()` をうまく使うこと
2. `while` ループを使うこと

[back home](https://github.com/Seigakuin/todays_task)

### [このスタートファイルをコピー](https://github.com/Seigakuin/todays_task/blob/master/task_templates/task13.py)
