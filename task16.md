# 課題  Level 16
## テーマ： Dictionary を使ったデータ保存

<br></br>
### 1
#### 課題： 映画のデータを保存しよう
<br></br>
### pseudo code (疑似コード)
1. "1 - 新規映画保存 / 2 - 映画一覧 / 3 - 検索 / 4 - 終了"とユーザーに聞く
2. ユーザーがメニューから選択する


<br></br>
### [ movies データの見本 ]
```python:
movie = {
    'name': ... (str),
    'director': ... (str),
    'year': ... (int)
}
```


<br></br>
### [ 実装しなけらば行けない function ]
```python:

def menu():

def add_movie():

def show_movie():

def find_movie():


```

<br></br>
以下のスケルトンからはじめましょう。（????の部分を埋めましょう)
```python:
movies = [{
    'name': 'Harry Potter',
    'director': 'Michael Wage',
    'year': 1997
}]

def menu():
    user_input = input("1 - 新規映画保存 / 2 - 映画一覧 / 3 - 検索 / 4 - 終了\n")

    while user_input != '4':
        if user_input == '1':
            add_movie()
        elif user_input == '2':
            show_movies(movies)
        elif user_input == '3':
            find_movie()
        else:
            print("Stopping program...")
            
        user_input = input("1 - 新規映画保存 / 2 - 映画一覧 / 3 - 検索 / 4 - 終了\n")

def add_movie():
    ???

def show_movies():
    ???

def find_movie():
    ???


```

<br></br>
実行例
```
1 - 新規映画保存 / 2 - 映画一覧 / 3 - 検索 / 4 - 終了
--> 2

---------------------------
映画名: Harry Potter
監督名: Michael Wage
リリース年: 1997
```