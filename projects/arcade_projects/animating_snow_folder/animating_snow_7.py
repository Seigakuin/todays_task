""" 
Animating Snow 07
Goal:
- arcade.SpriteクラスからSnowクラスを継承しよう
    - こうすることにより各インスタンスが管理しやすくなる
    - 動きも良くなる
- Snowクラス自体に`update`メソッド(関数)を加え、動きを管理する
- Spriteクラスを継承してたSnowクラスをSpriteListクラスに入れることによって色々便利に管理できる
    - SpriteListクラスをforループを使わずに、直接`update()`をリストから呼び出すことができる

Exercises:
- Snowクラスのインスタンスの数を限界まで増やしてみよう
- (Difficult) Snowクラスのupdateに新たなルールをつけてみよう
    - ex. center_xのスタート位置を変える
    - ex. 再描画するときにradiusに変化をつける


"""
import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# ここでarcade.Spriteを継承する
class Snow(arcade.Sprite):
	def __init__(self, center_x, center_y, radius, speed):
		# 継承したクラスを初期化呼び出す
		super().__init__()
		
		self.center_x = center_x
		self.center_y = center_y
		self.radius = radius
		self.speed = speed
		
		# 継承したSpriteクラスにはtextureというステータスがある
		# このtextureにcircle入れる
		self.texture = arcade.make_soft_circle_texture(
			self.radius, arcade.color.WHITE)
	
	# 継承したSpriteクラスにはupdateという動き(Method)がある
	# ここに下に動くアニメーションを設定する
	def update(self):
		self.center_y -= self.speed
		
		# 画面下に移動してしまった場合
		# 画面上に移動させる
		if self.center_y < 0:
			self.center_y = SCREEN_HEIGHT


class MyGame(arcade.Window):
	""" arcade 組み込みのクラス """
	
	def __init__(self):
		""" コンストラクタ """
		# 親クラスのコンストラクタに画面幅、画面高さ、画面の名前を表示
		super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "ARCADE EXAMPLE 7")
		
		# Spriteクラスを継承していることにより
		# Snow をarcade.SpriteListに入れることができる！
		# snow一粒一粒を入れておくSpritelistを作成
		self.snow_list = arcade.SpriteList()
		
		# 仮のsnowのステータスを作る
		# 一回限りだからselfが取れているのに注意!!!
		# for ループでたくさん作る
		for i in range(100):
			# 各Snowインスタンスのステータスを作る
			x = random.randrange(0, SCREEN_WIDTH)
			y = random.randrange(0, SCREEN_HEIGHT)
			radius = random.randrange(10, 50)
			speed = random.randrange(1, 5)
			
			# Snowクラスを上記で作ったステータスでインスタンス化する
			snow = Snow(x, y, radius, speed)
			# 上で作った仮のSnowインスタンスをsnow_listに付け加える
			self.snow_list.append(snow)
	
	def on_draw(self):
		""" 描かれるものを定義 """
		arcade.start_render()
		
		# SpriteListだとdrawするのが便利！！
		# SpriteListクラスには、中にあるSpriteを描くdrawという動き(Method)
		# がある
		self.snow_list.draw()
	
	def on_update(self, delta_time):
		""" 動きとゲームロジック """
		
		# SpriteListだとupdateするのが便利！！
		# SpriteListクラスには、中にあるSpriteを描くupdateという動き(Method)がある
		# SpriteListにあるすべてのSpriteをupdateしてくれる
		self.snow_list.update()
	
	def on_key_press(self, key, modifiers):
		""" キーが押されたら """
		pass
	
	def on_key_release(self, key, modifiers):
		""" キーが離されたら """
		pass


def main():
	""" main method """
	window = MyGame()
	arcade.run()


if __name__ == "__main__":
	main()
