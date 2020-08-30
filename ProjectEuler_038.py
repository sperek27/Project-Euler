def pandigital(s):
    a = ''.join(sorted(s))
    return a == "123456789"
for i in range(1,50000):
    ans = ""
    for j in range(1,9):
        ans += str(j*i)
        if pandigital(ans):
            print(ans)
