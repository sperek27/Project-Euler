# Dynamic Fibonacci Algorithm
def fib(n):
  arr = [1,1]
  for i in range(2,n):
    arr.append(arr[i-1] + arr[i-2])
  return arr[n-1]

#finding the first fibonacci number greater than 4 million
i = 1
while True:
  if fib(i) > 4000000:
    print(fib(i+1))
    break
  i += 1

# recall that the sum of even fibonacci numbers if equal to the sum of odd fibonacci numbers and F1 + F2 .. + Fn = Fn+2 - F2
print(9227464//2)
