import pygame


class Shape(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0

    def go_right(self, x):
        self.change_x += x

    def go_left(self, x):
        self.change_x -= x

    def go_down(self, y):
        self.change_y += y

    def go_up(self, y):
        self.change_y -= y

    # def draw(self, screen):
    #     self.screen = screen

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

    def check_edges(self, screen_rect):
        if self.rect.right > screen_rect.width and self.change_x > 0:
            self.change_x *= -1
        elif self.rect.left < 0 and self.change_x < 0:
            self.change_x *= -1
        if self.rect.bottom > screen_rect.height and self.change_y > 0:
            self.change_y *= -1
        elif self.rect.top < 0 and self.change_y < 0:
            self.change_y *= -1


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(radius * 2, radius * 2)
        self.radius = radius
        self.color = color
        pygame.draw.circle(
            self.image, color, (self.rect.centerx, self.rect.centery), self.radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(
            self.image,
            self.color,
            (self.radius, self.radius),
            self.radius
        )
        screen.blit(self.image, self.rect)


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(width, height)
        self.color = color
        pygame.draw.rect(
            self.image,
            self.color,
            self.rect
        )

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(
            self.image,
            self.color,
            self.rect
        )
        # self.rect = self.image.get_rect()
        screen.blit(self.image, self.rect)


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

    # 画面を描く前に状況を更新するfunction/method
    def update(self):
        # ブロックは1ずつ降りてくる
        self.rect.y += 1

        # もし画面外に出たらreset_pos function を呼び出す
        if self.rect.y > 410:
            self.reset_pos()


"""
class Rectangle():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
    def speed(self,*speed):
        self.speed_x = speed[0]
        self.speed_y = speed[1]
    def draw(self, screen):
        self.screen = screen
        pygame.draw.rect(self.screen, white, [self.x, self.y, self.height, self.width])
        print "meth draw: x,y", self.x, self.y
    def move(self):
        print "self.x", self.x
        print "self.speed_x:", self.speed_x
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x > 250 or self.x < 0:
            self.speed_x = -self.speed_x
        if self.y > 250 or self.y < 0:
            self.speed_y = -self.speed_y


box_surface_fill = pygame.Surface((50, 50), pygame.SRCALPHA)
            box_surface_fill.fill((255, 255, 255, i*20))

            box_surface_rect = pygame.Surface((50, 50), pygame.SRCALPHA)
            pygame.draw.rect(box_surface_rect, (255, 255, 255, i*20), (0,0, 50,50))

            box_surface_circle = pygame.Surface((50, 50), pygame.SRCALPHA)
            pygame.draw.circle(box_surface_circle, (255, 255, 255, i*20), (25,25), 10)


            box_surface_polygon = pygame.Surface((50, 50), pygame.SRCALPHA)
            pygame.draw.polygon(box_surface_polygon, (255, 255, 255, i*20), ((25,0), (0,25), (25,50), (50,25)))


"""
