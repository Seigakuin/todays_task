# Task: arcadeライブラリで図形描画
## テーマ：　図形を描こう



### 準備: PyCharmでの設定

* PyCharm -> Preference -> Project -> Project Interpreter -> '+' -> 'arcade'を検索 -> Install Package -> OK
* 

### Activity1: 画面を描く, 長方形を描く

```python

# arcadeライブラリをインポートする
import arcade

# ウィンドウを開く
# open_windowファンクションで開く
# ウィンドウのタイトルを "Drawing Example"とする
# ウィンドウのサイズを設定（幅width, 高さheight)
arcade.open_window(600, 600, "Drawing Example")

# backgroundの色を設定
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

# 描く準備
arcade.start_render()

# 長方形を描く(長方形の中心を起点）
# 座標(x: 100, y: 520) を中心に幅width 45, 高さheight25の長方形を描く
arcade.draw_rectangle_filled(100, 520, 45, 25, arcade.color.BLUSH)

# 描くのを終了
arcade.finish_render()

# ウィンドウを開き続ける（閉じるまで）
arcade.run()

```


### Activity2: 長方形を回転させる

```python
# 長方形を回転
# 座標 (200, 520) width of 45 and height of 25
# 45度回転する
arcade.draw_rectangle_filled(200, 520, 45, 25, arcade.color.BLUSH, 45)
```

### Activity3: 自分でAPIからFunctionを選び、画面に描く

#### [他のいろいろな形を描くfunction](http://arcade.academy/quick_index.html#id1)

#### [使用できる色一覧](http://arcade.academy/arcade.color.html?highlight=color#arcade-color-package)

### Activity4: draw_rect() ファンクションを作る
* xとy座標を受け取ると、長方形を描くファンクションを定義しましょう

```python
def draw_rect(x, y):
	???

# 座標(300, 300)に長方形を描く
draw_rect(300, 300)
# 座標(100, 250)に長方形を描く
draw_rect(100, 250)

```