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


def last_digit_fibonacci_partial_sum(m, n):
    mod_n = fibonacci_modulo(n + 2, 10)
    mod_m = fibonacci_modulo(m + 1, 10)
    return (mod_n + 10 - mod_m) % 10


if __name__ == "__main__":
    m, n = map(int, input().split())
    print(last_digit_fibonacci_partial_sum(m, n))
