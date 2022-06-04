# 入力された２つの整数値の大小関係を判定するプログラム
x = input("好きな整数を１つ入力して下さい。： ")
x = int(x)
y = input("好きな整数をもう一つ入力して下さい。： ")
y = int(y)
if(x > y):
    print("{}の方が{}よりも大きいです。".format(x, y))
elif(x < y):
    print("{}の方が{}よりも大きいです。".format(y, x))
else:
    print("２つの値は等しいです。")
