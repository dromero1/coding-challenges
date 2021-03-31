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


def fibonacci(n):
    n = n % pisano_period(10)
    if n <= 1:
        return n
    prev = 0
    curr = 1
    for _ in range(n - 1):
        prev, curr = curr, prev + curr
    return curr


def last_digit_fibonacci_sum_of_squares(n):
    fn = fibonacci(n)
    fp = fibonacci(n - 1)
    return (fn * (fn + fp)) % 10


if __name__ == "__main__":
    n = int(input())
    print(last_digit_fibonacci_sum_of_squares(n))
