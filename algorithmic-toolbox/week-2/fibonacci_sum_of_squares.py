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


def last_digit_fibonacci_sum_of_squares(n):
    fn = fibonacci_modulo(n, 10)
    fp = fibonacci_modulo(n - 1, 10)
    return (fn * (fn + fp)) % 10


if __name__ == "__main__":
    n = int(input())
    print(last_digit_fibonacci_sum_of_squares(n))
