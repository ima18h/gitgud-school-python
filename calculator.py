def add(x, y):
    return x + y

def divide(n, d):
    return n / d

def factorial(n):
    try:
        n*(n-1)
    except:
        raise ValueError("Not defined. choose an integer > 0")
    if n < 0:
        raise ValueError("Not defined. choose a number > 0")

    if n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact

def sin(x, N = 20):
    sin = 0
    for n in range(N):
        sin += (-1)**n*x**(2*n + 1) / factorial(2*n + 1)
    return sin
