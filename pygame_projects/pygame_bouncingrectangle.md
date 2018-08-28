# :computer: SEIG PROGRAMMING CLUB :computer:
## BOUNCING RECTANGLE
### 目標：
* pygame の基本を理解
* 変数の理解（色の変数）
* フレームの理解　`pygame.time.Clock()
* メインループの理解 `while done is False: `
* イベントの理解 `for event in pygame.event.get():`

```python
import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Starting position of the rectangle
rect_x = 50
rect_y = 50

# Speed and direction of rectangle
rect_change_x = 5
rect_change_y = 5

# -------- Main Program Loop -----------
while done is False:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Set the screen background
    screen.fill(BLACK)

    # Draw the rectangle
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])

    # Move the rectangle starting point
    rect_x += rect_change_x
    rect_y += rect_change_y

    # Bounce the rectangle if needed
    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 650 or rect_x < 0:
        rect_change_x = rect_change_x * -1

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
```



## :sparkles: チャレンジ :sparkles: 
1. 上ボタンを押すとスピードが上がるようにしよう。
    * ブロックが進んでいる方向に合わせてスピードを上げないと、イメージ通りに進みません
    * ヒント：https://www.programcreek.com/python/example/6891/pygame.KEYUP
2. 複数の自由に動き回るブロックを作ろう
    * 初期設定を変えないと（ランダマイズ）全く同じ動きをしてしまいます。
