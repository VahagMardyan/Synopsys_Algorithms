def swap(arr:list, i:list, j:list) -> None:
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr:list, low:int, high:int) -> int:
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    
    swap(arr, i+1, high)
    return i+1

def quicksort(arr:list, low:int, high:int) -> None:
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)
