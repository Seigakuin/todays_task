import pygame
import random
import sys


def check_events(items, speed):
    # pygame全てのeventを読み取る
    for event in pygame.event.get():
        # eventがQUIT(画面を閉じる)だった場合は終了判定
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, items, speed)


def check_keydown_events(event, items, speed):
    if event.key == pygame.K_RIGHT:
        for item in items:
            item.go_right(speed)
    elif event.key == pygame.K_LEFT:
        for item in items:
            item.go_left(speed)
    elif event.key == pygame.K_UP:
        for item in items:
            item.go_up(speed)
    elif event.key == pygame.K_DOWN:
        for item in items:
            item.go_down(speed)
