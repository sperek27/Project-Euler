a=1
b=1
c=3
while True:
    a=a+b
    c=c+1
    if len(str(a+b))==1000:
        print(c)
        break
    b=b+a
    c=c+1
    if len(str(a+b))==1000:
        print(c)
        break    
    
