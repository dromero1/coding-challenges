import textwrap


def wrap(string, max_width):
    wl = textwrap.wrap(string, max_width)
    wt = ''
    for l in wl:
        wt += l + '\n'
    return wt


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)