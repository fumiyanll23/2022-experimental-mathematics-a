# 02. FizzBuzz Function
# ここにmy_fizzbuzz関数を定義する
# 解答例01
def my_fizzbuzz(n):
    # iが15の倍数のとき
    if i % 15 == 0:
        return("FizzBuzz")
    # iが3の倍数のとき
    elif i % 3 == 0:
        return("Fizz")
    # iが5の倍数のとき
    elif i % 5 == 0:
        return("Buzz")
    # それ以外のとき
    else:
        return(i)

# 解答例02
# def my_fizzbuzz(n):
#     answer = ""
#     if i % 3 == 0:
#         answer += "Fizz"
#     if i % 5 == 0:
#         answer += "Buzz"
#     if answer == "":
#         answer = i
#     return answer

# ここから下は書き換えない
# nを入力させる
n = int(input('正整数 n を入力してください：'))
for i in range(1, n+1):
    print(my_fizzbuzz(i))
