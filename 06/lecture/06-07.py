# 何の計算をするプログラムでしょうか？
# 解答例：斜辺2、頂角30°の直角三角形の他の2辺を求めるプログラム
import math
deg = 30
len = 2
rad = deg * math.pi / 180.0
x = len * math.cos( rad )
y = len * math.sin( rad )
print("X = {}であり、 Y = {}である。".format(x, y))
