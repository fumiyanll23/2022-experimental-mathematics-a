# 入力された点数を並べ替えるプログラム
NUMBER = 5
ten = [0] * NUMBER
print("{}人の得点を入力して下さい。".format(NUMBER))
for i in range(NUMBER):
    ten[i] = input("")
    ten[i] = int(ten[i])
for s in range(NUMBER-1):
    for t in range(s+1, NUMBER):
        if(ten[t] > ten[s]):
            c = ten[t]
            ten[t] = ten[s]
            ten[s] = c
for j in range(NUMBER):
    print("{}位の人の点数は{}です。".format(j+1, ten[j]))
