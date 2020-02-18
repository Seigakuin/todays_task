# すごろくを作ろう!

<br></br>

---






## Level 1:

### 課題：
画面にすごろくの盤面を描こう！
下記の「ユーザーから見たプログラム」と同様の画面を出力しなさい。
(😀の前には9個のハイフン、😀の後には20個のハイフン)

#### コードの骨格
```python
print("SUGOROKU!!")
print("-" ? ???  + "😀" + "-" ? ???)
```

#### ヒント：
- １文字を繰り返すにはどうする？


#### ユーザーから見たプログラム
```
SUGOROKU!!
---------😀--------------------

```


<details>

<summary> <b> Level 1表示 </b> </summary>

<p>

```python
print("SUGOROKU!!")
print("-" * 9 + "😀" + "-" * 20)
```

</p>
</details>

---







## Level 2:

### 課題：

`player_position`という変数を使ってLevel1と同じ出力を作りなさい。

#### ヒント：
`player_position`を使ってハイフンの数を計算すること。

#### コードの骨格
```python
player_position = 10


print("SUGOROKU!!")
print("-" * (???) + "😀" + "-" * (???))

```


#### ユーザーから見たプログラム
```
SUGOROKU!!
---------😀--------------------
```

<details>

<summary> <b> Level 2 答え表示 </b> </summary>

<p>

```python
player_position = 10

print("SUGOROKU!!")
print("-" * (player_position - 1) + "😀" + "-" * (30 - player_position))

```

</p>
</details>

<br></br>

---









## Level 3:

### 課題：

出力を`banmen()`という関数を作り、呼び出しなさい。

#### ヒント：
関数の作り方を再確認しましょう。

#### コードの骨格
```python
player_position = 10


??? ???:
    print("SUGOROKU!!")
    print("-" * (player_position - 1) + "😀" + "-" * (30 - player_position))


???

```


#### ユーザーから見たプログラム
```
SUGOROKU!!
---------😀--------------------
```

<details>

<summary> <b> Level 3 答え表示 </b> </summary>

<p>

```python
player_position = 10


def banmen():
    print("SUGOROKU!!")
    print("-" * (player_position - 1) + "😀" + "-" * (30 - player_position))


banmen()

```

</p>
</details>

<br></br>

---








## Level 4:

### 課題：

`player`と`computer`を出力しよう。


#### コードの骨格
```python
player_position = 10
computer_position = 15


def banmen():
    print("SUGOROKU!!")
    print("-" * (player_position - 1) + "😀" + "-" * (30 - player_position))
    print(???)


banmen()

```


#### ユーザーから見たプログラム
```
SUGOROKU!!
---------😀--------------------
--------------😈---------------
```

<details>

<summary> <b> Level 4 答え表示 </b> </summary>

<p>

```python
player_position = 10
computer_position = 15


def banmen():
    print("SUGOROKU!!")
    print("-" * (player_position - 1) + "😀" + "-" * (30 - player_position))
    print("-" * (computer_position - 1) + "😈" + "-" * (30 - computer_position))


banmen()

```

</p>
</details>

<br></br>

---









## Level 5:

### 課題：

`while`ループを使って`player`と`computer`を動かそう


#### ヒント：
`input`を使うとループが止まる
（これがないと永遠にループに入ってしまう！）


#### コードの骨格
```python
player_position = 1
computer_position = 1


def banmen():
    print("SUGOROKU!!")
    print("-" * (player_position - 1) + "😀" + "-" * (30 - player_position))
    print("-" * (computer_position - 1) + "😈" + "-" * (30 - computer_position))


while ???:
    banmen()
    ???  # ここにユーザーからのインプットを受け取るとループが止まる！
    ???  # playerのコマを動かす
    ???  # computerのコマを動かす

```


#### ユーザーから見たプログラム
```
SUGOROKU!!
---------😀--------------------
--------------😈---------------
```

<details>

<summary> <b> Level 4 答え表示 </b> </summary>

<p>

```python
player_position = 1
computer_position = 1


def banmen():
    print("SUGOROKU!!")
    print("-" * (player_position - 1) + "😀" + "-" * (30 - player_position))
    print("-" * (computer_position - 1) + "😈" + "-" * (30 - computer_position))


while True:
    banmen()
    input("Press Enter!!!!")
    player_position = player_position + 1
    computer_position = computer_position + 1

```

</p>
</details>

<br></br>

---



















## Level ??:
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

<summary> <b> Level ??表示 </b> </summary>

<p>

```python

```

</p>
</details>