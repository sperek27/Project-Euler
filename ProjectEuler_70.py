import collections

compare = lambda x, y: collections.Counter(x) == collections.Counter(y)

def facto(n):
  i = 2
  ans = 1
  while i*i <= n:
    if n%i == 0:
      power1 = i
      power2 = 1
      n /= i
      while n%i == 0:
        power1 *= i
        power2 *= i
        n /= i
      ans *= power1 - power2
    if i != 2:
      i += 1
    i += 1

def tot(n):
  ans = n
  i = 2
  while i*i <= n:
    if n%i == 0:
      while n%i == 0:
        n //= i
      ans -= ans//i
    i += 1
  if n > 1:
    ans -= ans//n 
  return ans 

def isPerm(a,b):
  if len(str(a)) != len(str(b)):
    return False
  if a-b > a//100:
    return False
  return compare(list(str(a)), list(str(b)))

i = 10000000
ans = []
record = 2
while i > 0:
  temp = tot(i)
  if isPerm(i, temp):
    div = i/temp
    if div < record:
      record = div
    print(i, record)
  i -= 1
