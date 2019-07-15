size = int(input())
nums = list(map(int, input().split()))
# 
# size = 6
# nums = [0, 2, 2, 0, 2, 2]

numu = list(set(nums))
if len(numu) == 1 and numu[0] == 0:
  print("Yes")
  quit()


if len(numu) == 2 \
    and nums.count(0) != 0 \
    and nums.count(0) * 3 == size:
  print("Yes")
  quit()

if len(numu) == 3:
  if nums.count(0) == 1:
    print("No")
    quit()

  if not nums.count(numu[0]) == nums.count(numu[1]) == nums.count(numu[2]):
    print("No")
    quit()

  if numu[0] ^ numu[2] == numu[1] \
      and numu[1] ^ numu[0] == numu[2] \
      and numu[2] ^ numu[1] == numu[0]:
    print("Yes")
    quit()

print("No")
