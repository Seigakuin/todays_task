# Level 5

player_position = 1
computer_position = 1


def banmen():
    print("SUGOROKU!!")
    print("-" * (player_position - 1) + "😀" + "-" * (30 - player_position))
    print("-" * (computer_position - 1) + "😈" + "-" * (30 - computer_position))


while True:
    banmen()
    input("Press Enter!!!!")
    player_position = player_position + 1
    computer_position = computer_position + 1

