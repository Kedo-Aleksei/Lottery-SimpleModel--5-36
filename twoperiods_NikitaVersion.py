import matplotlib.pyplot as plt
import numpy as np


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

C = [0] * 36
for i in range(36):
    C[i] = (C1[i] + C2[i]) / 2
D = [0] * 36
for i in range(36):
    D[i] = ((C1[i] - C[i]) ** 2 + (C2[i] - C[i]) ** 2) ** (1 / 2) / 2
print('Выборочное стандартное отклонение')
print(D)  # Выборочное стандартное отклонение

X = [0]*36  #Расхождение для каждого числа
for i in range(36):
    X[i] = abs(C2[i] - C1[i])
print(X)

E = []  #Список из 36 чисел
for i in range(1, 37):
    E.append(i)

Y = [0]*36
for i in range(36):
    Y[i] = [X[i], E[i]]
Y.sort()  #Ранжированный список чисел и их расхождений по годам (от меньшего к большему)

Z = [0]*36  #Список ранжированных по величине расхождения чисел
for i in range(36):
    Z[i] = str(Y[i][1])
print(Z)

Q = [0]*36  #Список ранжированных расхождений
for i in range(36):
    Q[i] = Y[i][0]
print(Q)

plt.plot(E, C1, "bo", E, C2, "go")
plt.axis([0, 37, 0, 5])
plt.title("Средние выборочные 1 (син.) и 2 (зел.) периодов")
plt.xlabel('Номер')
plt.ylabel('Вероятность (%)')
plt.show()

plt.subplots(1, 1, figsize=(10, 5))
plt.bar(Z, Q)
plt.title("Расхождение средних выборочных значений по 2 периодам")
plt.xlabel('Номер')
plt.ylabel('Величина расхождения')
plt.show()

T22a = [0]*6
for i in range(6):
    T22a[i] = B1[i][21]
T22b = [0]*6
for i in range(6):
    T22b[i] = B2[i][21]
T22 = T22a + T22b

L = ['1981', '1982', '1983', '1984', '1985',
     '1986', '1987', '1988', '1989', '1990',
     '1991', '1992']

plt.subplots(1, 1, figsize=(10, 5))
plt.scatter(L, T22, c='red', s=30, alpha=0.9)
plt.axis([-1, 12, 0, 5])
plt.title("Выборочные вероятности числа 22")
plt.xlabel('Год')
plt.ylabel('Вероятность (%)')
plt.show()
