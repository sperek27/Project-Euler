def reverse(s):
  return s[::-1]

def pal(s):
  if str(s) == reverse(str(s)):
    return True
  else:
    return False
  
def binary(n):
  q=0
  while n>0:
    z=0
    while (2**z)<=n:
      z=z+1
    n=n-(2**(z-1))
    q=q+(10**(z-1))
  return q

a=1
count = 0
while a < 1000000:
  if pal(a) == True and pal(binary(a)) == True:
    count = count + a
  a=a+1
print(count)
