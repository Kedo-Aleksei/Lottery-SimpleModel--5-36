from itertools import cycle

n = 5

directions = ((1, 0), (0, -1), (-1, 0), (0, 1))

nums = range(1, n * n + 1)


def length_producer(_max):
    curr_l = _max
    while curr_l > 0:
        yield curr_l
        curr_l -= 1
        yield curr_l


print(list(length_producer(n)), sum(list(length_producer(n))))

buffer = []
for i in range(n):
    buffer.append([None] * n)

print(buffer)

curr_i, curr_j = -1, n - 1

values_iterator = iter(nums)

for l, d in zip(length_producer(n), cycle(directions)):
    print(l, d)
    for i in range(l):
        num = next(values_iterator)
        curr_i += d[0]
        curr_j += d[1]
        buffer[curr_i][curr_j] = num

for line in buffer:
    print(line)
