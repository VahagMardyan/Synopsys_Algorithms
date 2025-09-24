from random import randint
import time

# # Brute-force algorithm O(n²)
def max_subarray_brute_force(arr:list):
    res = arr[0]
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            res = max(res, current_sum)
    return res

# # Divide & Conquer algorithm O(n*log₂(n))
def find_max_crossing_subarray(arr:list, low:int, mid:int, high:int):
    left_sum = float('-inf')
    current_sum = 0
    max_left = None
    for i in range(mid, low - 1, -1):
        current_sum += arr[i]
        if current_sum > left_sum:
            left_sum = current_sum
            max_left = i
    
    right_sum = float('-inf')
    current_sum = 0
    max_right = None
    for j in range(mid+1, high+1):
        current_sum += arr[j]
        if current_sum > right_sum:
            right_sum = current_sum
            max_right = j
    return (max_left, max_right, left_sum + right_sum)

def find_max_subarray(arr:list, low:int, high:int):
    if high == low:
        return (low, high, arr[low]) # # only one element
    else:
        mid = (low + high)//2 
        (left_low, left_high, left_sum) = find_max_subarray(arr, low, mid)
        (right_low, right_high, right_sum) = find_max_subarray(arr, mid+1, high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(arr, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)

# # Kadane's algorithm O(n)
def max_subarray_kadane(arr:list):
    max_so_far = arr[0]
    max_ending_here = arr[0]
    for i in range(1, len(arr)):
        max_ending_here += arr[i]
        if max_ending_here < arr[i]:
            max_ending_here = arr[i]
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
    return max_so_far

class Test:
    def __init__(self):
        self.algorithms = {
            "Divide and conquer": lambda arr :  find_max_subarray(arr, 0, len(arr)-1)[2],
            "Kadane":max_subarray_kadane,
            "Brute-force":max_subarray_brute_force,
        }

    def generate_array(self,size:int):
        return [ randint(-10_000, 10_000) for _ in range(size) ]
    
    def timer(self, size:int):
        arr = self.generate_array(size)
        print(f"\nArray size: {len(arr)}")
        results = {}
        for name, func in self.algorithms.items():
            if name == "Brute-force" and size > 5000:
                print(f"{name}: skipped (too slow)")
                continue
            start = time.perf_counter()
            res = func(arr)
            end = time.perf_counter()
            spent_time = (end - start) * 1000
            print(f"{name}: result={res}, time={spent_time:.4f} ms")
            results[name] = res

        # # Check correctness
        if len(results) > 1 and len(set(results.values())) > 1:
            print("Warning: mismatch between algorithms!")  

t = Test()
for size in [10, 100, 1000, 5000, 10000]:
    t.timer(size)