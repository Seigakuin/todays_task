# クラスの勉強2
# クラスに加える、メソッド(ファンクション)を定義しよう
# メソッドとはそのクラスにある「動作」です。
# 例：Animalクラスがcry(鳴く)する
class Animal:
    def __init__(self):
        self.age = 0
        self.name = ""
        self.weight = 0

    # クラスに「動作」を与えるために
    # クラスにメソッド（ファンクション）を定義する
    def cry(self):
        # 自分自身の名前 self.name を使う
        print("ガオー！  " + self.name + " より")


def main():
    # Animalクラスのインスタンスを作成
    myanimal = Animal()

    myanimal.age = 3
    myanimal.name = "動物"
    myanimal.weight = 15

    print("My animal's name is " + myanimal.name)

    # cry()メソッドを呼び出す
    myanimal.cry()


# メインファンクションを呼ぶのを忘れずに！
main()
