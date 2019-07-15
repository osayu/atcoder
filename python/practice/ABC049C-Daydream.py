def daydream(s):
  rev_s = s[::-1]
  words = []
  words.append("dream"[::-1])
  words.append("dreamer"[::-1])
  words.append("erase"[::-1])
  words.append("eraser"[::-1])

  size = len(rev_s)
  n = 0
  next = True
  while n < size and next:
    next = False
    for word in words:
      # print("{} {}".format(n, n + len(word)))
      # print(rev_s[n: n + len(word)])
      if rev_s[n: n + len(word)] == word:
        n += len(word)
        next = True
        break

  # print(next, n, size)
  return next


a = input()
# a = "amdreamdreamdreamdreamdreamdreamdreamdreamdreamdream"
if daydream(a):
  print("YES")
else:
  print("NO")
