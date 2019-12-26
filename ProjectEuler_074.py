def facto(n):
    z = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    return z[n]

def cycle(n):
    z = 0
    for i in str(n):
        z += facto(int(i))
    return z

def lengthOfChain(n):
    z = []
    nprime = n
    length = 1
    while True:
        z.append(nprime)
        nprime = cycle(nprime)
        if nprime in z:
            return length
        length += 1
count = 0
n = 1
while n<1000000:
    if lengthOfChain(n)==60:
        count += 1       
    n += 1
print(count)  
