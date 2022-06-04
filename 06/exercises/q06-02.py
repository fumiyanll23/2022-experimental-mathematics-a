# レポート問題02
# a^2+b^2の値をprint関数を用いて出力するプログラム
# ただし、グローバル変数としてa = 5, b = 6を定義せよ
# a^2+b^2の値を返す関数
a, b = 5, 6
def my_square_sum(a, b):
    return a**2 + b**2

print(f"{a}^2+{b}^2の値は {my_square_sum(a, b)} です")
