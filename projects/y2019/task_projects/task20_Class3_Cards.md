# 課題  Level 20 
## テーマ：Class 3

<br></br>
### 1
#### 課題： クラスを実際に使ってみよう `Player` クラスを作ろう
#### レベル： Hard
<br></br>
### pseudo code (疑似コード)
- カードゲームの `Player` クラスを作成しなさい `Player` クラスは `hand` と `name` というプロパティを持っている
  - `hand` は空の配列を初期値として入れる ex. []
  - `name` は好きな名前をクラス作成時に引数として受け取る
- `add_card_to_hand(self, card)` を作成
  - `card` を受け取って、自分のプロパティ `hand` に保存する (`.append()` を使用する)
  - `card` が `None` (空)だった場合はなにもしないようにする (`if` を使用する)
- `remove_card_from_hand(self, card)` を作成
  - `card` を受け取って、自分のプロパティ `hand` にそれがある場合はその`card` を消す (`.remove()` を使用する)


ベース
```python
class Player:
    def __init__(self):
        ????
        ????
    
    def add_card_to_hand(self, card):
        ????
    
    def remove_card_from_hand(self, card):
        ????

```
<br></br>
### 2
#### 課題： クラスを実際に使ってみよう `CardDeck` クラスを作ろう
#### レベル： Difficult
<br></br>
### pseudo code (疑似コード)
- カードゲームの `CardDeck` クラスを作成しなさい `CardDeck` クラスは `deck` というプロパティを持っている
  - `deck` は List である。初期値はベタ打ちで良い
- `get_card(self)` を作成
  - `card` を `deck` のなかからランダムに選ぶ (`choice()`を使用する) * `import random` をファイルの上部に書く必要あり!!
  - 選ばれた `card` を`deck` の中から消す
  - その選ばれたカードを返す (`return`)


<br></br>
ベース
```python
class CardDeck:
    def __init__(self):
        self.deck = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']

    def get_card(self, card):
        ????

```



<br></br>

実行例
```python
"""
>>> player1 = Player("Taro")
>>> player2 = Player("Kenta")
>>> deck = CardDeck()

card1 = deck.get_card()
player1.add_card_to_hand(card1)

"""
```

[back home](https://github.com/Seigakuin/todays_task)
