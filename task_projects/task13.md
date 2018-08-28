# 課題
## Level 13
### テーマ： Tuples

TupleはListとそっくりです。
大きな違いはTupleの中身は immutable であるということ。
immutable ということは、その中身は一度宣言すると変えられないということです。
immutableであるということはプログラムを作る上で様々なバグを防いでくれます。

* 以下にあるリストから「出力」のようにデータを表示しなさい。偶数の位置にある要素だけを出力しなさい。
```python:
mytuple = (0, 1, 5, 9, 13)
```
出力
```python:
0
5
13
```
注意！！
tupleではlistと違って以下ができない
```python:
mytuple[0] = 12
```

ヒント
1. `range()` `len()` をうまく使うこと


<a href="https://repl.it/@unicoshun/task13" target="_blank">ANSWER</a>

[back home](https://github.com/Seigakuin/todays_task)