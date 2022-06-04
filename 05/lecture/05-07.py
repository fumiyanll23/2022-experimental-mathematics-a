# 2つの行列の和を求めるプログラム
A = [[1, 2, 3], [4, 5, 6]]
B = [[6, 3, 4], [5, 1, 2]]
C = [[0]*3 for i in range(2)]
for i in range(2):
    for j in range(3):
        C[i][j] = A[i][j] + B[i][j]
for i in range(2):
    for j in range(3):
        print("C[{}][{}]={:>3}".format(i, j, C[i][j]))
# {:>3}は出力数字の表示桁数をそろえるため
