def r(a,b):
    n=0
    for i in range(0,a):
        for j in range(0,b):
            n=n + ((a-i)*(b-j))
    return n
def score(a,b):
    return abs(2000000-r(a,b))
x=1
y=1
optimal = 10000000
area = 0
while True:
    x=1
    while r(x,y)<2000000:
        if score(x,y)<optimal:
            optimal = score(x,y)
            area = x*y
        x=x+1
    y=y+1
print(optimal)
print(area)
