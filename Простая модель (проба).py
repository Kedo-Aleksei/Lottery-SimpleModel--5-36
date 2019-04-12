fin = open('1981.csv', encoding='utf8')
data = list(fin)
data.pop(0)
data.pop(0)  # Удаляем первые две строки
c = []
for s in data:
    s = s[:-1].replace(" ", "")  # Удаляем \n
    s = s.split(';')
    c.append(list(map(int, s)))
print(c)
