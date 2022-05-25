# レポート問題04
# 適当な2つの3次正⽅⾏列を与えて、それらの和を表⽰するプログラム
n = 3
print(f"{n}次正⽅⾏列X: ")
xss = [[*map(int, input(f"第{i+1}行: ").split())] for i in range(n)]
print(f"{n}次正⽅⾏列Y: ")
yss = [[*map(int, input(f"第{i+1}行: ").split())] for i in range(n)]
# 行列の和を求める
ans = [[0]*3 for _ in range(n)]
for i in range(n):
    for j in range(n):
        ans[i][j] = xss[i][j] + yss[i][j]
print(f"{xss} と {yss} の和は {ans} です")


# 別解01
# n = 3
# print(f"{n}次正⽅⾏列X: ")
# xss = [[*map(int, input(f"第{i+1}行: ").split())] for i in range(n)]
# print(f"{n}次正⽅⾏列Y: ")
# yss = [[*map(int, input(f"第{i+1}行: ").split())] for i in range(n)]
# 行列の和を求める
# ans = [[0]*3 for _ in range(n)]
# for i, (xs, ys) in enumerate(zip(xss, yss)):
#     for j, (x, y) in enumerate(zip(xs, ys)):
#         ans[i][j] += x + y
# print(f"{xss} と {yss} の和は {ans} です")


# 別解02
# n = 3
# print(f"{n}次正⽅⾏列X: ")
# xss = [[*map(int, input(f"第{i+1}行: ").split())] for i in range(n)]
# print(f"{n}次正⽅⾏列Y: ")
# yss = [[*map(int, input(f"第{i+1}行: ").split())] for i in range(n)]
# 行列の和を求める
# print(f"{xss} と {yss} の和は {[[x+y for x, y in zip(xs, ys)] for xs, ys in zip(xss, yss)]} です")
