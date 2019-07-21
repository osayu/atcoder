import io
import sys
from math import ceil


def IN_S():
  return input()


def IN_I():
  return int(input())


def IN_L_I():
  return list(map(int, input().split()))


def IN_L_S():
  return list(map(str, input().split()))


def STR_SPLIT(s, n):
  for l in range(0, len(s), n):
    yield s[0 + l:n + l]


def T_IN():
  global test_str
  sys.stdin = io.StringIO(test_str[1:-1])


test_str = '''
7
1
0
3
4
1
2
1
'''


def MAIN():
  # T_IN()
  A()


def A():
  n = IN_I()

  l = [IN_I()]

  for i in range(0, n - 1):
    num = IN_I()

    if l[0] >= num:
      l.insert(0, num)
      continue

    inl = 0
    inr = len(l) - 1
    # 1, 2, 3, 4, 5
    for j in range(0, len(l)):
      if inr == inl:
        l[inr] = num
        break

      mid = ceil((inr - inl) / 2)
      if l[mid] >= num:
        inr = mid - 1
      else:
        inl = mid
    # print(l)

  print(len(l))
  return None


def B():
  return None


def C():
  return None


MAIN()
