# レポート問題03
# 適当な2つの4次元ベクトルを与えて、それらの内積を計算するプログラム
k = 4
print(f"{k}次元ベクトルx: ")
xs = [*map(int, input().split())]
print(f"{k}次元ベクトルy: ")
ys = [*map(int, input().split())]
# xsとysの内積を求める
ans = 0
for i in range(k):
    ans += xs[i] * ys[i]
print(f"{xs} と {ys} の内積は {ans} です")


# 別解01
# k = 4
# print(f"{k}次元ベクトルx: ")
# xs = [*map(int, input().split())]
# print(f"{k}次元ベクトルy: ")
# ys = [*map(int, input().split())]
# # xsとysの内積を求める
# ans = 0
# for x, y in zip(xs, ys):
#     ans += x * y
# print(f"{xs} と {ys} の内積は {ans} です")


# 別解02
# k = 4
# print(f"{k}次元ベクトルx: ")
# xs = [*map(int, input().split())]
# print(f"{k}次元ベクトルy: ")
# ys = [*map(int, input().split())]
# xsとysの内積を求める
# print(f"{xs} と {ys} の内積は {sum([x*y for x, y in zip(xs, ys)])} です")
