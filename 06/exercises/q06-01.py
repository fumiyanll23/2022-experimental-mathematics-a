# レポート問題01
# 異なる３つの数値を⼊⼒し、それらの平均値を出⼒するプログラム
# ただし、自作関数を用いよ
# 異なる３つの数値を⼊⼒し、それらの平均値を出⼒する関数
def my_average(a, b, c):
    return (a + b + c) / 3

a = float(input("1つ目の数値aを入力してください："))
b = float(input("aとは異なる、2つ目の数値bを入力してください："))
c = float(input("aともbとも異なる、3つ目の数値cを入力してください："))
print(f"{a}, {b}, {c} の平均値は {my_average(a, b, c)} です")


# (発展) n個の数値を入力してそれらの平均値を出力するプログラム
# def my_advanced_average(args: list):
#     return sum(args) / len(args)

# 標準入力から受け取った数値を空白区切りでlistに格納する
# xs = [*map(float, input("好きなだけ数値を空白区切りで入力してください：").split())]
# print(*xs)
# print(f"の平均値は {my_advanced_average(xs)} です")
