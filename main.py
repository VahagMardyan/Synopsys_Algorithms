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

def generator(a:int, b:int, size:int):
    arr=[]
    for n in range(0,size):
        arr.append(random.randint(a,b))
    insertion_sort(arr)
    return arr

array = generator(1,1000,12)
print(array)

sizes=[100,200,500,1000,2000,5000]

for n in sizes:
    arr = [random.randint(0,10000) for _ in range(n)]
    start = time.time()
    insertion_sort(arr)
    end = time.time()
    print(f"Array size {n}: time={(end-start) * 1000:.2f} miliseconds")

