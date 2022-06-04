# 1から入力された正の整数値までの和を求めるプログラム
sum=0
n = input("好きな正の整数を入力して下さい。： ")
n = int(n)
for i in range(1,n+1):
    sum += i
print("1から{}までの和は{}です。".format(n, sum))
