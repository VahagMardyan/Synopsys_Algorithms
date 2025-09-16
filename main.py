import random
import time

# # Insertion Sort

def insertion_sort(arr:list):
    for i in range(1,arr.__len__()):
        key = arr[i]
        j=i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j=j-1
        arr[j+1] = key

a = [1,5,66,12] # # 1 5 12 66

# insertion_sort(a)

# print(a)

def generate_array(a:int, b:int, size:int):
    arr=[]
    for n in range(0,size):
        arr.append(random.randint(a,b))
    insertion_sort(arr)
    return arr

array = generate_array(1,1000,12)
# print(array)

def format_auto_duration(d:float):
    ns = d * 1e9
    if ns < 1_000:
        return f"{ns:.2f} ns"
    elif ns < 1_000_000:
        return f"{ns / 1_000:.2f} µs" # # microseconds
    elif ns < 1_000_000_000:
        return f"{ns / 1_000_000:.2f} ms"
    else:
        return f"{ns / 1_000_000_000:.2f} s"
    

def insertion_sort_timer(max_size:int = 10_000,factor:int = 10):
    n = 10
    while n<=max_size:
        arr = [ random.randint(0,10000) for _ in range(n) ]
        start = time.time()
        insertion_sort(arr)
        end = time.time()
        duration = end - start
        print(f"Array size {n}: time={format_auto_duration(duration)}")
        n += int((n * factor)/100)


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

def merge_sort_timer(max_size:int = 10_000, factor:int = 10):
    n = 10
    while n<=max_size:
        arr = [ random.randint(0,10000) for _ in range(n) ]
        start = time.time()
        merge_sort(arr, 0, len(arr) - 1)
        end = time.time()
        duration = end - start
        print(f"Array size {n}: time={format_auto_duration(duration)}")
        n += int((n * factor)/100)

m_size = 1000

print("Insertion sort results:\n")
insertion_sort_timer(m_size)

print("\nMerge sort results:\n")
merge_sort_timer(m_size)