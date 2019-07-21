import io
import sys
from fractions import gcd


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
314159265358979323 846264338327950288 419716939 937510582
'''


def MAIN():
  # T_IN()
  A()


def A():
  a, b, c, d = IN_L_I()

  divc = (b // c) - ((a - 1) // c)
  divd = (b // d) - ((a - 1) // d)
  cd = c * d // gcd(c, d)
  divcd = (b // cd) - ((a - 1) // cd)


  total = (b + 1 - a) - divc - divd + divcd

  print(total)
  return None
 

def B():
  return None


def C():
  return None


MAIN()
