import itertools
import csv

N = 36
n = 5
A = list(range(1, N + 1))

combinations = itertools.combinations(A, n)

with open("combinations.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(combinations)
