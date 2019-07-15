a = int(input())
mochi = []
while len(mochi) < a:
  mochi.append(int(input()))

print(len(set(mochi)))