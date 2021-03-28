def swap_case(s):
    l = [ ( c.upper() if c.islower() else c.lower() ) for c in s ]
    return "".join(l)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)