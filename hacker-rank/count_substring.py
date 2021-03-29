def count_substring(string, sub_string):
    count = 0
    n = len(string)
    m = len(sub_string)
    for i in range(n - m + 1):
        if string[i:i+m] == sub_string:
            count = count + 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
