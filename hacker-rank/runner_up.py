if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    top = max(arr)
    others = [ i for i in arr if i < top ]
    runner_up = max(others)
    print(runner_up)
