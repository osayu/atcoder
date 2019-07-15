n, a, b = map(int, input().split())

num_total = 0
for x in range(1, n + 1):
  total = sum(list(map(int, str(x))))

  if a <= total <= b:
    # print(x)
    num_total += x

print(num_total)
