l = []


def process(command):
    c = command.split()
    if c[0] == "insert":
        l.insert(int(c[1]), int(c[2]))
    elif c[0] == "print":
        print(l)
    elif c[0] == "remove":
        l.remove(int(c[1]))
    elif c[0] == "append":
        l.append(int(c[1]))
    elif c[0] == "sort":
        l.sort()
    elif c[0] == "pop":
        l.pop()
    elif c[0] == "reverse":
        l.reverse()


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        command = input()
        process(command)