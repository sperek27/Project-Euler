import collections

compare = lambda x, y: collections.Counter(x) == collections.Counter(y)

i = 1
while True:
  for j in range(2,7):
    if not compare(str(i),str(j*i)):
      break
  else:
    print(i)
  i += 1
