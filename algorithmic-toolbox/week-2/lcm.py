def gcd(a, b):
    """ Greatest common divisor (Euclidean algorithm) """
    if b == 0:
        return a
    a_prime = a % b
    return gcd(b, a_prime)


def lcm(a, b):
    """ Least common multiple """
    return int(abs(a * b) / gcd(a, b))


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(lcm(a, b))
