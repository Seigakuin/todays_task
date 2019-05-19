# クラスの勉強
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
