import csv
import numpy as np

A = list(open('ulam_matrix.csv'))
A = A[0]
A = A.split(',')
A = list(map(int, A))

B = np.array([A]).reshape(-1, 616)
with open("matrix.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(B)

# def slice_list(input):
#     input_size = int(len(A))
#     slice_size = int(input_size / 616)
#     remain = input_size % 616
#     result = []
#     iterator = iter(input)
#     for i in range(616):
#         result.append([])
#         for j in range(slice_size):
#             result[i].append(iterator.next())
#             if remain:
#             result[i].append(iterator.next())
#     remain -= 1
#     return result
#     print(result)

# input = A
# print(slice_list(A))

# mat = [[0] * len(A) for i in range(len(A))]
# st, m = 1, 0
# # Заранее присваиваю значение центральному элементу
# # матрицы
# mat[len(A) // 2][len(A) // 2] = A[len(A)]
#
# for v in range(len(A) // 2):
#     # Заполнение верхней горизонтальной матрицы
#     for i in range(len(A) - m):
#         mat[v][i + v] = A[st]
#         st += 1
#         # i+=1
#     # Заполнение правой вертикальной матрицы
#     for i in range(v + 1, len(A) - v):
#         mat[i][-v - 1] = A[st]
#         st += 1
#         # i+=1
#     # Заполнение нижней горизонтальной матрицы
#     for i in range(v + 1, len(A) - v):
#         mat[-v - 1][-i - 1] = A[st]
#         st += 1
#         # i+=1
#     # Заполнение левой вертикальной матрицы
#     for i in range(v + 1, len(A) - (v + 1)):
#         mat[-i - 1][v] = A[st]
#         st += 1
#         # i+=1
#     # v+=1
#     m += 2
# # Вывод результата на экран
# for i in mat:
#     print(*i)
