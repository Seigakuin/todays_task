import sys
from random import randint
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE

pygame.init()
pygame.key.set_repeat(5, 5)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SURFACE = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),pygame.FULLSCREEN)
FPSCLOCK = pygame.time.Clock()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (47, 79, 79)

HOLE_WIDTH = 40
HOLE_HEIGHT = 400
SLOPE_RAND_MAX = 30
SLOPE_RAND_MIN = 20

SHIP_START_Y = SCREEN_HEIGHT // 2 - 80

font = pygame.font.SysFont(None, 76)
score_font = pygame.font.SysFont(None, 44)

bg = pygame.image.load("background.png")


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
draw_text("CAVE type1!!", font, SURFACE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
draw_text(
    "Plase press SPACE key to continue",
    font,
    SURFACE,
    SCREEN_WIDTH // 2,
    SCREEN_HEIGHT // 2 + 50,
)
pygame.display.update()
wait_for_player_to_press_key()


def main():
    """ メインルーチン """
    walls = 100
    ship_y = SHIP_START_Y
    velocity = 0
    score = 0
    slope = randint(SLOPE_RAND_MIN, SLOPE_RAND_MAX)
    sysfont = pygame.font.SysFont(None, 36)
    ship_image = pygame.image.load("ship.png")
    bang_image = pygame.image.load("bang.png")
    holes = []
    for xpos in range(walls):
        holes.append(Rect(xpos * 10, 100, HOLE_WIDTH, HOLE_HEIGHT))
    game_over = False

    while True:
        SURFACE.blit(bg, bg.get_rect())
        is_space_down = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    is_space_down = True

        # 自機を移動
        if not game_over:
            score += 10
            velocity += -3 if is_space_down else 3
            ship_y += velocity

            # 洞窟をスクロール

            # hole 最後の帯をedgeに
            edge = holes[-1].copy()
            # slope分、動かす
            test = edge.move(0, slope)
            # 帯が動いたとしたら、壁に当たるのかを確認
            if test.top <= 10 or test.bottom >= SCREEN_HEIGHT:
                slope = randint(SLOPE_RAND_MIN, SLOPE_RAND_MAX) * (
                    -1 if slope > 0 else 1
                )
                edge.inflate_ip(0, -20) # make hole smaller
            edge.move_ip(HOLE_WIDTH, slope) # move hole
            holes.append(edge) # add hole to holes
            del holes[0] # delete first hole
            holes = [x.move(-HOLE_WIDTH, 0) for x in holes]



            # 衝突 ?

            upper_limit = 63
            lower_limit = 88 # default 80
            if1 = holes[0].top > ship_y - upper_limit or holes[0].bottom < ship_y + lower_limit
            if2 = holes[1].top > ship_y - upper_limit or holes[1].bottom < ship_y + lower_limit
            if3 = holes[2].top > ship_y - upper_limit or holes[2].bottom < ship_y + lower_limit

            if if1 or if2 or if3:
                game_over = True

        # 描画
        SURFACE.fill(GREEN)  # GREEN
        # SURFACE.blit(bg, bg.get_rect())

        # Draw black Holes
        for hole in holes:

            pygame.draw.rect(SURFACE, BLACK, hole)

        # Draw Ship
        SURFACE.blit(ship_image, (0, ship_y))

        # Draw score
        score_image = sysfont.render("score is {}".format(score), True, (0, 153, 153))
        SURFACE.blit(score_image, (SCREEN_WIDTH - 200, 20))

        # If Game Over...
        if game_over:
            score = 0
            # Draw Game over Image
            SURFACE.blit(bang_image, (0, ship_y - 40))

            pygame.display.update()
            # Wait for player to press any key
            wait_for_player_to_press_key()

            game_over = True  # switch Game Over to True
            ship_y = SHIP_START_Y

            holes = []
            for xpos in range(walls):
                # 縦帯を作成
                holes.append(Rect(xpos * 10, 100, HOLE_WIDTH, HOLE_HEIGHT))
            game_over = False
            # 描画
            SURFACE.fill(GREEN)

            for hole in holes:
                pygame.draw.rect(SURFACE, BLACK, hole)
            SURFACE.blit(ship_image, (0, ship_y))
            score_image = sysfont.render(
                "score : {}".format(score), True, (0, 153, 153)
            )
            SURFACE.blit(score_image, (SCREEN_HEIGHT, 20))

            score += 10
            velocity += -3 if is_space_down else 3
            ship_y += velocity

            # 洞窟をスクロール
            edge = holes[-1].copy()  # holesの最後の黒い縦帯をedgeに読み込む
            test = edge.move(0, slope)  # その縦帯を次の動き分動かしてみる
            # もし動かした分が画面の上か下に触れていたら...
            if test.top <= 0 or test.bottom >= SCREEN_HEIGHT:
                # 縦の逆方向に付け足し始める
                slope = randint(SLOPE_RAND_MIN, SLOPE_RAND_MAX) * (
                    -1 if slope > 0 else 1
                )
                # 縦帯を立てに狭める: 難易度を決める
                edge.inflate_ip(0, -20)

            edge.move_ip(HOLE_WIDTH, slope)  # 縦帯を右に動かす
            holes.append(edge)  # 動かした縦帯を
            del holes[0]
            holes = [x.move(-HOLE_WIDTH, 0) for x in holes]

        pygame.display.update()
        FPSCLOCK.tick(15)


if __name__ == "__main__":
    main()
