from sorting_algorithms import merge_sort, insertion_sort
from bubble_sort import bubble_sort
from heap_sort import heapsort
from quick_sort import quicksort

from random import randint
import time
import matplotlib.pyplot as plt
import pandas as pd

algs = {
    "Insertion" : insertion_sort,
    "Bubble" : bubble_sort,
    "Merge" : lambda arr : merge_sort(arr, 0, len(arr) - 1),
    "Heap" : heapsort,
    "Quick": lambda arr : quicksort(arr, 0, len(arr) - 1)
}

def is_sorted(arr:list) -> bool:
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

def generate_array(size:int) -> list:
    return [ randint(-10_000, 10_000) for _ in range(size) ]
    
sizes = []
n = 10_000
factor = 0.1 # # growth factor, (0;1]

while n <= 50_000:
    sizes.append(n)
    n = int(n * (1+factor))

print(f"Sizes: {sizes}\nSize growth factor: {factor*100}%")

results = []

for size in sizes:
    print(f"\n=== Testing size {size} ===")
    base_arr = generate_array(size)
    for name, func in algs.items():
        arr = base_arr.copy()
        if name in ("Insertion", "Bubble") and size > 20_000:
            print(f"Skipping {name} for size {size} (too slow)")
            results.append((size, name, None))
            continue
        start = time.perf_counter()
        func(arr)
        end = time.perf_counter()

        ms = (end - start) * 1000
        ok = is_sorted(arr)
        print(f"{name:10s} | {ms:10.2f}ms | sorted={ok}")
        results.append((size, name, ms))

df = pd.DataFrame(results, columns=["Size", "Algorithm", "Time (ms)"])
print(df)

# df.to_excel("results.xlsx", index=False)
# print("Saved to results.xlsx")

plt.figure(figsize=(10,6))

for name in algs.keys():
    sub = df[df["Algorithm"] == name]
    plt.plot(sub["Size"], sub["Time (ms)"], marker="o", label=name)

plt.xlabel("Array size")
plt.ylabel("Time (ms)")
plt.title(f"Sorting Algorithms Performance ({factor*100}% growth size)")
plt.legend()
plt.grid(True)
plt.show()

"""
Time complexities (for average cases)
Insertion sort: O(n²)
Bubble sort: O(n²)
Merge sort: O(n*log₂(n))
Heap sort: O(n*log₂(n))
Quick sort: O(n*log₂(n))
"""

