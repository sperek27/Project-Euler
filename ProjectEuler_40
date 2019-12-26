# Gives the nth digit
def dn(n):
  l = 0
  i = 1
  digit = 1
  while l < n:
    for j in range(len(str(i))):
      digit = int(str(i)[j])
      l += 1
      if l == n:
        return digit
    i += 1
  return digit

print(dn(1)*dn(10)*dn(100)*dn(1000)*dn(10000)*dn(100000)*dn(1000000))
