def fibonacci(n):
    if n <= 1:
        return n
    prev = 0
    curr = 1
    for _ in range(n - 1):
        prev, curr = curr, prev + curr
    return curr


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


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(fibonacci_modulo(n, m))
