"""Pygame Zero Level 5 - 画像を動かそう！

1. update()ファンクションを新たに書こう
＊update()はフレームのたびに呼び出されるファンクション(1秒に60回呼び出される!)

2. その中にalien.left += 2を書こう
＊alienの左側の位置(left)を2ピクセルずつ、足していく(+=)指示

3. 上にある"プレイ"ボタンを押して実行しよう

4. 色々ば方向にalienを移動させよう

＊上下移動のためには alien.top（alienの上の位置)に数値を足したり引いたりすれば良い


"""
WIDTH = 800
HEIGHT = 600
TITLE = "HELLO"

alien = Actor("alien")
alien.pos = (300, 200)


def draw():
    screen.fill((255, 255, 255))
    alien.draw()

def update():
    alien.left += 2