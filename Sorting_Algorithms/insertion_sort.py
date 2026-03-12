# Insertion Sort algorithm

def insertion_sort(arr:list):
    for i in range(1,len(arr)):
        key = arr[i]
        j=i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j=j-1
        arr[j+1] = key
         
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
