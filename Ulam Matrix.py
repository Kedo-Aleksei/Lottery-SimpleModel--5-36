import csv

A = list(open("combinations.csv"))
comb = []
for s in A:
    s = s[:-1]  # Удаляем \n
    s = s.split(',')
    comb.append(list(map(int, s)))

data = []
for i in [1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992]:
    lot = list(open('{id}.csv'.format(id=i)))
    lot.pop(0)
    lot.pop(0)
    for s in lot:
        s = s[:-1].replace(" ", "")  # Удаляем \n
        s = s.split(';')
        s = s[1:6]
        data.append(list(map(int, s)))

ulam = [0] * len(comb)
for i in range(len(comb)):
    for j in range(len(data)):
        if comb[i] == data[j]:
            ulam[i] = 1

with open("ulam_matrix.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(ulam)
