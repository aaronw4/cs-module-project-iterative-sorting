def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i            
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    min = 0
    max = len(arr) - 1

    while len(arr) > 0:
        mid =(min + max) // 2

        if target > arr[mid]:
            min = mid + 1
        elif target < arr[mid]:
            max = mid -1
        else:
            return mid

    return -1  # not found
