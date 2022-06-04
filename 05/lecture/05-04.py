# 2つの整数値の和を繰り返し表示するプログラム
b = 1
for a in range(10):
    if a+b >= 5:
        break
    print("{}+{}={}".format(a, b, a+b))
