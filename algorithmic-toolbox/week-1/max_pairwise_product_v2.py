def max_pairwise_product(numbers):
    first_max = max(numbers)
    numbers.remove(first_max)
    second_max = max(numbers)
    return first_max * second_max


if __name__ == "__main__":
    n = int(input())
    numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(numbers))