# 消費税を関数を定義して求めるプログラム
tax = 0.10
def taxfunc(x):
    return (x + x*tax)
a = input("金額を入力して下さい。： ")
a = int(a)
print("消費税率は{:.0%}なので、税込み{}円です。".format(tax, taxfunc(a)))
