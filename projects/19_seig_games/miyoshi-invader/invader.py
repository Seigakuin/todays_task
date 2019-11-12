# -*- coding: utf8 -*-
import sys
from random import randint
import pygame
from pygame.locals import Rect, QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_SPACE

pygame.init()
pygame.key.set_repeat(5, 5)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SURFACE = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
FPSCLOCK = pygame.time.Clock()

BLACK = (255, 255, 255)
WHITE = (0, 0, 0)

ship_image = pygame.image.load("player.png")


class Drawable:
    """ 全ての描画オブジェクトのスーパークラス """

    def __init__(self, rect, offset0, offset1):
        strip = pygame.image.load("strip.png")
        self.images = (
            pygame.Surface((24, 24), pygame.SRCALPHA),
            pygame.Surface((24, 24), pygame.SRCALPHA),
        )
        self.rect = rect
        self.count = 0
        self.images[0].blit(strip, (0, 0), Rect(offset0, 0, 24, 24))
        self.images[1].blit(strip, (0, 0), Rect(offset1, 0, 24, 24))

    def move(self, diff_x, diff_y):
        """ オブジェクトを移動 """
        self.count += 1
        self.rect.move_ip(diff_x, diff_y)

    def draw(self):
        """ オブジェクトを描画 """
        image = self.images[0] if self.count % 2 == 0 else self.images[1]
        SURFACE.blit(image, self.rect.topleft)


class Ship(Drawable):
    """ 自機オブジェクト """

    def __init__(self):
        super().__init__(Rect(300, 550, 24, 24), 192, 192)
        # self.images = [ship_image, ship_image]


class Beam(Drawable):
    """ ビームオブジェクト """

    def __init__(self):
        super().__init__(Rect(300, 0, 24, 24), 0, 24)


class Bomb(Drawable):
    """ 爆弾オブジェクト """

    def __init__(self):
        super().__init__(Rect(300, -50, 24, 24), 48, 72)
        self.time = randint(5, 220)


class Alien(Drawable):
    """ エイリアンオブジェクト """

    def __init__(self, rect, offset, score):
        super().__init__(rect, offset, offset + 24)
        self.score = score


font = pygame.font.SysFont(None, 76)
score_font = pygame.font.SysFont(None, 44)


def draw_text(text, font, surface, x, y):
    textobj = font.render(text, 1, BLACK)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)


# NEW!!
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
draw_text("invader!!", font, SURFACE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
draw_text(
    "Press SPACE", font, SURFACE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50
)
pygame.display.update()
wait_for_player_to_press_key()


def main():
    global SURFACE
    """ メインルーチン """
    sysfont = pygame.font.SysFont(None, 72)
    scorefont = pygame.font.SysFont(None, 36)
    message_clear = sysfont.render("!!Yarimasune!!", True, (0, 255, 0))
    message_over = sysfont.render("You lose!!", True, (255, 255, 255))
    message_rect = message_clear.get_rect()
    message_rect.center = (300, 300)
    game_over = False
    moving_left = True
    moving_down = False
    move_interval = 20
    counter = 0
    score = 0
    aliens = []
    bombs = []
    ship = Ship()
    beam = Beam()
    # beams = pygame.sprite.Group()

    # エイリアンの並びを初期化
    for ypos in range(4):
        offset = 96 if ypos < 2 else 144
        for xpos in range(10):
            rect = Rect(100 + xpos * 50, ypos * 50 + 50, 24, 24)  #!!!!!!! 24
            alien = Alien(rect, offset, (4 - ypos) * 10)
            aliens.append(alien)

    # 爆弾を設定
    for _ in range(4):
        bombs.append(Bomb())

    while True:

        ship_move_x = 0
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    ship_move_x = -8
                elif event.key == K_RIGHT:
                    ship_move_x = +8
                elif event.key == K_SPACE:
                    # elif event.key == K_SPACE and beam.rect.bottom < 0:
                    beam.rect.center = ship.rect.center

        if not game_over:
            counter += 1
            # 自機を移動
            ship.move(ship_move_x, 0)

            # ビームを移動
            beam.move(0, -30)

            # エイリアンを移動
            area = aliens[0].rect.copy()
            for alien in aliens:
                area.union_ip(alien.rect)

            if counter % move_interval == 0:
                move_x = -5 if moving_left else 5
                move_y = 0

                if (area.left < 10 or area.right > 590) and not moving_down:
                    moving_left = not moving_left
                    move_x, move_y = 0, 24
                    move_interval = max(5, move_interval - 1)
                    moving_down = True
                else:
                    moving_down = False

                for alien in aliens:
                    alien.move(move_x, move_y)

            if area.bottom > 550:
                game_over = True

            # 爆弾を移動
            for bomb in bombs:
                if bomb.time < counter and bomb.rect.top < 0:
                    enemy = aliens[randint(0, len(aliens) - 1)]
                    bomb.rect.center = enemy.rect.center

                if bomb.rect.top > 0:
                    bomb.move(0, 10)

                if bomb.rect.top > 600:
                    bomb.time += randint(50, 250)
                    bomb.rect.top = -50

                if bomb.rect.colliderect(ship.rect):
                    game_over = True

            # ビームがエイリアンと衝突?
            tmp = []
            for alien in aliens:
                if alien.rect.collidepoint(beam.rect.center):
                    beam.rect.top = -50
                    score += alien.score
                else:
                    tmp.append(alien)
            aliens = tmp
            if len(aliens) == 0:
                game_over = True

        # 描画
        SURFACE.fill((0, 0, 0))
        for alien in aliens:
            alien.draw()
        ship.draw()
        beam.draw()
        for bomb in bombs:
            bomb.draw()

        score_str = str(score).zfill(5)
        score_image = scorefont.render(score_str, True, (0, 255, 0))
        SURFACE.blit(score_image, (500, 10))

        if game_over:
            if len(aliens) == 0:
                SURFACE.blit(message_clear, message_rect.topleft)
            else:
                SURFACE.blit(message_over, message_rect.topleft)
            pygame.display.update()
            wait_for_player_to_press_key()
            game_over = False
            moving_left = True
            moving_down = False
            move_interval = 10
            counter = 0
            score = 0
            aliens = []
            bombs = []
            ship = Ship()
            beam = Beam()

            # エイリアンの並びを初期化
            for ypos in range(4):
                offset = 96 if ypos < 2 else 144
                for xpos in range(10):
                    rect = Rect(100 + xpos * 50, ypos * 50 + 50, 24, 24)
                    alien = Alien(rect, offset, (4 - ypos) * 10)
                    aliens.append(alien)

            # 爆弾を設定
            for _ in range(4):
                bombs.append(Bomb())

        pygame.display.update()
        FPSCLOCK.tick(60)


if __name__ == "__main__":
    main()
