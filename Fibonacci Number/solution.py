def fib(N):
    a, b = 0, 1
    for _ in range(N):
        a, b = b, (a+b)
    return a

for i in range(30):
    print(fib(i))