from itertools import permutations

l = list(permutations(range(0, 10)))
s = 0
for j in l:
  i = ""
  for L in j:
    i += str(L)
  if int(i[7:10])%17 == 0 and int(i[6:9])%13 == 0 and int(i[5:8])%11 == 0 and int(i[4:7])%7 == 0 and int(i[3:6])%5 == 0 and int(i[2:5])%3 == 0 and int(i[1:4])%2 == 0:
    print(i)
    s += int(i)
print(s)
