def counting_valleys(steps, path):
    level = 0
    valleys = 0
    for step in path:
        if level == 0 and step == 'D':
            valleys += 1
        if step == 'U':
            level += 1
        else:
            level -= 1
    return valleys


if __name__ == '__main__':
    steps = int(input().strip())
    path = input()
    print(counting_valleys(steps, path))
