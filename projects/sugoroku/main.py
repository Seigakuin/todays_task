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
