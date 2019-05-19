# クラスの勉強4
# クラスの継承(Inheritence)を理解しよう！
# 継承とは親となるクラスのフィールド、メソッドを再利用することです。
class Animal:
    def __init__(self, age, name, weight):
        self.age = age
        self.name = name
        self.weight = weight

    # クラスに「動作」を与えるために
    # クラスにメソッド（ファンクション）を定義する
    def cry(self):
        # 自分自身の名前 self.name を使う
        print("ガオー！  " + self.name + " より")


class Dog(Animal):
    def __init__(self, age, name, weight):
        # 親クラスに引数を渡すときに注意！！
        super().__init__(age, name, weight)  # Animalクラスのフィールドをすべて継承
        self.address = ""  # 犬専用のフィールドを設定

    def cry(self):
        # Animalクラスから継承したものをOverrideする
        # Overrideとは上書きすること
        print("ワンワン! " + self.name + " より")


def main():
    # Dogクラスのインスタンスを作成
    mydog = Dog(12, "シロ", 35)

    mydog.age = 12
    mydog.name = "シロ"
    mydog.weight = 5

    print("My dog's name is " + mydog.name)

    # bark()メソッドを呼び出す
    mydog.cry()


# メインファンクションを呼ぶのを忘れずに！
main()
