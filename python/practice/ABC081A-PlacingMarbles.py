# from pprint import pprint
size = int(input())
nums = list(map(int, input().split()))

# size = 3
# nums = [10, 20, 30]
# print(size)
# pprint(nums)

flag = True
res = 0
while flag:
  for i, num in enumerate(nums):
    if num % 2 == 1:
      flag = False
      break
    else:
      nums[i] /= 2
  if flag:
    res += 1

print(res)
