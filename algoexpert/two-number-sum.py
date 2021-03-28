# O(n) time | O(n) space
def two_number_sum(array, target):
    nums = {}
    for x in array:
        y = target - x
        if y in nums:
            return [x, y]
        else:
            nums[x] = True
    return []