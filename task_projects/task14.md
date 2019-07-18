# Task14

## テーマ：　 Tuple の基本 / enumerate()の使い方

Tuple は List にそっくりです。
大きな違いは Tuple の中身は immutable であるということ。
immutable ということは、その中身は一度宣言すると変えられないということです。
immutable であるということはプログラムを作る上で様々なバグを防いでくれます。

- 以下にあるリストから「出力」のようにデータを表示しなさい。偶数の位置にある要素だけを出力しなさい。

注意

- `enumerate()`を使用すること

```python
mylist = ['a', 'b', 'c']

for key, value in enumerate(mylist):
    print(key, value)

```

出力

```python
0 a
1 b
2 c
```

- 0, 1, 2 各要素の順番 key を取得できる！

#### スタートコード (これはコピペしても良い) \* **???** の箇所を自分のコードに置き換えること

```python
mytuple = (0, 1, 5, 9, 13)

for key, value in enumerate(mytuple):
    if ???:
        print(???)

```

#### 出力

```python
0
5
13
```

[back home](https://github.com/Seigakuin/todays_task)
