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
primes = []
for i in range(1000,9999):
  if isPrime(i):
    primes.append(i)

def aPermB(a,b):
  A = []
  B = []
  for i in str(a):
    A.append(i)
  for i in str(b):
    B.append(i)
  if sorted(A) == sorted(B):
    return True
  return False

for i in range(len(primes)):
  for j in range(i+1, len(primes)):
    if (primes[j] + primes[j] - primes[i]) in primes and aPermB(primes[i], primes[j]) and aPermB(primes[i], (primes[j] + primes[j] - primes[i])):
      print(primes[i], primes[j], (primes[j] + primes[j] - primes[i]))
