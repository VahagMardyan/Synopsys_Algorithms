from sorting_algorithms import merge_sort, insertion_sort
from bubble_sort import bubble_sort
from heap_sort import heapsort
from random import randint
import time

def is_sorted(arr:list) -> bool:
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

def generate_array(size:int) -> list:
    return [ randint(-10_000, 10_000) for _ in range(size) ]
    
original = generate_array(50_000)
print(f"Array size: {len(original)}\n")

# # Insertion sort O(n²)
arr = original.copy()
start = time.perf_counter()
insertion_sort(arr)
end = time.perf_counter()
duration = (end - start) * 1000
print(f"Algorithm name: Insertion sort | time={duration:.4f}ms | sorted={is_sorted(arr)}\n") # ≈56778.7527 ms ≈56 seconds

# # Bubble sort O(n²)

arr = original.copy()
start = time.perf_counter()
bubble_sort(arr)
end = time.perf_counter()
duration = (end - start) * 1000
print(f"Algorithm name: Bubble sort | time={duration:.4f}ms | sorted={is_sorted(arr)}\n") # ≈134731.2737 ms=2.24 minutes

# # Merge sort O(n*log(n))

arr = original.copy()
start = time.perf_counter()
merge_sort(arr, 0, len(arr)-1)
end = time.perf_counter()
duration = (end - start) * 1000
print(f"Algorithm name: Merge sort, time={duration:.4f}ms | sorted={is_sorted(arr)}\n") # ≈165.2721ms

# # Heap sort O(n*log(n))
arr = original.copy()
start = time.perf_counter()
heapsort(arr)
end = time.perf_counter()
duration = (end - start) * 1000
print(f"Algorithm name: Heap sort, time={duration:.4f}ms | sorted={is_sorted(arr)}\n") # ≈165.2721ms
