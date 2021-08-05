def groupsum(start, nums, target):
    if start == len(nums):
        return target == 0
    if groupsum(start + 1, nums, target - nums[start]):
        return True
    if groupsum(start + 1, nums, target):
        return True
    return False


def ArrayAddition(arr):
    arr.sort()
    target = arr[len(arr) - 1]
    arr.remove(target)
    return groupsum(0, arr, target)


print(ArrayAddition(input()))
