def max_pairwise_product(numbers):
    n = len(numbers)
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            prod = numbers[i] * numbers[j]
            if prod >= res:
                res = prod
    return res


if __name__ == "__main__":
    n = int(input())
    numbers = [ int(x) for x in input().split() ]
    print(max_pairwise_product(numbers))
