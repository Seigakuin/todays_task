# Arcade Project 03: 
## テーマ：　Arcadeライブラリで定義されているクラスの勉強
file: ch15_4_1.py

### 前回までのコード
#### ここのコピペからはじめてください。

```python
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # 背景の色を設定
        arcade.set_background_color(arcade.color.ASH_GREY)


    def on_draw(self):
        """ windowが描かれるたびに呼び出されるメソッド """
        arcade.start_render()


def main():
    # 以前までは
    # arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

    # しかし、Windowクラスを継承したMyGameクラスを使うと
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

    arcade.run()


main()
```

<br></br>
---

### Acitivity1: Ballクラスを作成する

- 画面の大きさをグローバルに設定する　　(グローバルとはコード全体から読めるようにすること）
- `Ball`クラスを作成する	
	- 理由： クラスにすることにより、簡単な複数作成することができる




```python
import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Ball:
    def __init__(self, radius, color, pos_x, pos_y):
        """ コンストラクタ """
        self.radius = ???
        self.color = ???
        self.pos_x = ???
        self.pos_y = ???

    def draw(self):
        """ 画面上に与えられた引数でボールを描く"""
        arcade.draw_circle_filled(???, ???, ???, ???)
        
class MyGame(arcade.Window):
	# 省略

def main():
	# 省略

main()

```

<br></br>
---

### Acitivity2: Ballクラスを使ってボールを描く!

- `MyGame`クラスにコードを追加
	- `__init__()`に`Ball`インスタンスを追加
	- `on_draw()`に`Ball`インスタンスを追加

#### `__init__()`
#### `on_draw()`

```python
class MyGame(arcade.Window):
	def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # 背景の色を設定
        arcade.set_background_color(arcade.color.ASH_GREY)

        # Ballクラスのインスタンスを作成
        self.ball = Ball(???)

    def on_draw(self):
      	""" windowが描かれるたびに呼び出されるメソッド """
        arcade.start_render()
        self.ball.???

```

<br></br>
---

### Acitivity3: Ballクラスを使ってボールを動かす!

- `Ball`クラスに属性(Attribute)を追加する
	- `change_x`, `change_y` -> １フレームでどのくらい動くか（動く速さ）
- `update`ファンクション（メソッド）を加える (フレームごとにどのようにデータを更新するのか)


#### `__init__()`
#### `update()`
```python
class Ball:
    def __init__(self, radius, color, pos_x, pos_y, ???, ???):
        """ コンストラクタ """
        self.radius = ???
        self.color = ???
        self.pos_x = ???
        self.pos_y = ???
        self.change_x = ???
        self.change_y = ???

    def draw(self):
        # 省略

    def update(self):
        """ ボールのデータの更新に使うメソッド """

        # ボールを動かす
        self.pos_x += ???
        self.pos_y += ???

        # 壁にあたっているかの衝突判定
        if self.pos_x < ???:
            self.change_x *= -1 # つまり逆方向に移動するということ

        if self.pos_x > ???:
            self.change_x *= -1

        if self.pos_y < ???:
            self.change_y *= -1

        if self.pos_y > ???:
            self.change_y *= -1

class MyGame(arcade.Window):
	# 省略

def main():
	# 省略

main()

```


<br></br>
---


### Acitivity4: Ballクラスを使ってボールをたくさん動かす!

- `MyGame`クラスに`Ball`インスタンスを格納するための空のListを作成
- `Ball`インスタンスを複数追加　(`append()`を使用する！)
- `MyGame`クラスの`on_draw`メソッドに全てのボールを描くためのコードを書く (forループ使用！）

#### `MyGame`
#### `on_draw()`
```python
class Ball:
    def __init__(self, radius, color, pos_x, pos_y, ???, ???):
        # 省略

    def draw(self):
        # 省略

    def update(self):
    	# 省略



class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # 背景の色を設定
        arcade.set_background_color(arcade.color.ASH_GREY)

        # ボールのリストを作成
        self.ball_list = ???

        # 3つのボールを３つ足す
        ball = Ball(???)
        self.ball_list.???
        ball = Ball(???)
        self.ball_list.???
        ball = Ball(???)
        self.ball_list.???
        
    def on_draw(self):
    	""" windowが描かれるたびに呼び出されるメソッド """
        arcade.start_render()

        # forループでボールを一つ一つ描く
        for ??? in ???:
            ???
            

def main():
	# 省略

main()

```
---

