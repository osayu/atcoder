size = int(input())
nums = list(map(int, input().split()))

# size = 10
# nums = list(map(int, "3 1 4 1 5 9 2 6 5 3".split()))

fnums = nums[1:size - 1]
rnums = list(reversed(fnums))

tmp = nums[1: size - 1]
tmp.sort()
tmps = len(tmp)

idxs = []
for num in tmp:
  fix = fnums.index(num)
  lix = rnums.index(num)
  if fix <= lix:
    # print("fix")
    # print("{} {}".format(tmps, fix))
    idxs.append(fix)
    fnums[fix] = -1
    rnums[tmps - fix - 1] = -1

  else:
    # aaaa
    # print("lix")
    idxs.append(tmps - lix - 1)
    fnums[tmps - lix - 1] = -1
    rnums[lix] = -1

  # print(fnums)
  # print(rnums)

first = 0
# print(idxs)
for i in range(0, len(idxs)):
  idx = idxs[i]
  # print("{} {}".format(idx, nums))
  n = nums.pop(idx + 1)
  nums[idx] += n
  nums[idx + 1] += n
  for j in range(0, len(idxs)):
    idxs[j] -= 1 if idxs[j] > idx else 0

print(sum(nums))

# 5 2 4 1 6 9
# 5 2 5 7 9
# 7 7 7 9
# 14 14 9
# 28 23
# 51
