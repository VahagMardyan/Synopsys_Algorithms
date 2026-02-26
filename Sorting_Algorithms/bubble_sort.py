from random import randint
import time

def bubble_sort(arr:list):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                (arr[j], arr[j+1]) = (arr[j+1], arr[j])
                swapped = True
        if not swapped:
            break

def is_sorted(arr:list) -> bool:
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

class Test:
    def __init__(self):
        pass
    
    def generate_array(self, size:int):
        return [ randint(-10_000, 10_000) for _ in range(size) ]
    
    def timer(self, size:int):
        arr = self.generate_array(size)
        print(f"\nArray size: {len(arr)}")
        start = time.perf_counter()
        bubble_sort(arr)
        end = time.perf_counter()
        duration = (end - start) * 1000
        correct = is_sorted(arr)
        print(f"Bubble sort: time={duration:.4f}ms | sorted={correct}")

# t = Test()
# i = 10
# while i<=1000:
#     t.timer(i)
#     i = int(i*1.01)+1

