def fibonacci(n):
    fib = [0, 1] + [None] * (n - 1 if n >= 2 else n + 1)
    for i in range(2, n + 1):
        fib[i] = (fib[i - 1] + fib[i - 2]) % 10
    return fib[n]


if __name__ == "__main__":
    n = int(input())
    print(fibonacci(n))
