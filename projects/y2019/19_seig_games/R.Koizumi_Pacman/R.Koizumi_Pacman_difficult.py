""" asteroid.py - Copyright 2016 Kenichiro Tanaka """
import sys
from math import radians, sin, cos
from random import randint
import pygame
from pygame.locals import (
    Rect,
    QUIT,
    KEYDOWN,
    KEYUP,
    K_SPACE,
    K_LEFT,
    K_RIGHT,
    K_UP,
    K_DOWN,
)

# SIZE
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (37, 211, 102)
YELLOW = (255, 212, 0)

pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
FPSCLOCK = pygame.time.Clock()


class Drawable:
    """ 全ての描画オブジェクトの親クラス """

    def __init__(self, rect):
        self.rect = rect
        self.step = [0, 0]

    def move(self):
        """ 描画対象を移動する """
        rect = self.rect.center
        xpos = (rect[0] + self.step[0]) % SCREEN_WIDTH
        ypos = (rect[1] + self.step[1]) % SCREEN_HEIGHT
        self.rect.center = (xpos, ypos)


class Rock(Drawable):
    """ 隕石オブジェクト """

    def __init__(self, pos, size):
        super(Rock, self).__init__(Rect(0, 0, size, size))
        self.rect.center = pos
        self.image = pygame.image.load("newrock.png")
        self.theta = randint(0, 360)
        self.size = size
        self.power = 128 / size
        self.step[0] = cos(radians(self.theta)) * self.power
        self.step[1] = sin(radians(self.theta)) * -self.power

    def draw(self):
        """ 隕石を描画する """
        rotated = pygame.transform.rotozoom(
            self.image, self.theta, self.size / 64
        )
        rect = rotated.get_rect()
        rect.center = self.rect.center
        SURFACE.blit(rotated, rect)

    def tick(self):
        """ 隕石を移動する """
        self.theta += 3
        self.move()


class Shot(Drawable):
    """ 弾丸オブジェクト """

    def __init__(self, theta):
        super(Shot, self).__init__(Rect(0, 0, 6, 6))
        self.count = 50
        self.power = 10
        self.max_count = 50

        # #
        self.theta = theta
        self.accel = 0
        self.explode = False
        self.image = pygame.image.load("newbullet.png")

    def draw(self):
        """ 弾丸を描画する """

        rotated = pygame.transform.rotate(self.image, self.theta + 90)
        rect = rotated.get_rect()
        rect.center = self.rect.center
        # SURFACE.blit(rotated, rect)

        if self.count < self.max_count:
            SURFACE.blit(rotated, rect)

        # if self.count < self.max_count:
        #     pygame.draw.rect(SURFACE, (225, 225, 0), self.rect)

    def tick(self):
        """ 弾丸を移動する """
        self.count += 1
        self.theta += 100
        self.move()


class Ship(Drawable):
    """ 自機オブジェクト """

    def __init__(self):
        super(Ship, self).__init__(Rect(355, 370, 90, 60))
        self.theta = 0
        self.power = 0
        self.accel = 0
        self.explode = False
        self.image = pygame.image.load("newship.png")
        self.bang = pygame.image.load("bang.png")

    def draw(self):
        """ 自機を描画する """
        rotated = pygame.transform.rotate(self.image, self.theta)
        rect = rotated.get_rect()
        rect.center = self.rect.center
        SURFACE.blit(rotated, rect)
        if self.explode:
            SURFACE.blit(self.bang, rect)

    def tick(self):
        """ 自機を動かす """
        self.power += self.accel
        self.power *= 0.94
        self.accel *= 0.94
        self.step[0] = cos(radians(self.theta)) * self.power
        self.step[1] = sin(radians(self.theta)) * -self.power
        self.move()


def key_event_handler(keymap, ship):
    """ キーイベントを処理する """
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key not in keymap:
                keymap.append(event.key)
        elif event.type == KEYUP:
            if event.key in keymap:
                keymap.remove(event.key)

    if K_LEFT in keymap:
        ship.theta += 5
    elif K_RIGHT in keymap:
        ship.theta -= 5
    elif K_UP in keymap:
        ship.accel = min(5, ship.accel + 0.1)
    elif K_DOWN in keymap:
        ship.accel = max(-5, ship.accel - 0.1)


font = pygame.font.SysFont(None, 76)
score_font = pygame.font.SysFont(None, 44)


def draw_text(text, font, surface, x, y):
    textobj = font.render(text, 1, YELLOW)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)


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
                if event.key == pygame.K_SPACE:
                    return


# 画面を白くする
SURFACE.fill(BLACK)
# 文字を表示
draw_text("OPPOSITE PACMAN", font, SURFACE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 )
draw_text(
    "Press SPACE", font, SURFACE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100
)
pygame.display.update()
wait_for_player_to_press_key()


def main():
    """ メインルーチン """
    sysfont = pygame.font.SysFont(None, 72)
    scorefont = pygame.font.SysFont(None, 36)
    message_clear = sysfont.render("!!CLEARED!!", True, GREEN)
    message_over = sysfont.render("GAME OVER!!", True, GREEN)
    message_rect = message_clear.get_rect()
    message_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    keymap = []
    shots = []
    rocks = []
    ship = Ship()
    game_over = False
    score = 0
    back_x, back_y = 0, 0
    back_image = pygame.image.load("newbg.png")
#     back_image = pygame.transform.scale2x(back_image)

    # 隕石の数
    while len(rocks) < 8:
        pos = randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT)
        rock = Rock(pos, 64)
        if not rock.rect.colliderect(ship.rect):
            rocks.append(rock)

    # 弾丸の数
    while len(shots) < 10:
        shots.append(Shot(ship.theta))

    while True:
        key_event_handler(keymap, ship)

        if not game_over:

            ship.tick()

            # 隕石を移動
            for rock in rocks:
                rock.tick()
                if rock.rect.colliderect(ship.rect):
                    ship.explode = True
                    game_over = True

            # 弾丸を移動
            fire = False
            for shot in shots:
                if shot.count < shot.max_count:
                    shot.tick()

                    # 弾丸と隕石の衝突処理
                    hit = None
                    for rock in rocks:
                        if rock.rect.colliderect(shot.rect):
                            hit = rock
                    if hit != None:
                        score += hit.rect.width * 10
                        shot.count = shot.max_count
                        rocks.remove(hit)
                        if hit.rect.width > 16:
                            rocks.append(
                                Rock(hit.rect.center, hit.rect.width / 2)
                            )
                            rocks.append(
                                Rock(hit.rect.center, hit.rect.width / 2)
                            )
                        if len(rocks) == 0:
                            game_over = True

                elif not fire and K_SPACE in keymap:
                    shot.count = 0
                    shot.rect.center = ship.rect.center
                    shot_x = shot.power * cos(radians(ship.theta))
                    shot_y = shot.power * -sin(radians(ship.theta))
                    shot.step = (shot_x, shot_y)
                    fire = True

        # 背景の描画
#         back_x = (back_x + ship.step[0] / 2) % 1600
#         back_y = (back_y + ship.step[1] / 2) % 1600
        SURFACE.fill((0, 0, 0))
        SURFACE.blit(back_image,(0, 0))
#         SURFACE.blit(back_image, (-back_x, -back_y), (0, 0, 3200, 3200))

        # 各種オブジェクトの描画
        ship.draw()
        for shot in shots:
            shot.draw()
        for rock in rocks:
            rock.draw()

        # スコアの描画
        score_str = str(score).zfill(6)
        score_image = scorefont.render(score_str, True, GREEN)
        SURFACE.blit(score_image, (SCREEN_WIDTH - 100, 10))

        # メッセージの描画
        if game_over:
            if len(rocks) == 0:
                SURFACE.blit(message_clear, message_rect.topleft)
                pygame.display.update()
                wait_for_player_to_press_key()
                main()
            else:
                SURFACE.blit(message_over, message_rect.topleft)
                pygame.display.update()
                wait_for_player_to_press_key()
                main()

        pygame.display.update()
        FPSCLOCK.tick(20)


if __name__ == "__main__":
    main()
