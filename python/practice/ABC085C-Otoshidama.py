n, y = map(int, input().split())

diff = y - n * 1000

# diff = man * 9000 + gosen * 4000
for gosen in range(0, diff // 4000 + 1):
  tmp = gosen * 4000
  if diff - tmp < 0:
    break

  if (diff - tmp) % 9000 == 0:
    man = (diff - tmp) // 9000
    if man >= 0 and man + gosen <= n:
      print("{} {} {}".format(man, gosen, n - (man + gosen)))
      quit()

print("-1 -1 -1")

