def gcd(a, b):
    """ Euclidean algorithm """
    if b == 0:
        return a
    a_prime = a % b
    return gcd(b, a_prime)


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(gcd(a, b))
