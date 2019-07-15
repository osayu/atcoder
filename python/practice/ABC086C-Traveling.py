def traveling(t, x, y, tt, tx, ty):
  dx = abs(x - tx) if x > tx else abs(tx - x)
  dy = abs(y - ty) if y > ty else abs(ty - y)
  if dx + dy > tt - t:
    # 間に合わない
    return [-1, 0, 0]

  diff = (dx + dy) - (tt - t)
  if diff % 2:
    # 時間潰せない
    return [-1, 0, 0]

  return [tt, tx, ty]


poss = []
# poss.append([3, 1, 2])
# poss.append([7, 1, 1])
size = int(input())
for i in range(0, size):
  poss.append(list(map(int, input().split())))

t = 0
x = 0
y = 0
for pos in poss:
  t, x, y = traveling(t, x, y, pos[0], pos[1], pos[2])
  if t < 0:
    print("No")
    quit()

print("Yes")