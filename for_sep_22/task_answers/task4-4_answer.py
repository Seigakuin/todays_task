# -----------------------------
# Task4-4: 「もしも」「そうでなければ」を練習しよう！
# -----------------------------
answer = 9
userinput = input("数字を当ててください")
userinput = int(userinput)


# 英語で「もしも」は if  です。
# 「そうでなければ」 は else です。
# もしanswerとuserinputが等しければ「正解」と出力しよう
# >> if ___ :  （行末の: コロンをわずれずに！）
# もしanswerとuserinputが等しくなければ「不正解」と出力しよう
# >> else:（行末の: コロンをわずれずに！）
# [[↓自分で打ってみよう↓]]
if answer == userinput:
    print("正解")
else:
    print("不正解")
