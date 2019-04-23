B = [[0] * 36, [0] * 36]
for e in range(1, 3):
    lot = open('{id}.csv'.format(id=e))
    A = list(lot)
    A.pop(0)
    A.pop(0)
    data = []
    for s in A:
        s = s[:-1].replace(" ", "")
        s = s.split(';')
        data.append(list(map(int, s)))
    M = [0] * 36
    for i in range(len(data)):
        for j in [1, 2, 3, 4, 5]:
            M[data[i][j] - 1] += data[i][7] * 10000000 / data[i][6]
    k = 0
    K = [0] * 36
    for i in range(36):
        k += M[i]
    for i in range(36):
        K[i] = M[i] * 100 / k
    for i in range(36):
        B[e-1][i] = K[i]
print(B)
