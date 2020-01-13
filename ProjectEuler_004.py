def isPalindrome(n):
  s = str(n)
  return s == s[::-1]

record = 0
a = 999
while a > 100:
  b = 999
  while b > 100:
    p = a*b
    if isPalindrome(p) and p > record:
      record = p
      print(p)
    b -= 1
  a -= 1
