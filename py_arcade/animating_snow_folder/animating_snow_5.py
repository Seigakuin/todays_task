""" 
Animating Snow 05
Goal:
- 雪の粒が画面下の外に移動したら、再び上に戻す(ifを使用)

Exercises:
- 雪の粒が突然上に移動してしまうエラーを直す
    - エラー：　雪の粒が瞬間移動してしまう
    - 修正後：　雪が完全に画面外下へ消え、画面の上（外）から自然と降りてくる
    - ヒント：　画面外を判断する`if`文の`center_y`値を変更する、そして描き始める`centery_y`値も変更する
- 同じ縦に位置から降り始めるので、それをrandomにする
    - ヒント：　再描画するときの`center_x`値をランダムにする

"""
import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
	""" arcade 組み込みのクラス """
	
	def __init__(self):
		""" コンストラクタ """
		# 親クラスのコンストラクタに画面幅、画面高さ、画面の名前を表示
		super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "ARCADE EXAMPLE 5")
		
		# snow一粒一粒を入れておくlistを作成
		self.snow_list = []
		
		# あとでsnow_listに付け加えるための
		# 仮のsnowのステータスを作る
		# 一回限りだからselfが取れているのに注意!!!
		# for ループでたくさん作る
		for i in range(50):
			snow_status = {
				"center_x": random.randrange(0, SCREEN_WIDTH),
				"center_y": random.randrange(0, SCREEN_HEIGHT),
				"radius": random.randrange(10, 50),
			}
			# 上で作った仮のsnow_statusをsnow_listに付け加える
			self.snow_list.append(snow_status)
	
	def on_draw(self):
		""" 描かれるものを定義 """
		arcade.start_render()
		
		# snow_statusを使って、snowを作る
		# forループで作ったsnow_listに入っているたくさんの
		# ステータスからたくさん描く
		for snow in self.snow_list:
			# snow_listにある一つ一つのsnowを取り出す
			# 注意: snowはforループ中の仮の変数
			arcade.draw_circle_filled(
				snow["center_x"], snow["center_y"], snow["radius"],
				arcade.color.WHITE
			)
			if snow["center_y"] < 0:
				snow["center_y"] = SCREEN_HEIGHT
	
	def on_update(self, delta_time):
		""" 動きとゲームロジック """
		for snow in self.snow_list:
			snow["center_y"] -= 1
	
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
