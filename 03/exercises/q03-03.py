# レポート問題03
# aの値をbに、bの値をaに入れ替えて表示するプログラム
# ただし、int型の変数a, bにそれぞれ数値13, 17を代入する
a = 13
b = 17
a, b = b, a
print(f"a = {a}, b = {b}")
