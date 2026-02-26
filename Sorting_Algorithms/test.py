from sorting_algorithms import *
import random, time
import csv

def generate_list(n:int, min_val:int = 0, max_val:int = 10_000) -> list:
    return [ random.randint(min_val, max_val) for _ in range(n) ]

def is_sorted(seq):
    """ Check if sequence is sorted """
    return all(seq[i] <= seq[i+1] for i in range(len(seq)-1))

class SortingTester:
    def __init__(self, sorting_func):
        self.sorting_func = sorting_func
        self.results = []
    
    def test_correctness_once(self, n):
        """Generate random list, sort it, check correctness"""
        arr = generate_list(n)
        original = arr[:]
        self.sorting_func(arr)
        if not is_sorted(arr):
            print("Not sorted properly")
            return False
        
        if sorted(original) != arr:
            print("Elements missing or duplicated")
            return False
        return True
    
    def test_correctness(self, factor=20, limit=10_000):
        """Run correctness tests with increasing sizes"""
        count = 10
        while count < limit:
            if self.test_correctness_once(count):
                print(f"Correctness test passed with {count} elements")
            else:
                print(f"Correctness test failed with {count} elements")
                return False
            count += (count * factor) // 100
        return True
    
    def measure_time(self, n):
        """Measure time spent on sorting"""
        arr = generate_list(n)
        start = time.perf_counter()
        self.sorting_func(arr)
        end = time.perf_counter()
        spent_ms = (end - start) * 1000
        self.results.append((n,spent_ms))
        print(f"Sorting {n} elements took {spent_ms:.2f} ms")
    
    def test_wall_time(self, factor=10, start_size=10, limit=10_00):
        """Run performance tests with increasing sizes"""
        count = start_size
        while count < limit:
            self.measure_time(count)
            count += (count * factor) // 100
        return True
    
    def export_results(self,filename="sorting_times.xlsx"):
        with open("sorting_times.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Size", "Time_ms"])
            writer.writerows(self.results)
        print("Exported sorting times to sorting_times.csv")
    

def merge_sort_wrapper(arr):
    """Wrapper so we can pass merge_sort to SortingTester"""
    if arr:
        merge_sort(arr, 0, len(arr)-1)

def run_sorting_test(test_name="",sorting_func=None):
    tester = SortingTester(sorting_func)
    tester.test_correctness()
    tester.test_wall_time()
    # tester.export_results(f"{test_name.replace(' ','_')}_data.csv")

run_sorting_test("Insertion sort",insertion_sort)