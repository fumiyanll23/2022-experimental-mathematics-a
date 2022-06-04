# 01. FizzBuzz Question
# nを入力させる
n = int(input("正整数 n を入力してください："))

# ここから下にコードを書く
# 解答例01
# for文を使う。今回のようにループ回数が明確に分かっているときにはfor文を使うことができる
for i in range(1, n+1):
    # iが15の倍数のとき
    if i % 15 == 0:
        print("FizzBuzz")
    # iが3の倍数のとき
    elif i % 3 == 0:
        print("Fizz")
    # iが5の倍数のとき
    elif i % 5 == 0:
        print("Buzz")
    # それ以外のとき
    else:
        print(i)

# 解答例02
# 「nが15の倍数である <=> nが3の倍数である、かつnが5の倍数である」を利用する
# for i in range(1, n+1):
#     answer = ""
#     if i % 3 == 0:
#         answer += "Fizz"
#     if i % 5 == 0:
#         answer += "Buzz"
#     if answer == "":
#         answer = i
#     print(answer)
