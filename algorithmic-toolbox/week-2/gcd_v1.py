def gcd(a, b):
    """ Greatest common divisor (Brute-force algorithm) """
    best = 0
    for i in range(1, a + b):
        if a % i == 0 and b % i == 0:
            best = i
    return best


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
