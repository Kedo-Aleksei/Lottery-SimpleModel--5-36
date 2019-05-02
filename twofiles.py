def pos(fin):
    A = list(fin)
    A.pop(0)
    A.pop(0)  # Удаляем первые две строки
    data = []
    for s in A:
        s = s[:-1].replace(" ", "")  # Удаляем \n
        s = s.split(';')
        data.append(list(map(int, s)))
    # Считаны данные
    M = [0] * 36  # Список суммы показателей
    B = [0] * 36  # Количество раз, когда выпал этот элемент
    for i in range(len(data)):
        for j in [1, 2, 3, 4, 5]:
            M[data[i][j] - 1] += data[i][7] * 10000000 / data[i][6]
            B[data[i][j] - 1] += 1
    # Исправляем список суммы показателей
    for i in range(36):
        M[i] /= B[i]
    k = 0
    K = [0] * 36  # Проценты
    for i in range(36):
        k += M[i]
    for i in range(36):
        K[i] = 100 * M[i] / k
    return K


B = []
n = 2  # Количество лет
for i in [1991, 1992]:
    lot = open('{id}.csv'.format(id=i))
    B.append(pos(lot))
print(B)

C = [0] * 36
for i in range(36):
    C[i] = (B[0][i] + B[1][i]) / n
print(C)  # Выборочное среднее
D = [0] * 36
for i in range(36):
    D[i] = ((B[0][i] - C[i])**2 + (B[1][i] - C[i])**2) / n
print(D)  # Выборочная дисперсия
