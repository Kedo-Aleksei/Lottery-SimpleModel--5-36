import itertools
import csv

N = int(input())
n = int(input())
A = list(range(N + 1))
del(A[0])
combinations = itertools.combinations(A, n)

filename = "combinations.csv"

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(combinations)

with open(r"C:\Users\admino\PycharmProjects\untitled1\1981.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    reader = list(reader)
    del(reader[0])
    del(reader[0])
    for row in reader:
        print(row)