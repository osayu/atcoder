l, r = map(int, input().split())

# # 
# l = 2020
# r = 2040
r = min(r, l + 2019)

min = -1
for tl in range(l, r + 1):
  for tr in range(tl + 1, r + 1):
    tmp = (tl * tr) % 2019
    if min == -1 or min > tmp:
      min = tmp

print(min)