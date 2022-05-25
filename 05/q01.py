# レポート問題01
# 2の1乗から10乗までの計算結果を表⽰するプログラム
# ただし、累乗は演算子 "**" を用いずにfor文を用いて計算せよ
a = 2
ans = 1
for i in range(1, 11):
    ans *= a
    print(f"{a} の {i} 乗は {ans} です")


# while文を用いると...
# a = 2
# ans = 1
# loop = 10
# while loop > 0:
#     ans *= a
#     print(f"{a} の {11 - loop} 乗は {ans} です")
#     loop -= 1
