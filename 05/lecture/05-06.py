# 入力された10個の整数値の和を求めるプログラム
x = [0] * 10 # xの初期化
sum = 0
print("好きな10個の整数を入力して下さい。： ", end = "")
for i in range(10):
    x[i] = input("")
    x[i] = int(x[i])
for j in range(10):
    sum += x[j]
print("10個の和は{}です。".format(sum))
