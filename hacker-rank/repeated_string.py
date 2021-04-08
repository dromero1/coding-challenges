import math


def character_frequency(c, s):
    return sum(1 if ch == c else 0 for ch in s)


def repeated_string(s, n):
    length = len(s)
    times = math.floor(n / length)
    left = n % length
    return times * character_frequency('a', s) + character_frequency('a', s[:left])


if __name__ == '__main__':
    s = input()
    n = int(input())
    print(repeated_string(s, n))
