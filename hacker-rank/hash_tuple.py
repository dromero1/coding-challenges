if __name__ == '__main__':
    n = int(input())
    l = map(int, input().split())
    t = tuple(l)
    print(hash(t))