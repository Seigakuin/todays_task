# Arcade Project 02: 
## テーマ：　Arcadeライブラリで定義されているクラスの勉強

### Acitivity1: arcade.Windowを継承する

- `arcade.Window`クラスを、自分で名付ける`MyGame`クラスに継承する(Interitance)

- `arcade.Window`を継承する利点
	- すでにたくさんのメソッド(ファンクション)が定義されている
	- ex. `on_draw()`: windowが呼び出されるたびに実行されるメソッド(アニメーションするには必須！！)
	- ex. `update()`: 画面上にあるクラス(例: ボールなど）のデータを更新するために呼び出されるメソッド(アニメーションするには必須！！)


### Activity1: Addressクラスを定義する

*  「住所」というクラス（設計図）を作りましょう

#### [注意]
* `main()`ファンクションに実行するコードをまとめておくと後で便利 (最後に`main()`を呼ぶのを忘れずに)


```python
import arcade


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # 背景の色を設定
        arcade.set_background_color(arcade.color.ASH_GREY)

    def on_draw(self):
        """ windowが描かれるたびに呼び出されるメソッド """
        arcade.start_render()

        # 画面に赤い点を描く(左したに)
        arcade.draw_circle_filled(50, 50, 15, arcade.color.AUBURN)
```


### Activity2: `MyGame`クラスに`on_draw()`メソッドを追加

* 画面に円を描く

#### [注目]

* `finish_render()`が必要ない！！`arcade.Window`が勝手に処理してくれる
* `arcade.open_window()`が必要ない！！

```python
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # 背景の色を設定
        arcade.set_background_color(arcade.color.ASH_GREY)

    def on_draw(self):
        """ windowが描かれるたびに呼び出されるメソッド """
        arcade.start_render()

        # 画面に赤い点を描く(左したに)
        arcade.draw_circle_filled(50, 50, 15, arcade.color.AUBURN)


def main():
    # 以前までは
    # arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

    # しかし、Windowクラスを継承したMyGameクラスを使うと
    window = MyGame(640, 480, "Drawing Example")

    arcade.run()


main()
```


### Activity3: アニメーションを作ろう！！

* クラスに属性を加える(`self.ball_x`, `self.ball_y`
* `update()`メソッドでフレームごとにballの位置のデータをアップデートし、`on_draw()`で画面上に描く
* 完成すれば画面のボールが動くはず！


#### [注目]

* `__init__()`の中身に属性が加えられている
* `update()`でデータを更新している

```python
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # 背景の色を設定
        arcade.set_background_color(arcade.color.ASH_GREY)

        # Attribute(属性)を設定
        self.ball_x = 50
        self.ball_y = 50

    def on_draw(self):
        """ windowが描かれるたびに呼び出されるメソッド """
        arcade.start_render()

        # 画面に赤い点を描く(左したに)
        arcade.draw_circle_filled(self.ball_x, self.ball_y, 15,
                                  arcade.color.AUBURN)

    def update(self, delta_time):
        """ 画面上にあるもののデータを更新するために呼び出されるメソッド
        毎秒約60回呼び出される
        """
        self.ball_x += 1
        self.ball_y += 1


def main():
    # 以前までは
    # arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

    # しかし、Windowクラスを継承したMyGameクラスを使うと
    window = MyGame(640, 480, "Drawing Example")

    arcade.run()


main()
```

