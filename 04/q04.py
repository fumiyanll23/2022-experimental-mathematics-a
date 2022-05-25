# レポート問題04
# 入力された正の整数値が3の倍数がそうでないかを判定するプログラム
print("正整数n: ")
n = int(input())
if n % 3 == 0:
    print(f"{n} は3の倍数です")
else:
    print(f"{n} は3の倍数ではありません")


# 別解01
# print("正整数n: ")
# n = int(input())
# print(f"{n} は3の倍数" + ("です" if n % 3 == 0 else f"ではありません"))
