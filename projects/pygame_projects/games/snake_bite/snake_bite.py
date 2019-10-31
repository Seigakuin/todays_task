# -*- coding: utf8 -*-
import sys
import random
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, Rect

pygame.init()

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800

SURFACE = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FPSCLOCK = pygame.time.Clock()

FOODS = []
SNAKE = []
BLOCK_SIZE = 50
BLOCK_COUNT = SCREEN_WIDTH // BLOCK_SIZE
(W, H) = (BLOCK_SIZE, BLOCK_SIZE)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SPEED = 200


def add_food():
    """ ランダムな場所に餌を配置 """
    while True:
        pos = (random.randint(0, W - 1), random.randint(0, H - 1))
        if pos in FOODS or pos in SNAKE:
            continue
        FOODS.append(pos)
        break


def move_food(pos):
    """ 餌を別の場所へ移動 """
    i = FOODS.index(pos)
    del FOODS[i]
    add_food()


def paint(message):
    """ 画面全体の描画 """
    SURFACE.fill(BLACK)
    for food in FOODS:
        pygame.draw.ellipse(
            SURFACE,
            (0, 255, 0),
            Rect(
                food[0] * BLOCK_COUNT,
                food[1] * BLOCK_COUNT,
                BLOCK_COUNT,
                BLOCK_COUNT,
            ),
        )
    for body in SNAKE:
        pygame.draw.rect(
            SURFACE,
            (0, 255, 255),
            Rect(
                body[0] * BLOCK_COUNT,
                body[1] * BLOCK_COUNT,
                BLOCK_COUNT,
                BLOCK_COUNT,
            ),
        )
    for index in range(BLOCK_SIZE):
        pygame.draw.line(
            SURFACE,
            (64, 64, 64),
            (index * BLOCK_COUNT, 0),
            (index * BLOCK_COUNT, SCREEN_HEIGHT),
        )
        pygame.draw.line(
            SURFACE,
            (64, 64, 64),
            (0, index * BLOCK_COUNT),
            (SCREEN_WIDTH, index * BLOCK_COUNT),
        )
    if message != None:
        SURFACE.blit(message, (150, SCREEN_HEIGHT // 2))
    pygame.display.update()


font = pygame.font.SysFont(None, 76)
score_font = pygame.font.SysFont(None, 44)


def draw_text(text, font, surface, x, y):
    textobj = font.render(text, 1, BLACK)
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
                return


# 画面を白くする
SURFACE.fill(WHITE)
# 文字を表示
draw_text("BLOCKS!!", font, SURFACE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
draw_text(
    "Press SPACE", font, SURFACE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50
)
pygame.display.update()
wait_for_player_to_press_key()


def main():
    """ メインルーチン """
    global SNAKE, FOODS, SPEED
    myfont = pygame.font.SysFont(None, 80)
    key = K_DOWN
    message = None
    game_over = False
    SNAKE.append((int(W / 2), int(H / 2)))
    for _ in range(10):
        add_food()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                key = event.key

        # ゲームオーバーでなかったら...
        if not game_over:
            if key == K_LEFT:
                head = (SNAKE[0][0] - 1, SNAKE[0][1])
            elif key == K_RIGHT:
                head = (SNAKE[0][0] + 1, SNAKE[0][1])
            elif key == K_UP:
                head = (SNAKE[0][0], SNAKE[0][1] - 1)
            elif key == K_DOWN:
                head = (SNAKE[0][0], SNAKE[0][1] + 1)

            if (
                head in SNAKE
                or head[0] < 0
                or head[0] >= W
                or head[1] < 0
                or head[1] >= H
            ):
                message = myfont.render("Game Over!", True, (255, 255, 0))
                game_over = True

            SNAKE.insert(0, head)
            if head in FOODS:
                move_food(head)
                SPEED += 5
            else:
                SNAKE.pop()

        paint(message)
        if game_over:
            pygame.display.update()
            wait_for_player_to_press_key()
            print("here!")
            game_over = False

            FOODS = []
            SNAKE = []

            key = K_DOWN
            message = None
            game_over = False
            SNAKE.append((int(W / 2), int(H / 2)))
            for _ in range(10):
                add_food()
        FPSCLOCK.tick(SPEED)


if __name__ == "__main__":
    main()
