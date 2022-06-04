# 入力された2つの整数値の最大値を関数を定義して求めるプログラム
def max(x, y):
    if (x > y):
        return x
    else:
        return y
print("2つの整数を入力して下さい。")
a = input("整数A：")
a = int(a)
b = input("整数B：")
b = int(b)
ans = max(a, b);
print("最大値は{}です。".format(ans))
