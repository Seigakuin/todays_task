import sys

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize the game engine
pygame.init()
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height), pygame.SRCALPHA)
screen.set_alpha(200)
screen_rect = screen.get_rect()
# elf.surface.blit(self.background, (0,0), None, BLEND_RGB_MAX)
# screen.fill((200, 200, 200, 255))

# フレームクラスのインスタンスを作成

clock = pygame.time.Clock()
