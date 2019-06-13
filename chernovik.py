from math import sqrt


def interval(p, n):
    z = 1.65  # 90% Доверительный интервал
    le = z * sqrt(p * (1 - p) / n)
    return max(p - le, 0), p + le


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


F = [[0] * 36, [0] * 36, [0] * 36, [0] * 36, [0] * 36, [0] * 36,
     [0] * 36, [0] * 36, [0] * 36, [0] * 36, [0] * 36, [0] * 36]  # Интервалы в очередности год, число
S = [[], [], [], [], [], [], [], [], [], [], [], []]  # Выигрышные номера по годам и тиражам
for i in [1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992]:
    B = pos(open('{id}.csv'.format(id=i)))
    L = len(list(open('{id}.csv'.format(id=i)))) - 2
    for j in range(len(B)):
        F[i - 1981][j] = interval(B[j] / 100, L)
    A = list(open('{id}.csv'.format(id=i)))
    A.pop(0)
    A.pop(0)  # Удаляем первые две строки
    for s in A:
        s = s[:-1]  # Удаляем \n
        s = s.split(';')
        s = s[1:6]
        for k in range(5):
            S[i - 1981].append(int(s[k]))
NN = [[], [], [], [], [], [], [], [], [], [], [], []]  # Сколько раз выигрышное число встречалось по годам
for i in range(12):
    for j in range(36):
        NN[i].append(S[i].count(j + 1))
SNN = [0] * 36  # Сколько раз число встретилось за все годы
for i in range(12):
    for j in range(36):
        SNN[j] += NN[i][j]
print(SNN)
