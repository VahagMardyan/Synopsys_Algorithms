def binarysearch(arr:list,x) -> int:
    """Assumes that the array is sorted"""
    # arr.sort()
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif x > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [1,2,3,4,5,10,18]
x = 10
print(binarysearch(arr, x)) # # 5
