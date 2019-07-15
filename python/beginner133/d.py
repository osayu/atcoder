# size = int(input())
# items = list(map(int, input().split()))

size = 3
items = list(map(int, "1000000000 1000000000 0".split()))
# size = 3
# items = list(map(int, "2 2 4".split()))

total = sum(items)
diff = 0
y1 = total
while True:
  skip = False
  y1 -= diff
  print(y1)
  tmp = [0] * size
  res = [0] * size
  np1 = y1
  flg = False
  for i, item in enumerate(items):
    # print("y1:{} np1:{} item:{}".format(y1, np1, item))
    res[i] = np1

    if np1 != -1 and np1 // 2 > item:
      print("break")
      skip = True
      break

    tmp[i] += np1 // 2
    tmp[(i + 1) % size] += np1 // 2

    np1 = int(item - tmp[(i + 1) % size]) * 2

  print("nonb:{}")
  if tmp[0] == items[size - 1]:
    print(" ".join(map(str, res)))
    quit()
  else:
    print(tmp[0] - items[size - 1])
    diff = (tmp[0] - items[size - 1]) // 2
