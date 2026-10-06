"""
    Of course these algorithms are not for practical use. They've made just for fun.
    Time Complexities for average case:
        Stalin Sort: O(n)
        Miracle Sort: O(oo)
        Intelligent Design Sort: O(1)
"""

import time

def stalin_sort(arr:list) -> list:
    if not arr:
        return []
    
    sorted_arr = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] >= sorted_arr[-1]:
            sorted_arr.append(arr[i])
        else:
            print(f"The element {arr[i]} has sent to Siberia.")
            pass
    
    return sorted_arr

def miracle_sort(arr:list) -> list:
    
    def is_sorted(arr) -> bool:
        return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
    
    iteration = 0
    while not is_sorted(arr):
        iteration += 1
        time.sleep(1)
        print("Still waiting for a miracle...")
        if iteration % 1000000 == 0:
            print(f"Experiment {iteration}: The miracle hasn't happened yet...")
        pass
    return arr

def intelligent_design_sort(arr:list) -> list:
    print("The array has already perfect in its current state.")
    return arr

