# :computer: SEIG PROGRAMMING CLUB :computer:
## SPRITE
### 目標：
- Sprite classの理解 `class Block(pygame.sprite.Sprite):`
- クラスの継承の理解 `class Block(pygame.sprite.Sprite):`
- 衝突判定の理解 `pygame.sprite.spritecollide(player, block_list, True)`



```python
import pygame
import sys
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# CLASS
# Spriteクラスを継承している
class Block(pygame.sprite.Sprite):
    # コンストラクタ
    def __init__(self, color, width, height):
        # Spriteクラスのコンストラクタを呼び出し、初期化
        super().__init__()

        # ブロックのSurfaceを設定
        self.image = pygame.Surface([width, height])
        # ブロックSurfaceの色を設定
        self.image.fill(color)
        # ブロックSurfaceのRectをself.rectに設定
        self.rect = self.image.get_rect()

    # 画面から消えたブロックを画面上部に戻す(reset)するためのfunction/method
    def reset_pos(self):
        self.rect.y = -20
        self.rect.x = random.randrange(700 - 20)

    # 画面を描く前に状況を更新するfunction/method
    def update(self):
        # ブロックは1ずつ降りてくる
        self.rect.y += 1

        # もし画面外に出たらreset_pos function を呼び出す
        if self.rect.y > 410:
            self.reset_pos()


# Playerクラス
# Blockクラスを継承している
class Player(Block):
    def __init__(self, color, width, height):
        # 継承元のBlockクラスのコンストラクタを呼び出す
        super(Block, self).__init__()

    # 画面を描く前に状況を更新するfunction/method
    def update(self):
        # マウスの位置を読み取る (x, y)
        pos = pygame.mouse.get_pos()

        self.rect.centerx = pos[0]  # x の座標
        self.rect.centery = pos[1]  # y の座標


# pygameを初期化
pygame.init()

# 画面のアスペクトを設定
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

# 空のBlockクラスインスタンスが入る集合(Group)を作る
block_list = pygame.sprite.Group()

# 空のPlayerクラスも含めた、Blockクラスインスタンスが入る集合(Group)を作る
all_sprites_list = pygame.sprite.Group()

# Blockのインスタンスをたくさん作る
for i in range(50):
    # Blockクラスのインスタンスを作成
    block = Block(BLACK, 20, 15)

    # ランダムに位置を設定
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    # ブロックGroupに作成したインスタンスを入れる
    block_list.add(block)
    # 全Groupにも入れる
    all_sprites_list.add(block)

# Playerクラスのインスタンスを作成
player = Player(RED, 20, 15)
# 全Groupに入れる
all_sprites_list.add(player)

# メインループの終了判定の変数
done = False

# フレームクラスのインスタンスを作成
clock = pygame.time.Clock()

# スコアを入れておく変数
score = 0

# ----- MAIN LOOP -----
while not done:
    # pygame全てのeventを読み取る
    for event in pygame.event.get():
        # eventがQUIT(画面を閉じる)だった場合は終了判定
        if event.type == pygame.QUIT:
            done = True
            sys.exit()

    # 画面を白く塗る
    screen.fill(WHITE)

    # --- UPDATE ---
    # 全Group の中のすべてのインスタンスを更新する
    # インスタンスの update function を呼び出す
    all_sprites_list.update()

    # player と衝突した block を　blocks_hit_listに格納する
    # True は「衝突した場合、画面から消す」という意味
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)

    # blocks_hit_listの長さに応じて点数を増やす
    for block in blocks_hit_list:
        score += 1
        # コンソールにスコアを表示
        print(score)

    # 全Groupを画面に描く
    # (draw functionを書いていないけど、これはSpriteクラスがすでに持っているfunction)
    all_sprites_list.draw(screen)

    # pygame 全体の画面を描く
    pygame.display.flip()
    # クロッククラスのtick functionを呼び出し、60ミリ秒ループを止める
    clock.tick(20)


# 念の為のpygame終了
pygame.quit()
sys.exit()

```
<br></br>

## :sparkles: チャレンジ :sparkles: 
1. block 一つ一つが別のスピードを持っているようにしよう
    * speedアトリビュート(属性)を付け加える
