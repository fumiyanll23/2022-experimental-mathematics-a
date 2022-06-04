# 入力された5個の整数値をリストを用いて表示するプログラム
seiseki = [90, 45, 89, 75, 60]
for i in range(5):
    print("{}人目の成績{}".format(i + 1, seiseki[i]))
