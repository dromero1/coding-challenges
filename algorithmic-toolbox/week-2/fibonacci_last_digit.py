def fibonacci(n):
    if n <= 1:
        return n
    prev = 0
    curr = 1
    for _ in range(n - 1):
        prev, curr = curr, (prev + curr) % 10
    return curr


if __name__ == "__main__":
    n = int(input())
    print(fibonacci(n))
