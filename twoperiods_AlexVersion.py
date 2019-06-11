import matplotlib.pyplot as plt
import numpy as np

def LenPos(p, n):
    z = 1.65
    l = z * sqrt(p * (1 - p) / n)
    return p - l, p + l

def pos(fin):
    '''Returns list K which contains probabilities of 36 numbers.'''
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
n = 12  # Количество лет для периода
for i in [1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992]:
    lot = open('{id}.csv'.format(id=i))
    B.append(pos(lot))

C = [0] * 36
for i in range(36):
    C[i] = (B[0][i] + B[1][i] + B[2][i] + B[3][i] + B[4][i] + B[5][i] +
            B[6][i] + B[7][i] + B[8][i] + B[9][i] + B[10][i] + B[11][i]) / n
print('Выборочное среднее')
print(C)  # Выборочное среднее

N = [0] * 36  # Максимальное расхождение вероятностей по годам
M = [100] * 36  # Минимальное расхождение вероятностей по годам
for i in range(36):
    for j in range(12):
        N[i] = max(N[i], B[j][i])
        M[i] = min(M[i], B[j][i])

R = [0] * 36
for i in range(36):
    R[i] = N[i] - M[i]
print(R)
I = np.argsort(R)  # Индексы отсортированного списка
print(I)
R.sort()
print(R)


# B1 = []
# n = 6  # Количество лет для периода
# for i in [1981, 1982, 1983, 1984, 1985, 1986]:
#     lot = open('{id}.csv'.format(id=i))
#     B1.append(pos(lot))
#
# C1 = [0] * 36
# for i in range(36):
#     C1[i] = (B1[0][i] + B1[1][i] + B1[2][i] + B1[3][i] + B1[4][i] + B1[5][i]) / n
# print('Выборочное среднее 1 периода')
# print(C1)  # Выборочное среднее 1 периода
#
# B2 = []
# for i in [1987, 1988, 1989, 1990, 1991, 1992]:
#     lot = open('{id}.csv'.format(id=i))
#     B2.append(pos(lot))
#
# C2 = [0] * 36
# for i in range(36):
#     C2[i] = (B2[0][i] + B2[1][i] + B2[2][i] + B2[3][i] + B2[4][i] + B2[5][i]) / n
# print('Выборочное среднее 2 периода')
# print(C2)  # Выборочное среднее 2 периода
#
# x = 0  # Максимальное расхождение средних (после уберем, если не нужно)
# for i in range(36):
#     x = max(x, abs(C1[i] - C2[i]))
# print('Максимальное расхождение средних')
# print(x)
#
# C = [0] * 36
# for i in range(36):
#     C[i] = (C1[i] + C2[i]) / 2
# D = [0] * 36
# for i in range(36):
#     D[i] = ((C1[i] - C[i]) ** 2 + (C2[i] - C[i]) ** 2) ** (1 / 2) / 2
# print('Выборочное стандартное отклонение')
# print(D)  # Выборочное стандартное отклонение
#
# x = 0  # Максимальное из стандартных отклонений (после уберем, если не нужно)
# for i in range(36):
#     x = max(x, D[i])
# print('Максимальное из стандартных отклонений')
# print(x)
#
# plt.plot(list(range(1, 37)), C1, "bo", list(range(1, 37)), C2, "go")
# plt.title("Средние выборочные 1 (син.) и 2 (зел.) периодов")
# plt.xlabel('Номер')
# plt.ylabel('Вероятность (%)')
# plt.show()
