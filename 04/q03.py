# レポート問題03
# ２つの整数x, yのうち、大きい方の値を表示するプログラム
print("整数x: ")
x = int(input())
print("整数y: ")
y = int(input())
if x < y:
    x, y = y, x
print(f"{x} と {y} のうち、大きい方の値は {x} です")


# 別解01
# print("整数x: ")
# x = int(input())
# print("整数y: ")
# y = int(input())
# print(f"{x} と {y} のうち、大きい方の値は {x if x > y else y} です")
