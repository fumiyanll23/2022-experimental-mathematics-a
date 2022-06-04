# 整数剰余を関数を定義して求めるプログラム
NUMBER = 5
def modulo(x):
    return (x * x % NUMBER)
a = input("整数を入力して下さい。：")
a = int(a)
print("その数の2乗を{}で割った余りは{}です。".format(NUMBER, modulo(a)))
