import math


def sock_merchant(n, ar):
    sock_count = {}
    for sock in ar:
        if sock not in sock_count:
            sock_count[sock] = 1
        else:
            sock_count[sock] += 1
    pairs = 0
    for _, count in sock_count.items():
        pairs += math.floor(count / 2)
    return pairs


if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    print(sock_merchant(n, ar))
