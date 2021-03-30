def fibonacci(n):
    fib = [0, 1] + [None] * (n - 1 if n >= 2 else n + 1)
    for i in range(2, n + 1):
        fib[i] = (fib[i - 1] + fib[i - 2]) % 10
    return fib[n]


def pisano_period(m):
    prev = 0
    curr = 1
    for i in range(m * m):
        temp = curr
        curr = (prev + curr) % m
        prev = temp
        if prev == 0 and curr == 1:
            return i + 1
    return -1


def fibonacci_modulo(n, m):
    rem = n % pisano_period(m)
    return fibonacci(rem) % m


def last_digit_fibonacci_sum(n):
    mod = fibonacci_modulo(n + 2, 10)
    if mod == 0:
        return 9
    else:
        return mod - 1


if __name__ == "__main__":
    n = int(input())
    print(last_digit_fibonacci_sum(n))
