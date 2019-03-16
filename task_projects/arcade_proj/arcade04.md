# Arcade Project 04: 
## テーマ：　ユーザーインプットを受け取る
file: ch16_1.py

### Acitivity1: マウスのインプットを受け取る

- `MyGame`クラスの中に`on_mouse_motion()`メソッドを追加する
- マウスの位置にボールの位置が来る


### `MyGame`クラス

```python
def on_mouse_motion(self, x, y, dx, dy):
    self.ball.pos_x = ???
    self.ball.pos_y = ???
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
def on_key_press(self, key, modifiers):
    if key == arcade.key.LEFT:
        self.ball.change_x = ???
    elif key == arcade.key.RIGHT:
        self.ball.change_x = ???
    elif key == arcade.key.UP:
        self.ball.change_y = ???
    elif key == arcade.key.DOWN:
        self.ball.change_y = ???

```

