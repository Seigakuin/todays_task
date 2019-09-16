# Arcade Project 04: 
## テーマ：　ユーザーインプットを受け取る
file: ch16_1.py



### 前回までのコード
#### ここのコピペからはじめてください。

```python
class Ball:
    def __init__(self, radius, color, pos_x, pos_y, change_x, change_y):
        """ コンストラクタ """
        self.radius = radius
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.change_x = change_x
        self.change_y = change_y

    def draw(self):
        """ 画面上に与えられた引数でボールを描く"""
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.radius, self.color)

    def update(self):
        """ ボールのデータの更新に使うメソッド """

        # ボールを動かす
        if self.pos_x < self.radius:
            self.change_x *= -1  # つまり逆方向に移動するということ

        if self.pos_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1

        if self.pos_y < self.radius:
            self.change_y *= -1

        if self.pos_y > SCREEN_HEIGHT - self.radius:
            self.change_y *= -1



class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # 背景の色を設定
        arcade.set_background_color(arcade.color.ASH_GREY)

        # ボールのリストを作成
        self.ball_list = ???

        # ボールを３つ足す
        self.ball = Ball(50, 50, 3, 3, 15, arcade.color.AUBURN)
        
    def on_draw(self):
    	""" windowが描かれるたびに呼び出されるメソッド """
        arcade.start_render()

        # ボールを描く
        self.ball.draw()
    
    def update(self, delta_time):
        """ 画面上にあるもののデータを更新するために呼び出されるメソッド
        毎秒約60回呼び出される
        """
        # ボールをアップデート
        self.ball.update()
            

def main():
    # Windowクラスを継承したMyGameクラスを使うと
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

    arcade.run()


main()

```
<br></br>
---






### Acitivity1: マウスのインプットを受け取る

- `MyGame`クラスの中に`on_mouse_motion()`メソッドを追加する
- マウスの位置にボールの位置が来る


### `MyGame`クラス

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
        # 省略
        
    def on_draw(self):
    	# 省略

	def on_mouse_motion(self, x, y, dx, dy):
		# dx, dyは今は無視
	    self.ball.pos_x = ???
	    self.ball.pos_y = ???

def main():
	# 省略

main()
```

<br></br>
---

### Acitivity2: 上下左右のインプットを受け取る

- グローバル変数に`MOVEMENT_SPEED`を追加

```python
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 3

```

- `MyGame`クラスの`on_key_press()`メソッドを更新

### `MyGame`クラス -> `on_key_press()`

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
        # 省略
        
    def on_draw(self):
    	# 省略

	def on_mouse_motion(self, x, y, dx, dy):
		# 省略

	def on_key_press(self, key, modifiers):
	    if key == arcade.key.LEFT:
	        self.ball.change_x = ???
	    elif key == arcade.key.RIGHT:
	        self.ball.change_x = ???
	    elif key == arcade.key.UP:
	        self.ball.change_y = ???
	    elif key == arcade.key.DOWN:
	        self.ball.change_y = ???

def main():
	# 省略

main()

```

