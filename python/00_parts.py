# -*- coding: utf-8 -*-
# 整数の入力
a = int(input())
# スペース区切りの整数の入力
b, c = map(int, input().split())
# 文字列の入力
s = input()

# 指定数読み込む
size = int(input())
items = []
for i in range(0, size):
  items.append(list(map(int, input().split())))

# ダミー値作るとき
items.append(list(map(int,"-2 8 9 3".split())))

# 出力
print("{} {}".format(a + b + c, s))


print (list(input()).count("1"))

for i,word in enumerate(['a','b','c']):
  print i,word

for ax in reversed(range(0, max_ax + 1)):

# 10進数 桁数
num = list(map(int, str(n)))

# list
sum([1,2,3,4])
len()
list.append(x)

# list ユニーク化
set(mochi)

import pprint

# 四則演算
べき乗
x = 1 ** 2
平方根
from math import sqrt
sqrt

# 整数判定
print(sqrt(25).is_integer())

# 多次元配列初期化
# hoge = [[0 for i in range(4004)] for j in range(4004)]


# n個からn個選ぶ
### CMB ###############################
def cmb(n, r, mod):
  if (r < 0 or r > n):
    return 0
  r = min(r, n - r)
  return g1[n] * g2[r] * g2[n - r] % mod


def cmb_init(mod):
  for i in range(2, N + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)


N = 10 ** 4
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

### CMB ###############################

