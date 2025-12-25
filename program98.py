def findSmallest(arr):
    if len(arr) == 1:
        return arr[0]
    return min(arr[0], findSmallest(arr[1:]))


print(findSmallest([3, 2, 5, 4, 1]))
