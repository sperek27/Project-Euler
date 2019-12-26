def gcd(m,n):
    if m< n: 
        (m,n) = (n,m)
    while (m % n != 0):
        (m, n) = (n, m % n)
    return n

count = 7500
for x in range(1, 51):
  for y in range(1, 51):
    count += min((y*gcd(x,y))//x, ((50-x)*gcd(x,y))//y)*2

print(count)
