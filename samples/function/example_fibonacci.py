def fib(n):
    a = 0
    b = 1
    while a < n:
        print(a, end=' ')
        t = a
        a = b
        b = t + b
    print()


fib(2000)

