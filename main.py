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
    

def timing(sizes:list):

    for n in sizes:
        arr = [random.randint(0,10000) for _ in range(n)]
        start = time.time()
        insertion_sort(arr)
        end = time.time()
        duration = end - start
        print(f"Array size {n}: time={format_auto_duration(duration)}")

sizes = [100,200,500,1000,2000,5000,10000,20000,50000,100000,200000,500000]

timing(sizes)