# 入力された正の整数値を半径とする円の面積を求めるプログラム
r = -1 # 変数の初期化
while r < 0:
    r = input("半径を入力して下さい。：")
    r = int(r)
s = r * r * 3.14 # 面積の計算
print("半径{}の円の面積は{}です。".format(r, s))