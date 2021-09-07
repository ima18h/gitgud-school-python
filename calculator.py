def add(x, y):
    return x + y

def divide(n, d):
    return n / d

def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1)

def sin(x, N = 20):
    sin = 0
    for n in range(N):
        sin += (-1)**n*x**(2*n + 1) / factorial(2*n + 1)
    return sin
