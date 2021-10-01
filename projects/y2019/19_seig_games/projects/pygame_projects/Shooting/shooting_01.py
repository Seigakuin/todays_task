import pygame
import random
import os

"""
level1: 
    player.pngでPlayerクラス
    player は右左と動く
    background.png で背景設定
   
level2:
    Bulletクラス実装
    bullet.pngを設定 
    
level2:
    Modクラス実装

level3:
    soundをつける
    
    BGM を設定
    
    Explosion アニメーション
        フレームごとに画像を設定
    
"""

###########################
# -- Set Constants: コンスタントを設定 --
###########################
WIDTH = 400
HEIGHT = 600
FPS = 80

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

###########################
# -- Set Assets: 使う部品の設定 --
###########################

# ディレクトリのパスを格納
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

###########################
# -- Initialize: 初期化 --
###########################
# pygame を初期化
pygame.init()
# ゲーム画面のSurfaceであるscreen を設定
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# ウィンドウ上部のタイトルを設定
pygame.display.set_caption("Shooting!")
# フレームを管理する時計をclockに格納
clock = pygame.time.Clock()


###########################
# -- Classes --
###########################
# ---- Player Class ----
class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

        # 最初の座標を設定
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10

        # 左右に動くスピード
        self.speedx = 0

    def update(self):
        self.speedx = 0

        # get_pressed()で現在押されているKeyの状態が含まれているdictionaryを返す
        # 押されている場合は True を返す
        keystate = pygame.key.get_pressed()

        # もし、K_LEFT、K_RIGHTが押されていたら
        # speedxを変更する
        if keystate[pygame.K_LEFT]:
            self.speedx = -10
        if keystate[pygame.K_RIGHT]:
            self.speedx = 10

        # player.rectに常にspeedx値を足す
        self.rect.x += self.speedx

        # もし、player.rectの右が画面幅より大きい場合
        if self.rect.right > WIDTH:
            # player.rectのrightは画面幅になる（つまり止まる）
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


# ---- LOAD IMAGES: 画像を読み込む ----
background = pygame.image.load(
    os.path.join(img_folder, "background.png")).convert()

# backgroundのRectを格納
background_rect = background.get_rect()

# player画像を読み込む
player_img = pygame.image.load(
    os.path.join(img_folder, "player.png")).convert()

# ---- SPRITES: スプライトの設定 ----
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

###########################
# -- Functions --
###########################


###########################
# -- GAME LOOP: ゲームループ --
###########################

# ゲームが走っているかを判断するBool値
running = True

while running:

    # ---- EVENTS: イベントを管理 ----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ---- UPDATE: 状態の更新 ----
    all_sprites.update()

    # ---- DRAW: 描写するもの準備 ----
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)

    # ---- FLIP: 画面を描く ----
    pygame.display.flip()

    # ---- フレームを空ける ----
    clock.tick(FPS)

pygame.quit()
