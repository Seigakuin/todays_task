from initialize import *
from classes import Circle, Rectangle
from utils import *

circle = Circle(WHITE, radius=150)
rectangle = Rectangle(WHITE, width=150, height=150)
circle.rect.x = random.randrange(screen_rect.width)
circle.rect.y = random.randrange(screen_rect.height)

rectangle.rect.y = random.randrange(screen_rect.height)


# ----- MAIN LOOP -----
def main():
    while True:
        check_events(items=[circle, rectangle], speed=5)

        # 画面を白く塗
        screen.fill(BLACK)

        # --- UPDATE ---
        circle.update()
        rectangle.update()

        circle.check_edges(screen_rect)
        rectangle.check_edges(screen_rect)

        # --- DRAW ---
        circle.draw(screen)
        rectangle.draw(screen)

        # pygame 全体の画面を描く
        pygame.display.flip()
        # クロッククラスのtick functionを呼び出し、60ミリ秒ループを止める
        clock.tick(120)

    # 念の為のpygame終了


if __name__ == '__main__':
    main()

sys.exit()
