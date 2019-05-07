# クラスの勉強3
# __init__(self)メソッド(コンストラクタ) に引数を渡す
# 引数を渡すと、クラスのインスタンスを作成するのが楽になる！
class Animal:
    def __init__(self, age, name, weight):
        # ここが変化！！
        self.age = age
        self.name = name
        self.weight = weight

    # クラスに「動作」を与えるために
    # クラスにメソッド（ファンクション）を定義する
    def cry(self):
        # 自分自身の名前 self.name を使う
        print("ガオー！  " + self.name + " より")


def main():
    # Animalクラスのインスタンスを作成するときに引数を入力
    myanimal = Animal(12, "タロウ", 32)

    print("My animal's name is " + myanimal.name)

    # cry()メソッドを呼び出す
    myanimal.cry()


# メインファンクションを呼ぶのを忘れずに！
main()
