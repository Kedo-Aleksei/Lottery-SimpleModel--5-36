import csv

A = list(open('ulam_matrix.csv'))

mat = [[0] * len(A) for i in range(len(A))]
st, m = 1, 0
# Заранее присваиваю значение центральному элементу
# матрицы
mat[len(A) // 2][len(A) // 2] = A[len(A)]

for v in range(len(A) // 2):
    # Заполнение верхней горизонтальной матрицы
    for i in range(len(A) - m):
        mat[v][i + v] = A[st]
        st += 1
        # i+=1
    # Заполнение правой вертикальной матрицы
    for i in range(v + 1, len(A) - v):
        mat[i][-v - 1] = A[st]
        st += 1
        # i+=1
    # Заполнение нижней горизонтальной матрицы
    for i in range(v + 1, len(A) - v):
        mat[-v - 1][-i - 1] = A[st]
        st += 1
        # i+=1
    # Заполнение левой вертикальной матрицы
    for i in range(v + 1, len(A) - (v + 1)):
        mat[-i - 1][v] = A[st]
        st += 1
        # i+=1
    # v+=1
    m += 2
# Вывод результата на экран
for i in mat:
    print(*i)