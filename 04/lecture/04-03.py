# 与えられた条件を判定するプログラム
a, b = 10, 20
print("a > bの演算結果は {} である。".format(a > b))
print("a <= b の演算結果は {}である。".format(a <= b))
print("a == b の演算結果は {} である。".format(a == b))
print("a != b の演算結果は {} である。".format(a != b))
x = a if (0 <= a and a <= 100) else 0
print("x の値は {} である。".format(x))
