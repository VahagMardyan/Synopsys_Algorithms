def max_heapify(arr:list, index:int, heap_size):
    l = 2 * index + 1
    r = 2 * index + 2
    largest = index

    if l < heap_size and arr[l] > arr[largest]:
        largest = l
    
    if r < heap_size and arr[r] > arr[largest]:
        largest = r
    
    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        max_heapify(arr, largest, heap_size)

def build_max_heap(arr:list):
    heap_size = len(arr)
    for i in range(heap_size//2 - 1, -1, -1):
        max_heapify(arr,i, heap_size)

def heapsort(arr:list):
    heap_size = len(arr)
    build_max_heap(arr)
    for i in range(heap_size - 1, 0 ,-1):
        arr[0],arr[i] = arr[i],arr[0]
        max_heapify(arr, 0, i)
