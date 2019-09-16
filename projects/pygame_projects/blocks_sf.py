import sys
import math
import random
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, Rect


class Block:
    """ ブロック・ボール・パドルオブジェクト """

    def __init__(self, col, rect, speed=0):
        self.col = col
        self.rect = rect
        self.speed = speed
        self.dir = random.randint(-45, 45) + 270

    def move(self):
        """ ボールを動かす """
        self.rect.centerx += math.cos(math.radians(self.dir)) \
                             * self.speed
        self.rect.centery -= math.sin(math.radians(self.dir)) \
                             * self.speed

    def draw(self):
        """ ブロック・ボール・パドルを描画する """
        if self.speed == 0:
            pygame.draw.rect(SURFACE, self.col, self.rect)
        else:
            pygame.draw.ellipse(SURFACE, self.col, self.rect)


def tick():
    """ 毎フレーム処理 """
    global hits
    global BLOCKS
    # +++ NEW!!!! +++
    # SCOREグローバル変数を取得
    global SCORE

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                PADDLE.rect.centerx -= 10
            elif event.key == K_RIGHT:
                PADDLE.rect.centerx += 10
    if BALL.rect.centery < 1000:
        BALL.move()

    # ブロックと衝突？
    prevlen = len(BLOCKS)
    new_blocks = []
    for x in BLOCKS:
        if not x.rect.colliderect(BALL.rect):
            new_blocks.append(x)
        else:
            # +++ NEW!!!! +++
            # BLOCK と衝突したらスコアをアップデート
            SCORE = SCORE + 10

    BLOCKS = new_blocks
    if len(BLOCKS) != prevlen:
        BALL.dir *= -1

    # パドルと衝突？
    if PADDLE.rect.colliderect(BALL.rect):
        BALL.dir = 90 + (PADDLE.rect.centerx - BALL.rect.centerx) \
                   / PADDLE.rect.width * 80

    # 壁と衝突？
    if BALL.rect.centerx < 0 or BALL.rect.centerx > 600:
        BALL.dir = 180 - BALL.dir
    if BALL.rect.centery < 0:
        BALL.dir = -BALL.dir
        BALL.speed = 15


pygame.init()
pygame.key.set_repeat(5, 5)
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SURFACE = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FPSCLOCK = pygame.time.Clock()
BLOCKS = []
PADDLE = Block((242, 242, 0), Rect(300, 700, 100, 30))
BALL = Block((242, 242, 0), Rect(300, 400, 20, 20), 10)

# +++ NEW!!!! +++
# SCOREとHIGHSCORE グローバル変数を設定
SCORE = 0
HIGHSCORE = 0
hits = 0

BLACK = (255, 255, 255)
WHITE = (0, 0, 0)

font = pygame.font.SysFont(None, 76)
score_font = pygame.font.SysFont(None, 44)


def draw_text(text, font, surface, x, y):
    textobj = font.render(text, 1, BLACK)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)


#  NEW!!
# ユーザーがボタンを押したのを確認するfunction
def wait_for_player_to_press_key():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Pressing ESC quits.
                    pygame.quit()
                    sys.exit()
                return


# 画面を白くする
SURFACE.fill(WHITE)
# 文字を表示
draw_text("BLOCKS!!", font, SURFACE, SCREEN_WIDTH // 2,
          SCREEN_HEIGHT // 2)
draw_text("Press SPACE",
          font, SURFACE, SCREEN_WIDTH // 2,
          SCREEN_HEIGHT // 2 + 50)
pygame.display.update()
wait_for_player_to_press_key()


def main():
    """ メインルーチン """
    myfont = pygame.font.SysFont(None, 80)
    mess_clear = myfont.render("Cleared!", True, (255, 255, 0))
    fps = 30
    colors = [(255, 0, 0), (255, 165, 0), (242, 242, 0),
              (0, 128, 0), (128, 0, 128), (0, 0, 250)]

    # +++ NEW!!!! +++
    # game_over bool を作成 True に設定する (一度、イニシャライズをするため)
    game_over = False

    # Blockを初期化する
    for ypos, color in enumerate(colors, start=0):
        for xpos in range(0, 5):
            BLOCKS.append(Block(color,
                                Rect(xpos * 100 + 60, ypos * 50 + 40,
                                     80, 30)))

    while True:

        # +++ NEW!!!! +++
        # game_over が Trueの場合 (初回は実行される)
        if game_over:
            # グローバル変数として設定されているものを使えるように
            # global ???? を使用する
            global PADDLE
            global BALL
            global SCORE
            global HIGHSCORE

            # Blockを初期化する
            for ypos, color in enumerate(colors, start=0):
                for xpos in range(0, 5):
                    BLOCKS.append(Block(color,
                                        Rect(xpos * 100 + 60, ypos * 50 + 40,
                                             80, 30)))

            # SCOREがHIGHSCOREより高ければ更新
            if SCORE > HIGHSCORE:
                HIGHSCORE = SCORE

            # 画面を白くする
            SURFACE.fill(WHITE)

            # 画面にGame Overを表示
            draw_text("GAME OVER!!", font, SURFACE, SCREEN_WIDTH // 2,
                      SCREEN_HEIGHT // 2)
            draw_text("Press Key to Play Again", font, SURFACE,
                      SCREEN_WIDTH // 2,
                      SCREEN_HEIGHT // 2 + 50)
            # 画面を描画する
            pygame.display.update()
            # ユーザーがボタンを押すのを待つ
            wait_for_player_to_press_key()

            # 画面を描画
            pygame.display.update()
            wait_for_player_to_press_key()

            # !!! グローバル変数を初期値に戻す !!!
            PADDLE = Block((242, 242, 0), Rect(300, 700, 100, 30))
            BALL = Block((242, 242, 0), Rect(300, 400, 20, 20), 10)
            SCORE = 0

            # game_over を False に設定 (ゲームが再び始まる)
            game_over = False

        tick()

        SURFACE.fill((0, 0, 0))
        BALL.draw()
        PADDLE.draw()

        # +++ NEW!!!! +++
        # スコアを画面上部に表示
        draw_text("Score: " + str(SCORE), score_font, SURFACE,
                  SCREEN_WIDTH - 200, 20)
        draw_text("High Score: " + str(HIGHSCORE), score_font, SURFACE,
                  200, 20)

        for block in BLOCKS:
            block.draw()

        if len(BLOCKS) == 0:
            SURFACE.blit(mess_clear, (200, 400))
        if BALL.rect.centery > 800 and len(BLOCKS) > 0:
            game_over = True

        pygame.display.update()
        FPSCLOCK.tick(fps)


if __name__ == '__main__':
    main()
