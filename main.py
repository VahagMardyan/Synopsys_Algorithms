import random
import time

# # Insertion Sort algorithm

def insertion_sort(arr:list):
    for i in range(1,arr.__len__()):
        key = arr[i]
        j=i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j=j-1
        arr[j+1] = key

def merge(arr:list, left:int, mid:int, right:int):
    n1 = mid - left + 1
    n2 = right - mid
    L=[0] * n1
    R=[0] * n2
    for i in range(n1):
        L[i] = arr[left + i]
    
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
    
    i=0
    j=0
    k=left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1
        k+=1

    while i < n1:
        arr[k] = L[i]
        i+=1
        k+=1

    while j < n2:
        arr[k] = R[j]
        j+=1
        k+=1
    
def merge_sort(arr:list, left:int, right:int):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid+1, right)
        merge(arr, left, mid, right)
 
# def format_auto_duration(d:float):
#     ns = d * 1e9
#     if ns < 1_000:
#         return f"{ns:.2f} ns"
#     elif ns < 1_000_000:
#         return f"{ns / 1_000:.2f} µs" # # microseconds
#     elif ns < 1_000_000_000:
#         return f"{ns / 1_000_000:.2f} ms"
#     else:
#         return f"{ns / 1_000_000_000:.2f} s"
