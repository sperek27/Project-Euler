def increasing(n):
    number = str(n)
    if int(number[1])>=int(number[0]):
        for i in range((len(number)-2)):
            if int(number[i+2])<int(number[i+1]):
                return False
        return True
    return False
def decreasing(n):
    number = str(n)
    if int(number[1])<=int(number[0]):
        for i in range((len(number)-2)):
            if int(number[i+2])>int(number[i+1]):
                return False
        return True
    return False
print(decreasing(110))
def bouncy(n):
    if (increasing(n)==False and decreasing(n)==False):
        return True
    else:
        return False
proportion = 0.000
c = 0
i = 100
while True:
    if bouncy(i)==True:
        c=c+1
    proportion = float(c*((i)**-1))
    if proportion >= 0.99:
        print(proportion, i)
        break
    i=i+1
