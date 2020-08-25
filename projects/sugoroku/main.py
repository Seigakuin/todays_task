# MAIN
import random

player_position = 1
computer_position = 1


def roll_dice():
    step = random.randint(1, 6)
    return step


def banmen():
    global player_position, computer_position
    print("SUGOROKU!!")
    if player_position < 30:
        print("-" * (player_position - 1) + "😀" + "-" * (30 - player_position))
    else:
        print("-" * 29 + "😀")

    if computer_position < 30:
        print(
            "-" * (computer_position - 1)
            + "😈"
            + "-" * (30 - computer_position)
        )
    else:
        print("-" * 29 + "😈")


while True:
    banmen()
    input("Press Enter!!!!")
    if player_position >= 29:
        print("Player Wins...")
        break

    if computer_position >= 29:
        print("Computer Wins...")
        break
    player_position = player_position + roll_dice()
    computer_position = computer_position + roll_dice()


"""
import random

player_position = 1
computer_position = 1


def roll_dice():
    step = random.randint(1, 6)
    return step


def banmen():
    print("SUGOROKU!!")
    print("-" * (player_position - 1) + "😀" + "-" * (30 - player_position))
    print("-" * (computer_position - 1) + "😈" + "-" * (30 - computer_position))


while True:

    banmen()
    input("Press Enter!!!!")
    computer_position = computer_position + roll_dice()
    player_position = player_position + roll_dice()


import os

player_position = 1
computer_position = 1


def banmen():
    print("-" * (player_position - 1) + "😀" + "-" * (30 - player_position))
    print("-" * (computer_position - 1) + "😈" + "-" * (30 - computer_position))


while True:
    os.system("cls||clear")
    banmen()
    input("Press Enter!!!")
    player_position = player_position + 2
    computer_position = computer_position + 1
"""
