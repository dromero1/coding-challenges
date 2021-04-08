def jumping_on_clouds(clouds, jumps):
    if len(clouds) == 1:
        return jumps
    jump_1, jump_2 = float('inf'), float('inf')
    if len(clouds) >= 2 and clouds[1] == 0:
        jump_1 = jumping_on_clouds(clouds[1:], jumps + 1)
    if len(clouds) >= 3 and clouds[2] == 0:
        jump_2 = jumping_on_clouds(clouds[2:], jumps + 1)
    return min(jump_1, jump_2)


if __name__ == '__main__':
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    print(jumping_on_clouds(c, 0))
