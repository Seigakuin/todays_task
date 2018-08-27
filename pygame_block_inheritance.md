# :computer: SEIG PROGRAMMING CLUB :computer:
## BLOCK INHERITANCE
### 目標：
- classの継承を理解 `class Player(Block):`
    - 継承コンストラクタ(初期化)の理解 `super().__init__(color, width, height)`
* 前回のコードから更新された所は `#  NEW!!` 

```python
import pygame
import sys

# DEFINE SOME COLOR VARIABLES
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# CLASS
class Block:

    # コンストラクタ
    # アトリビュート(属性)に`color, width, height`を設定
    def __init__(self, color, width, height):

        # ブロックのSurfaceを設定
        self.image = pygame.Surface([width, height])
        # ブロックSurfaceの色を設定
        self.image.fill(color)
        # ブロックSurfaceのRectをself.rectに設定
        self.rect = self.image.get_rect()
        self.change_x = 1
        self.change_y = 1

    # 画面を描く前に状況を更新するfunction
    def update(self):
        self.rect.centerx += self.change_x
        self.rect.centery += self.change_y

    # 画面に描くためのfunction
    def draw(self, screen):
        screen.blit(self.image, self.rect)


# NEW!!!
# CLASS
class Player(Block):

    # コンストラクタ
    # アトリビュート(属性)に`color, width, height`を設定
    def __init__(self, color, width, height):
        # 継承元のBlockクラスのコンストラクタを呼び出す
        super().__init__(color, width, height)
        self.change_x = 2
        self.change_y = 3

    # 画面を描く前に状況を更新するfunction
    def update(self):
        self.rect.centerx += self.change_x
        self.rect.centery += self.change_y


# pygameを初期化
pygame.init()

# 画面のアスペクトを設定
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])


# Blockクラスのインスタンスを作成
block = Block(RED, 20, 15)

# NEW!!!
# Playerクラスのインスタンスを作成
player = Player(GREEN, 30, 20)

# メインループの終了判定の変
done = False

# フレームクラスのインスタンスを作成
clock = pygame.time.Clock()


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
    # ブロッククラスの更新functionを呼び出す
    block.update()

    # NEW!!!
    # Playerクラスの更新functionを呼び出す
    player.update()

    # --- DRAW ---
    # ブロッククラスを描くfunctionを呼び出す
    block.draw(screen)

    # NEW!!!
    # Playerクラスを描くfunctionを呼び出す
    player.draw(screen)

    # pygame 全体の画面を描く
    pygame.display.flip()
    # クロッククラスのtick functionを呼び出し、60ミリ秒ループを止める
    clock.tick(60)


# 念の為のpygame終了
pygame.quit()
sys.exit()
```
