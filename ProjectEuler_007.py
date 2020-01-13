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

i = 3
count = 2
while count < 10001:
  i += 2
  if isPrime(i):
    count += 1
print(i)
