"""Level 4 - 足し算の関数を作ろう！

1. 見本である hello() 関数がどのように書かれているかを確認しよう
2. hello()関数を自分の名前を入れて実行しよう
3. hello()関数を見本にaddfive()関数を書こう
(addfive()関数は数字を受け取るとそれに5を足した数字を表示する)
4. できたaddfive()関数に好きな数字を入れ実行しよう


"""

def hello(name):
    print("Hello", name)

hello("たろう")

def addfive(number):
    print(number + 5)

addfive(12)