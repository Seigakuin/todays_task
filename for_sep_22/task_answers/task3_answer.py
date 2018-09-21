# Task3: 計算機を作ろう

# 変数 a に数字入れよう
# >> a = input("最初の数字はなんですか？")
# 変数 b に数字入れよう
# >> b = input("次の数字はなんですか？")
a = input("最初の数字はなんですか？")
b = input("次の数字はなんですか？")


# a と　b の結果を出力しよう
# >> print(a + b)
print(a + b)

# 出力結果は予想通りでしたか？

# input()から受け取る入力は数字のように見えて、実はすべて文字列str になってしまします。
# 数字として計算するためには文字列を数字に変えましょう
# >> a = int(a)
# >> b = int(b)
a = int(a)
b = int(b)

# もう一度、結果を出力しよう
# >> print(a + b)
print(a + b)


# 出力にことばをつけよう
# 注意!! 数字int と文字列strはそのままでは繋げられない
# つなげるためには数字int を文字列str に変換する必要がある
# そこで数字を文字列に変換する str() を使う
# >> print("足し算の結果は" + str(a + b) + "です。")
print("足し算の結果は" + str(a + b) + "です。")