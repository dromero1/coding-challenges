def gcd(a, b):
    """ Brute-force algorithm """
    best = 0
    for i in range(1, a + b):
        if a % i == 0 and b % i == 0:
            best = i
    return best


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(gcd(a, b))
