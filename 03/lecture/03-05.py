# 変数に数値を代入して桁揃え表示するプログラム
num = 123
age = 20
height = 167.8
weight = 55.555
print("学籍番号：{:>4}".format(num))
print("年齢：{:>4}歳".format(age))
print("身長：{}cm".format(height))
print("体重：{:7>.1f}kg".format(weight))
