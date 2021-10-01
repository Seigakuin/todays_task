# Level 4

player_position = 10
computer_position = 15


def banmen():
    print("SUGOROKU!!")
    print("-" * (player_position - 1) + "😀" + "-" * (30 - player_position))
    print("-" * (computer_position - 1) + "😈" + "-" * (30 - computer_position))


banmen()
