# -----------------------------
# Task4-5: 数字当てゲームをつくろう
# -----------------------------

# [[前Taskからのコード]]
import random
answer = random.randrange(1, 11)
userinput = input("数字を当ててください")
userinput = int(userinput)


# Task4で学んだことをすべて使い、数字当てゲームをつくろう
# 予測した数字が答えの数字と同じどうかを確認
# >> if answer == userinput:
# >>    print("正解!!!!!")
# >> else:
# >>    print("不正解...")

# 不正解の場合はもう一度だけチャンスを上げましょう
# >> userinput = input("もう一回だけチャンス")
# >> userinput = int(userinput)


# [[↓自分で打ってみよう↓]]
