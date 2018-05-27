# 課題  Level 17
## テーマ： List のスライシング

<br></br>
### 1
#### 課題： emailアドレスをパーツに分けよう
<br></br>
### pseudo code (疑似コード)
1. ユーザーに"What is your email address?: " と聞く
2. 受けとったアドレスのユーザー名とドメイン名を出力する

例
```python
"""
>>> What is your email address?: 
yourname@example.com
>>> Your user name is 'yourname' and your domain name is 'example.com'
"""
```



<br></br>
### [ ヒント ]
- リストスライスをうまく使う
```python:
word = "Hello my name is Tom"
word[0:5]
--> Hello
word[6:8]
--> my
word[6:]
--> my name is Tom
word[:5]
--> Hello
```
- `index()`を使う

```python:
word = "Hello my name is Tom"
word.index("name")
--> 6
word[word.index("name"):] # word[6:]と同じ！ 
--> my name is Tom
```

<br></br>
以下のスケルトンからはじめましょう。（????の部分を埋めましょう)
```python:

email = ???

user = ???

domain = ???

output = ???

print(output)


```