# Arcade Project 05: 
## テーマ：　スプライトを扱い、衝突判定をかつようする
file: ch18_1.py

### Acitivity1: まずはMyGameのテンプレートをコピー・ペーストする

- ??? - バックグラウンドの色は自分で指定する
- ??? - 描き始めるときに必ず呼び出すメソッド名はなんだっけ？
- ??? - arcadeを走らせるためのメソッド名は？

#### 出力: 指定した色の画面だけが描画される

```python
import arcade

# プレイヤー、ゴーストの大きさの比率
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_GHOST = 0.2
# ゴーストの出現数
GHOST_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


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

        # バックグラウンド色を自分の好きな色に
        arcade.set_background_color(???)

    def on_draw(self):
        # 描くのを始める
        arcade.???()


def main():
    """ Main method """
    window = MyGame()
    arcade.???()


if __name__ == "__main__":
    # 上で作ったmainファンクションを呼び出す
    main()
 

```

<br></br>
---

### Acitivity2: `MyGame`クラスに`setup()`メソッドを追加

- `MyGame`クラスに`setup()`メソッドを追加
- `on_draw()`メソッドにスプライトリストを描画するメソッド`.draw()`を追加
- `main()`に`setup()`を呼び出す


#### 出力: 画面の左下にプレイヤーが描画される

### `MyGame`クラスに追加

```python
    def setup(self):
        """ ゲームの変数を初期化し、ゲームを設定する """

        # スプライトの空リストを作成
        self.player_list = arcade.SpriteList()
        self.ghost_list = arcade.SpriteList()

        # スコアも０に設定
        self.score = 0

        # プレイヤーを設定
        # プレイヤーの大きさはSPRITE_SCALING_PLAYERで小さく
        self.player_sprite = arcade.Sprite("player.png",
                                           SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        # プレイヤースプライトリストに作ったプレイヤースプライトを追加
        self.player_list.append(self.player_sprite)

```

### `MyGame`クラスの`on_draw()`に追加
```python
    def on_draw(self):
        # 描くのを始める
        arcade.start_render()

        # NEW !! 
        # スプライトリスト全体をdraw()ファンクションで描く
        self.ghost_list.draw()
        self.player_list.draw()
```

### `main()`ファンクションに追加
```python
def main():
    """ Main method """
    window = MyGame()
    # NEW!!
    # MyGameクラスに追加した setup()ファンクションを呼び出し、
    # 変数を初期化する
    window.setup()
    arcade.run()
```

<br></br>
---

### Acitivity3: `MyGame`クラスに`setup()`メソッドを追加

- `MyGame`クラスに`setup()`内にたくさんのゴーストを作成する`for`ループを作成
- `on_draw()`メソッドにスプライトリストを描画するメソッド`.draw()`を追加
- `main()`に`setup()`を呼び出す


#### 出力: 画面にランダムでゴーストがたくさん描画される

### `MyGame`クラスの`setup()`に追加

```python
    def setup(self):
        """ ゲームの変数を初期化し、ゲームを設定する """

        # スプライトの空リストを作成
        self.player_list = arcade.SpriteList()
        self.ghost_list = arcade.SpriteList()

        # スコアも０に設定
        self.score = 0

        # プレイヤーを設定
        # プレイヤーの大きさはSPRITE_SCALING_PLAYERで小さく
        self.player_sprite = arcade.Sprite("player.png",
                                           SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        # プレイヤースプライトリストに作ったプレイヤースプライトを追加
        self.player_list.append(self.player_sprite)

        # NEW!!
        for i in range(GHOST_COUNT):
            # ゴーストのイメージを作成
            ghost = arcade.Sprite("ghost.png", SPRITE_SCALING_GHOST)

            # ゴーストの位置をランダムに設定
            ghost.center_x = random.randrange(SCREEN_WIDTH)
            ghost.center_y = random.randrange(SCREEN_HEIGHT)

            # ゴーストのスプライトリストにスプライトをたくさん追加
            self.ghost_list.append(ghost)
```

<br></br>
---

### Acitivity4: アニメーションと衝突判定を追加

- `on_draw()`にスコア(`self.score`)を画面上に描く - `.draw_text()`ファンクションを追加
- `MyGame`クラス内に新たに`on_mouse_motion()`メソッドを追加
- `MyGame`クラス内に新たに`update()`メソッドを追加


#### 出力: 画面のプレイヤーがマウスで動かし、ゴーストに衝突したらゴーストが消えるそして、スコアが増える

### `MyGame`クラスの`setup()`に追加

- `on_draw()`にスコア(`self.score`)を画面上に描く - `.draw_text()`ファンクションを追加


```python
    def on_draw(self):
        # 描くのを始める
        arcade.start_render()
        
        # スプライトリスト全体をdraw()ファンクションで描く
        self.ghost_list.draw()
        self.player_list.draw()

        # NEW !!
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
```

- `MyGame`クラス内に新たに`on_mouse_motion()`メソッドを追加

```python
    def on_mouse_motion(self, x, y, dx, dy):
        """ マウスの動きを制御 """

        # プレイヤースプライトの位置をマウスのx, y位置に移動
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y
```

- `MyGame`クラス内に新たに`update()`メソッドを追加

```python
# NEW !!
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
```
<br></br>
---

