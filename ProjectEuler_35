def isprime(n):
    if n < 2:
        return False
    if n%2==0:
        return False
    i=3
    while i<=n**(0.5):
        if n%i==0:
            return False
        i=i+1
    return True

def circular(n):
    length = len(str(n))
    string = str(n)
    if n == 2:
        return True
    for i in range(length):
        if not isprime(int(string)):
            return False
        string = string[1:n] + string[0]
    return True
c = 1
n = 1
while n < 1000000:
    if circular(n)==True:
        c=c+1
    n=n+2
print(c)
