# Arcade Project: 
## テーマ：　クラスの勉強

### クラスとは

- バラバラのコードをまとめることができる
- コードを「もの」(オブジェクト)と捉えることができる
- オブジェクトとは実際に世の中にあるもの(例: 住所、動物、犬)
- クラスはあくまで青写真・設計図　インスタンス（実体)を作って初めて「もの」になる


### Activity1: Addressクラスを定義する

*  「住所」というクラス（設計図）を作りましょう

#### [注意]
* `main()`ファンクションに実行するコードをまとめておくと後で便利 (最後に`main()`を呼ぶのを忘れずに)


```python
class Address:
    """ 住所を記録する """

    def __init__(self):
        """ __init__はクラスの中に定義する特別なファンクション(メソッド)
        Addressのインスタンスを作った時の初期値(initial)を設定する
        """
        self.country = ""
        self.prefecture = ""
        self.city = ""
        self.banchi = ""


def main():
    # 定義したAddressクラスを使ってインスタンスを作る
    my_address = Address()

    # 定義したフィールドにデータを入れる
    my_address.country = "Japan"
    my_address.prefecture = "Tokyo"
    my_address.city = "Nakazato"
    my_address.banchi = "1-13-4"

    print("My address is " + my_address.country)


main()
```


### Activity2: Animalクラスを定義し、「動作」(メソッド)を加える

* クラスに加える、メソッド(ファンクション)を定義しよう
* メソッドとはそのクラスにある「動作」です。
* 例：Animalクラスがcry(鳴く)する

#### [注目]

* Animalクラスの中に`cry()`が足されている

```python
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

```


### Activity3: Animalクラスのコンストラクタに引数を渡そう

* `__init__(self)`メソッド(コンストラクタ) に引数を渡す
* `__init__(self)`メソッドとはクラスをインスタンス化(実体化)する時に呼び出される（初期値)
* 引数を渡すと、クラスのインスタンスを作成するのが楽になる！


#### [注目]

* `__init__()` の中に`age, name, weight`という引数が増えている
* `main()`で`Animal()`をインスタンス化するときに引数を入力する`(12, "タロウ", 32)`

```python
class Animal:
    def __init__(self, age, name, weight):
        # !!!!!!NEW!!!!!!
        self.age = age
        self.name = name
        self.weight = weight

	
    # クラスに「動作」を与えるために
    # クラスにメソッド（ファンクション）を定義する
    def cry(self):
        # 自分自身の名前 self.name を使う
        print("ガオー！  " + self.name + " より")


def main():
    # !!!!!!NEW!!!!!!
    # Animalクラスのインスタンスを作成するときに引数を入力
    myanimal = Animal(12, "タロウ", 32)

    print("My animal's name is " + myanimal.name)

    # cry()メソッドを呼び出す
    myanimal.cry()


# メインファンクションを呼ぶのを忘れずに！
main()

```


### Activity4: Animalクラスを継承し、Dogクラスを定義しよう

* クラスの継承(Inheritence)を理解しよう！
* 継承とは親となるクラスのフィールド、メソッドを再利用することです。
* 継承をすると、同じコードを何度も書かなくて良くなる

#### [注目]

* `__init__()`の中に`super().__init__(age, name, weight)`を呼び出している
* `cry()`メソッドをAnimalクラスから継承しているけど、変えるためにOverride(上書き)している


```python
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

# !!!!!!NEW!!!!!!
class Dog(Animal):
    def __init__(self, age, name, weight):
        # 親クラスに引数を渡すときに注意！！
        # !!!!!!NEW!!!!!!
        super().__init__(age, name, weight)  # Animalクラスのフィールドをすべて継承
        self.address = ""  # 犬専用のフィールドを設定

    def cry(self):
    	 # !!!!!!NEW!!!!!!
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

```