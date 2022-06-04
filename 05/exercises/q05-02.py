# レポート問題02
# 6の階乗の計算結果を表⽰するプログラム
x = 6
ans = 1
for i in range(1, x+1):
    ans *= i
print(f"{x} の階乗は {ans} です")


# 別解01
# x = 6
# loop = x
# ans = 1
# while loop > 0:
#     ans *= loop
#     loop -= 1
# print(f"{x} の階乗は {ans} です")


# 別解02
# from math import factorial
# x = 6
# print(f"{x} の階乗は {factorial(x)} です")
