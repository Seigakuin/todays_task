# Task06

## テーマ：　 input() / int() / str()練習

### 足し算のプログラムの作成

1. `input()`を使ってユーザーに「１つ目の数字：」と尋ね、その入力を変数`num1`に格納
2. `input()`の入力は全て`string`型になっているので`int()`で数字に変換する（`string`（文字列）を数字として足せない）
3. `input()`を使ってユーザーに「１つ目の数字：」と尋ね、その入力を変数`num2`に格納
4. `num2`を数字に変換
5. `print()`で足し算の結果を出力

注意

- 最後の`print()`で文字 string と結果 int はそのままでは繋げられない　 int を文字列に変換しなければならない！ `str()`を使用すること！

```python
num1 = ???
num1 = ???


num2 = ???
num2 = ???

print("結果：" + ???)

```

出力

```python
1つ目の数字： 12
2つ目の数字：23
結果：35
```

### [このスタートファイルをコピー](https://github.com/Seigakuin/todays_task/blob/master/projects/task_templates/task06.py)