# Arcade Project 06: 
## テーマ：　スプライトを動かす
file: ch19_1.py


### 前回までのコード
#### ここのコピペからはじめてください。

```python
import random
import arcade

# プレイヤー、ゴーストの大きさの比率
SPRITE_SCALING_PLAYER = 0.2
SPRITE_SCALING_GHOST = 0.02
# ゴーストの出現数
GHOST_COUNT = 80

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Ghost(arcade.Sprite):
    """ Ghost Class
    """

    def update(self):
        # Ghostの初期位置を設定し、動かす
        pass


class MyGame(arcade.Window):
    """ arcade 組み込みのクラス """

    def __init__(self):
        """ コンストラクタ """
        # 親クラスのコンストラクタに画面幅、画面高さ、画面の名前を表示
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # プレイヤーのリスト、ゴーストリストの空を作成
        self.player_list = None
        self.ghost_list = None

        # プレイヤーのスプライトの空を作成
        self.player_sprite = None
        # スコアを0点で初期化
        self.score = 0

        # マウスを画面上で非表示にする
        self.set_mouse_visible(False)

        # バックグラウンド色を緑に
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ ゲームの変数を初期化し、ゲームを設定する """

        # スプライトの空リストを作成
        self.player_list = arcade.SpriteList()
        self.ghost_list = arcade.SpriteList()

        # スコアも０に設定
        self.score = 0

        # プレイヤーを設定
        # プレイヤーの大きさはSPRITE_SCALING_PLAYERで小さく
        self.player_sprite = arcade.Sprite("./player.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        # プレイヤースプライトリストに作ったプレイヤースプライトを追加
        self.player_list.append(self.player_sprite)

        # Ghostの作成
        for _ in range(GHOST_COUNT):
            # ゴーストのイメージを作成
            ghost = Ghost("ghost.png", SPRITE_SCALING_GHOST)

            # ゴーストの位置をランダムに設定
            ghost.center_x = random.randrange(SCREEN_WIDTH)
            ghost.center_y = random.randrange(SCREEN_HEIGHT)

            # ゴーストのスプライトリストにスプライトをたくさん追加
            self.ghost_list.append(ghost)

    def on_draw(self):
        # 描くのを始める
        arcade.start_render()
        # スプライトリスト全体をdraw()ファンクションで描く
        self.ghost_list.draw()
        self.player_list.draw()

        # 　スコアを描く
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ マウスの動きを制御 """
        # プレイヤースプライトの位置をマウスのx, y位置に移動
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ 動きとゲームロジック """
        # 全てのスプライトのupdate()ファンクションを呼び出す
        self.ghost_list.update()

        # プレイヤーと衝突したスプライトのリストを作成する
        # 衝突したものになにかをする時に便利！
        ghost_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.ghost_list
        )

        # 衝突したものリストをforループでさらい、消す(kill())
        # 衝突したら、スコアに足す
        for ghost in ghost_hit_list:
            ghost.kill()
            self.score += 1


def main():
    """ Main method """
    window = MyGame()
    # NEW!! ch18_2
    # MyGameクラスに追加した setup()ファンクションを呼び出し、
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

```
<br></br>
---



### Acitivity1: Spriteを下に動かす

- `Ghost`クラスを作成、`update()`メソッドを追加



#### 出力: `ghost.png`が複数描画され、下にゆっくり動く

### `Ghost`クラスに追加

```python
# コンスタント設定
# 省略


class Ghost(arcade.Sprite):
    """ Ghost Class
    """

    def update(self):
        # Ghostの初期位置を設定し、動かす
        self.center_y -= 1


class MyGame(arcade.Window):
    """ arcade 組み込みのクラス """

    def __init__(self):
        # 省略
        
    def setup(self):
        # 省略

    def on_draw(self):
        # 省略

    def on_mouse_motion(self, x, y, dx, dy):
        # 省略
    def update(self, delta_time):
        # 省略

def main():
    # 省略

if __name__ == "__main__":
    main()

```
<br></br>
---

### Acitivity2: Spriteが画面外に出たら上に戻す

- `update()`メソッドに新たなロジックを追加



#### 出力: `ghost.png`spriteが画面外に出たら上にまた戻ってまた描画される

### `update`メソッドにロジックを追加

```python
# コンスタント設定
# 省略


class Ghost(arcade.Sprite):
    """ Ghost Class
    """

    def update(self):
        # Ghostの初期位置を設定し、動かす
        self.center_y -= 1
    
    # 画面外にGhostが行ったら
    if self.top < 0:  # 完全に画面外にするためtopで判断
        # 画面外に行ったら場所をランダムな位置にリセット
        self.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)


class MyGame(arcade.Window):
    """ arcade 組み込みのクラス """

    def __init__(self):
        # 省略
        
    def setup(self):
        # 省略

    def on_draw(self):
        # 省略

    def on_mouse_motion(self, x, y, dx, dy):
        # 省略
    def update(self, delta_time):
        # 省略

def main():
    # 省略

if __name__ == "__main__":
    main()

```
<br></br>
---

### Acitivity3: Spriteを上に戻す位置をランダムにする

- `update()`メソッドに新たなロジックを追加
- `reset_pos()`メソッドを追加する



#### 出力: `ghost.png`spriteが画面外に出たら上にまた戻ってまたランダムな位置に描画される

### `update`メソッドにロジックを追加
### `reset_pos()`メソッドを追加する

```python
# コンスタント設定
# 省略


class Ghost(arcade.Sprite):
    """ Ghost Class
    """

    def update(self):
        # Ghostの初期位置を設定し、動かす
        self.center_y -= 1
        # 画面外にGhostが行ったら
        if self.top < 0:  # 完全に画面外にするためtopで判断
            # NEW 19_3
            self.reset_pos()
    
    def reset_pos(self):
        """ Ghostの位置を画面の上の位置にリセット
        """
        self.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)


class MyGame(arcade.Window):
    """ arcade 組み込みのクラス """

    def __init__(self):
        # 省略
        
    def setup(self):
        # 省略

    def on_draw(self):
        # 省略

    def on_mouse_motion(self, x, y, dx, dy):
        # 省略
    def update(self, delta_time):
        # 省略

def main():
    # 省略

if __name__ == "__main__":
    main()

```
<br></br>
---

### Acitivity4: Spriteをランダムな方向に動かし、跳ね返るようにする

- `Ghost`クラスに`__init__()`メソッドを追加
- `update()`メソッドに新たなロジックを追加
- `reset_pos()`メソッドを消す



#### 出力: `ghost.png`spriteが画面中動き回り、壁から跳ね返る


```python
# コンスタント設定
# 省略


class Ghost(arcade.Sprite):
    """ Ghost Class
    """
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)
        # Ghostの初期位置を設定し、動かす
        self.center_x = 0
        self.center_y = 0

    def update(self):
        # Ghostの初期位置を設定し、動かす
        self.center_x += self.change_x
        self.center_y += self.change_y

        # 画面の端にいったら跳ね返す
        if self.left < 0:
            self.change_x *= -1
        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1
        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class MyGame(arcade.Window):
    """ arcade 組み込みのクラス """

    def __init__(self):
        # 省略
        
    def setup(self):
        # 省略

    def on_draw(self):
        # 省略

    def on_mouse_motion(self, x, y, dx, dy):
        # 省略
    def update(self, delta_time):
        # 省略

def main():
    # 省略

if __name__ == "__main__":
    main()

```
<br></br>
---


### Acitivity5: Spriteが円を描くように動く

- `math`ライブラリを`import`
- `Ghost`クラスの中の`__init__()`メソッドに新たなロジックを追加
- `Ghost`クラスの中の`update()`メソッドに新たなロジックを追加
- `MyGame`クラスの中の`setup()`メソッドに新たなロジックを追加



#### 出力: `ghost.png`spriteが画面中動き回り、壁から跳ね返る


```python
# コンスタント設定
import random
import math
import arcade

# 省略


class Ghost(arcade.Sprite):
    """ Ghost Class
    """
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)
        # 角度を示すラジアン
        self.circle_angle = 0

        # 中心からの距離（半径）
        self.circle_radius = 0

        # 周る速さ（ラジアン）
        self.circle_speed = 0.02

        # Ghostの初期位置を設定し、動かす
        self.circle_center_x = 0
        self.circle_center_y = 0

    def update(self):
    
        self.center_x = (
            self.circle_radius * math.sin(self.circle_angle) + self.circle_center_x
        )
        self.center_y = (
            self.circle_radius * math.cos(self.circle_angle) + self.circle_center_y
        )

        # 角度を足す
        self.circle_angle += self.circle_speed


class MyGame(arcade.Window):
    """ arcade 組み込みのクラス """

    def __init__(self):
        # 省略
        
    def setup(self):
        """ ゲームの変数を初期化し、ゲームを設定する """

        # スプライトの空リストを作成
        self.player_list = arcade.SpriteList()
        self.ghost_list = arcade.SpriteList()

        # スコアも０に設定
        self.score = 0

        # プレイヤーを設定
        # プレイヤーの大きさはSPRITE_SCALING_PLAYERで小さく
        self.player_sprite = arcade.Sprite("./player.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        # プレイヤースプライトリストに作ったプレイヤースプライトを追加
        self.player_list.append(self.player_sprite)

        # Ghostの作成
        for _ in range(GHOST_COUNT):
            # ゴーストのイメージを作成
            ghost = Ghost("ghost.png", SPRITE_SCALING_GHOST)

            # ゴーストの位置をランダムに設定
            # NEW 19_5
            ghost.circle_center_x = random.randrange(SCREEN_WIDTH)
            ghost.circle_center_y = random.randrange(SCREEN_HEIGHT)

            # NEW 19_5
            # 開始半径をランダム
            ghost.circle_radius = random.randrange(10, 200)

            # NEW 19_5
            # 開始角度をランダム
            ghost.circle_angle = random.random() * 2 * math.pi

            # ゴーストのスプライトリストにスプライトをたくさん追加
            self.ghost_list.append(ghost)

    def on_draw(self):
        # 省略

    def on_mouse_motion(self, x, y, dx, dy):
        # 省略
    def update(self, delta_time):
        # 省略

def main():
    # 省略

if __name__ == "__main__":
    main()

```
<br></br>
---
