# レポート問題01
# xとyに適当な整数を代入し、大きい方の数を小さい方の数で割ったときの、商と余りを表示するプログラム
print("整数x: ")
x = int(input())
print("整数y: ")
y = int(input())
if x < y:
    x, y = y, x
q = x // y
r = x % y
print(f"{x} を {y} で割ったときの商は {q} で余りは {r} です")
