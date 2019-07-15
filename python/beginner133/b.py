from math import sqrt


def calc(pos_x, pos_y):
  sum = 0
  for i in range(0, len(pos_x)):
    sum += (pos_x[i] - pos_y[i]) ** 2

  return sqrt(sum).is_integer()


size, z = map(int, input().split())
items = []
for i in range(0, size):
  items.append(list(map(int, input().split())))

# items = []
# items.append(list(map(int, "-3 7 8 2".split())))
# items.append(list(map(int, "-12 1 10 2".split())))
# items.append(list(map(int, "-2 8 9 3".split())))

count = 0

for i in range(0, len(items)):
  for j in range(i + 1, len(items)):
    count += 1 if calc(items[i], items[j]) else 0

print(count)
