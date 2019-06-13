import matplotlib.pyplot as plt
import numpy as np
from math import sqrt


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


def interval(p, n):
    z = 1.65  # 90% Доверительный интервал
    le = z * sqrt((p * (1 - p)) / n)
    return [max((p - le), 0) * 100, min((p + le), 1) * 100]


B1 = []
n = 6  # Количество лет для периода
for i in [1981, 1982, 1983, 1984, 1985, 1986]:
    lot = open('{id}.csv'.format(id=i))
    B1.append(pos(lot))

C1 = [0] * 36
for i in range(36):
    C1[i] = (B1[0][i] + B1[1][i] + B1[2][i] + B1[3][i] + B1[4][i] + B1[5][i]) / n
print('Выборочное среднее 1 периода')
print(C1)  # Выборочное среднее 1 периода

B2 = []
for i in [1987, 1988, 1989, 1990, 1991, 1992]:
    lot = open('{id}.csv'.format(id=i))
    B2.append(pos(lot))

C2 = [0] * 36
for i in range(36):
    C2[i] = (B2[0][i] + B2[1][i] + B2[2][i] + B2[3][i] + B2[4][i] + B2[5][i]) / n
print('Выборочное среднее 2 периода')
print(C2)  # Выборочное среднее 2 периода


S = [[], [], [], [], [], [], [], [], [], [], [], []]  # Выигрышные номера по годам и тиражам
for i in [1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992]:
    A = list(open('{id}.csv'.format(id=i)))
    A.pop(0)
    A.pop(0)  # Удаляем первые две строки
    for s in A:
        s = s[:-1]  # Удаляем \n
        s = s.split(';')
        s = s[1:6]
        for k in range(5):
            S[i - 1981].append(int(s[k]))
NN = [[], [], [], [], [], [], [], [], [], [], [], []]  # Сколько раз число встречалось по годам
for i in range(12):
    for j in range(36):
        NN[i].append(S[i].count(j + 1))
SNN = [0] * 36  # Сколько раз число встретилось за все годы
for i in range(12):
    for j in range(36):
        SNN[j] += NN[i][j]

F = [[0] * 36, [0] * 36, [0] * 36, [0] * 36, [0] * 36, [0] * 36,
     [0] * 36, [0] * 36, [0] * 36, [0] * 36, [0] * 36, [0] * 36]  # Интервалы в очередности год, число
for i in [1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992]:
    B = pos(open('{id}.csv'.format(id=i)))
    for j in range(36):
        F[i - 1981][j] = interval(B[j] / 100, NN[i - 1981][j])

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

V = [0] * 36
for i in range(36):
    V[i] = interval(C[i] / 100, SNN[i])
V1 = [0] * 36
for i in range(36):
    V1[i] = V[i][1]
V2 = [0] * 36
for i in range(36):
    V2[i] = V[i][0]
print(V[0], V1[0], V2[0], C[0])
D = [0] * 36
for i in range(36):
    D[i] = ((C1[i] - C[i]) ** 2 + (C2[i] - C[i]) ** 2) ** (1 / 2) / 2
print('Выборочное стандартное отклонение')
print(D)  # Выборочное стандартное отклонение

R = [0] * 36  # Максимальное расхождение вероятностей по годам
M = [100] * 36
for i in range(36):
    for j in range(12):
        R[i] = max(R[i], B[j][i])
        M[i] = min(M[i], B[j][i])
N = [0] * 36
for i in range(36):
    N[i] = R[i] - M[i]

E = []  # Список из 36 чисел
for i in range(1, 37):
    E.append(i)

Y = [0] * 36
for i in range(36):
    Y[i] = [N[i], i + 1]
Y.sort()  #Ранжированный список чисел и их расхождений (средних)

Z = [0] * 36  # Список ранжированных по величине расхождения чисел
for i in range(36):
    Z[i] = str(Y[i][1])
print('Список чисел по возрастанию расхождения')
print(Z)

Q = [0] * 36  # Список ранжированных расхождений
for i in range(36):
    Q[i] = Y[i][0]
print('Числа, отсортированые по величине отхождения')
print(Q)

EE = [0] * 36
for i in range(36):
    EE[i] = str(i + 1)

VV = [0] * 36
for i in range(36):
    VV[i] = V1[i] - V2[i]

plt.subplots(1, 1, figsize=(10, 5))
plt.bar(EE, height=VV, bottom=V2, edgecolor='black', color='blue', alpha=0.65)
plt.scatter(EE, C, c='black', s=30, alpha=1)
plt.axis([-1, 36, 0, 6])
plt.title("Средние выборочные за 12 лет и 90%-ные доверительные интервалы")
plt.xlabel('Номер')
plt.ylabel('Вероятность (%)')
plt.show()

plt.subplots(1, 1, figsize=(10, 5))
plt.scatter(EE, C1, c='blue', s=30, alpha=0.9, label='1 период')
plt.scatter(EE, C2, c='green', s=30, alpha=0.9, label='2 период')
plt.legend()
plt.axis([-1, 36, 0, 5])
plt.title("Средние выборочные 1 и 2 периодов")
plt.xlabel('Номер')
plt.ylabel('Вероятность (%)')
plt.show()

plt.subplots(1, 1, figsize=(10, 5))
plt.bar(Z, Q)
plt.title("Максимальное расхождение выборочных значений за 2 периода")
plt.xlabel('Номер')
plt.ylabel('Величина расхождения')
plt.show()

years = ['1981', '1982', '1983', '1984', '1985',
     '1986', '1987', '1988', '1989', '1990',
     '1991', '1992']

top_numbers = [Z[0], Z[1], Z[2], Z[-3], Z[-2], Z[-1]]  # Топ-3 устойчивых и неустойчивых номеров
for number in top_numbers:
    Ta = [0]*6
    for i in range(6):
        Ta[i] = B1[i][int(number) - 1]
    Tb = [0]*6
    for i in range(6):
        Tb[i] = B2[i][int(number) - 1]
    T = Ta + Tb
    plt.subplots(1, 1, figsize=(10, 5))
    plt.scatter(years, T, c='black', s=30, alpha=1)
    H = [0] * 12
    T = [0] * 12
    for year in years:
        H[int(year) - 1981] = F[int(year) - 1981][int(number) - 1][1]
        T[int(year) - 1981] = F[int(year) - 1981][int(number) - 1][0]
    plt.bar(years, height=H, bottom=T, edgecolor='black', color='blue', alpha=0.65)
    plt.axis([-0.5, 11.5, 0, 20])
    plt.legend(handles=[plt.axhline(y=C[int(number) - 1],
                                    color='k', linestyle='-',
                                    label='Среднее выборочное значение')],
               loc=1)
    plt.title('Выборочные вероятности и доверительные интервалы числа %i' % int(number))
    plt.xlabel('Год')
    plt.ylabel('Вероятность (%)')
    plt.text(-0.25, 18.75, 'Уровень доверия = 90%')
    plt.show()
