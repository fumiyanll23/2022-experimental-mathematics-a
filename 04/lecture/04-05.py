# 入力された整数値が正の偶数かどうかを判定するプログラム
x = input("好きな整数を入力して下さい。： ")
x = int(x)
if(x > 0 and x%2 == 0):
    print("{}は正の数です。".format(x))
    print("{}は偶数です。".format(x))
