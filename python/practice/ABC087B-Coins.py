a = int(input())  # 500
b = int(input())  # 100
c = int(input())  # 50
x = int(input())

num = x // 50
count = 0
max_ax = num // 10 if num // 10 <= a else a

for ax in reversed(range(0, max_ax + 1)):
  # print("ax {}".format(ax))
  axnum = num - ax * 10

  max_bx = axnum // 2 if axnum // 2 <= b else b
  for bx in reversed(range(0, max_bx + 1)):
    # print("bx {}".format(bx))
    bxnum = axnum - bx * 2
    if bxnum <= c:
      # print("ax:{} bx:{} cx{}".format(ax, bx, bxnum))
      count += 1

print(count)
