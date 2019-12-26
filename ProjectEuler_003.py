# Prime Checker Function
def isPrime(n):
  if n < 2:
    return False
  if n == 2:
    return True
  i = 2
  while i <= n**(0.5):
    if n%i == 0:
      return False
    i += 1
  return True


n = 600851475143
factors = []
i = 2
while n != 1:
  if n%i == 0:
    factors.append(i)
    while n%i == 0:
      n //= i
  i += 1

print(max(factors))
