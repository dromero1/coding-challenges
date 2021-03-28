import re


if __name__ == "__main__":
    f = input().rstrip().split()
    n = int(f[0])
    m = int(f[1])
    matrix = []
    for _ in range(n):
        item = input()
        matrix.append(item)
    code = ""
    for j in range(m):
        for i in range(n):
            code = code + matrix[i][j]
    decoded = re.sub(r'(\w)(\W+)(\w)', r'\1 \3', code)
    print(decoded)