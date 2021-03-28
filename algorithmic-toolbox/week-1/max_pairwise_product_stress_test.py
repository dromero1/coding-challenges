import numpy as np
import time


def max_pairwise_product_slow(numbers):
    n = len(numbers)
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            prod = numbers[i] * numbers[j]
            if prod >= res:
                res = prod
    return res


def max_pairwise_product_fast(numbers):
    first_max = max(numbers)
    numbers.remove(first_max)
    second_max = max(numbers)
    return first_max * second_max


if __name__ == "__main__":
    while True:
        # Random test
        n = np.random.randint(2, high=10000)
        numbers = list(np.random.randint(1, high=100, size=n))
        # Slow algorithm
        tic = time.perf_counter()
        slow_res = max_pairwise_product_slow(numbers)
        toc = time.perf_counter()
        slow_time = toc - tic
        # Fast algorithm
        tic = time.perf_counter()
        fast_res = max_pairwise_product_fast(numbers)
        toc = time.perf_counter()
        fast_time = toc - tic
        # Display
        print('V1 (r: {}, t: {:0.4f}) V2 (r: {}, t: {:0.4f})'.format(slow_res, slow_time, fast_res, fast_time))
        if slow_res != fast_res:
            print('Wrong answer!')
            print('Test: {}'.format(numbers))
            break