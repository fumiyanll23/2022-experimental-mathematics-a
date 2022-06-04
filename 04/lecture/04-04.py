# 四則演算の順序を把握する計算プログラム
a, b, c = 2, 8, 6
print("a×b-c÷aの演算結果は{}である。".format(a*b-c/a))
print("a×(b-c)÷aの演算結果は{}である。".format(a*(b-c)/a))
print("a-b+c の演算結果は {} である。".format(a-b+c))
print("a-(b+c)の演算結果は {} である。".format(a-(b+c)))
