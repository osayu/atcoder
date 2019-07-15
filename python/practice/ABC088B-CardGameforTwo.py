n = int(input())
cards = list(map(int, input().split()))

cards.sort(reverse=True)
a = 0
b = 0
for i, card in enumerate(cards):
  if i % 2 == 0:
    a += card
  else:
    b += card

print(a - b)

