fin = open('1981.csv')
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
print(K)
