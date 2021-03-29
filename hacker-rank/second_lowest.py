if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = [name, score]
        students.append(student)
    lowest = min(s[1] for s in students)
    others = [ s for s in students if s[1] > lowest ]
    second_lowest = min(s[1] for s in others)
    names = [ s[0] for s in students if s[1] == second_lowest ]
    names.sort()
    for name in names:
        print(name)
