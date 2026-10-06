from abc import ABC, abstractmethod
from random import randint

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: list[int]) -> list[int]:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

class BubbleSort(SortStrategy):
    def __bubble_sort(self, arr:list):
        for i in range(len(arr)):
            swapped = False
            for j in range(len(arr)-1-i):
                if arr[j] > arr[j+1]:
                    (arr[j], arr[j+1]) = (arr[j+1], arr[j])
                    swapped = True
            if not swapped:
                break

    def sort(self, data: list[int]) -> list[int]:
        """
        Bubble Sort algorithm implementation.
        Time Complexity for average case: O(n²)
        """
        arr = data.copy()
        self.__bubble_sort(arr)
        return arr

    @property
    def name(self) -> str:
        return "Bubble Sort"

class InsertionSort(SortStrategy):

    def __insertion_sort(self, arr:list):
        for i in range(1,len(arr)):
            key = arr[i]
            j=i-1
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j=j-1
            arr[j+1] = key


    def sort(self, data: list[int]) -> list[int]:
        """
        Insertion Sort algorithm implementation
        Time Complexity for average case: O(n²)
        """
        arr = data.copy()
        self.__insertion_sort(arr)
        return arr

    @property
    def name(self) -> str:
        return "Insertion Sort"

class MergeSort(SortStrategy):
    def __merge(self, arr:list, left:int, mid:int, right:int):
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

    def __merge_sort(self, arr:list, left:int, right:int):
        if left < right:
            mid = (left + right) // 2
            self.__merge_sort(arr, left, mid)
            self.__merge_sort(arr, mid+1, right)
            self.__merge(arr, left, mid, right)

    def sort(self, data: list[int]) -> list[int]:
        """
        Merge Sort algorithm implementation
        Time Complexity for average case: O(n*log₂(n))
        """
        arr = data.copy()
        self.__merge_sort(arr, 0, len(arr) - 1)
        return arr

    @property
    def name(self) -> str:
        return "Merge Sort"

class HeapSort(SortStrategy):

    def __max_heapify(self, arr:list, index:int, heap_size):
        l = 2 * index + 1
        r = 2 * index + 2
        largest = index

        if l < heap_size and arr[l] > arr[largest]:
            largest = l

        if r < heap_size and arr[r] > arr[largest]:
            largest = r

        if largest != index:
            arr[index], arr[largest] = arr[largest], arr[index]
            self.__max_heapify(arr, largest, heap_size)

    def __build_max_heap(self, arr:list):
        heap_size = len(arr)
        for i in range(heap_size//2 - 1, -1, -1):
            self.__max_heapify(arr,i, heap_size)

    def __heapsort(self, arr:list):
        heap_size = len(arr)
        self.__build_max_heap(arr)
        for i in range(heap_size - 1, 0 ,-1):
            arr[0],arr[i] = arr[i],arr[0]
            self.__max_heapify(arr, 0, i)

    def sort(self, data: list[int]) -> list[int]:
        """
        Heap Sort algorithm implementation
        Time Complexity for average case: O(n*log₂(n))
        """
        arr = data.copy()
        self.__heapsort(arr)
        return arr

    @property
    def name(self) -> str:
        return "Heap Sort"

class QuickSort(SortStrategy):
    def __swap(self, arr:list, i:int, j:int) -> None:
        arr[i], arr[j] = arr[j], arr[i]

    def __partition(self, arr:list, low:int, high:int) -> int:
        """Randomized Partition"""
        random_idx = randint(low, high)
        self.__swap(arr, random_idx, high)
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                self.__swap(arr, i, j)

        self.__swap(arr, i+1, high)
        return i+1

    def __quicksort(self, arr:list, low:int, high:int) -> None:
        if low < high:
            pi = self.__partition(arr, low, high)
            self.__quicksort(arr, low, pi-1)
            self.__quicksort(arr, pi+1, high)


    def sort(self, data: list[int]) -> list[int]:
        """
        Quick Sort algorithm implementation
        Time Complexity for average case: O(n*log₂(n))
        """
        arr = data.copy()
        self.__quicksort(arr, 0, len(arr) - 1)
        return arr

    @property
    def name(self) -> str:
        return "Quick Sort"


class SelectionSort(SortStrategy):

    def __selectionsort(self, arr):
        n = len(arr)
        for i in range(n-1):
            min_index = i
            for j in range(i+1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]

    def sort(self, data: list[int]) -> list[int]:
        """
        Selection Sort algoritm implementation
        Time Complexity for average case: O(n²)
        """
        arr = data.copy()
        self.__selectionsort(arr)
        return arr

    @property
    def name(self) -> str:
        return "Selection Sort"


class CountingSort(SortStrategy):

    def __countsort(self, arr:list) -> list:
        if not arr:
            return []

        n = len(arr)
        min_val = min(arr)
        max_val = max(arr)

        range_of_elements = max_val - min_val + 1
        cnt_arr = [0] * range_of_elements

        for v in arr:
            cnt_arr[v - min_val] += 1

        for i in range(1, range_of_elements):
            cnt_arr[i] += cnt_arr[i - 1]

        ans = [0] * n

        for i in range(n - 1, -1, -1):
            v = arr[i]
            index = v - min_val
            ans[cnt_arr[index] - 1] = v
            cnt_arr[index] -= 1

        return ans

    def sort(self, data: list[int]) -> list[int]:
        """
        Counting Sort algorithm implementation
        Time Complexity for average case: O(n+k) where
            n -> The number of elements
            k -> The range of the input values k=max-min+1
        """

        return self.__countsort(data.copy())

    @property
    def name(self) -> str:
        return "Counting Sort"


class RadixSort(SortStrategy):
    
    def __radixsort(self, arr:list) -> list:
        if not arr:
            return []

        negatives = [x for x in arr if x < 0]
        positives = [x for x in arr if x >= 0]

        def _radix_for_positives(nums):
            if not nums:
                return []
            max_num = max(nums)
            exp = 1
            while max_num // exp > 0:
                nums = _counting_sort_by_digit(nums, exp)
                exp *= 10
            return nums

        def _counting_sort_by_digit(nums, exp):
            n = len(nums)
            ans = [0] * n
            cnt = [0] * 10

            for x in nums:
                index = (x // exp) % 10
                cnt[index] += 1

            for i in range(1, 10):
                cnt[i] += cnt[i-1]

            for i in range(n - 1, -1, -1):
                x = nums[i]
                index = (x // exp) % 10
                ans[cnt[index] - 1] = x
                cnt[index] -= 1

            return ans

        if negatives:
            neg_pos = [abs(x) for x in negatives]
            neg_sorted = _radix_for_positives(neg_pos)
            negatives = [-x for x in reversed(neg_sorted)]

        positives = _radix_for_positives(positives)

        return negatives + positives

    def sort(self, data: list[int]) -> list[int]:
        """
        Radix sort algorithm implementation
        Time Complexity for average case: O(d*(n+b)) where 
            n -> The number of elements, 
            d -> The number of digits in the largest number
            b -> The base of the number system being used (decimal, bin, oct, hex, ...). In our example b=10
        """
        return self.__radixsort(data.copy())

    @property
    def name(self) -> str:
        return "Radix Sort"


class StalinSort(SortStrategy):

    def __stalin_sort(self, arr:list) -> list:
        if not arr:
            return []

        sorted_arr = [arr[0]]
        for i in range(1, len(arr)):
            if arr[i] >= sorted_arr[-1]:
                sorted_arr.append(arr[i])
            else:
                # print(f"The element {arr[i]} has sent to Siberia.")
                pass
            
        return sorted_arr

    def sort(self, data: list[int]) -> list[int]:
        """
        Stalin Sort algoritm implementation
        Time Complexity for average case: O(n)
        """
        return self.__stalin_sort(data.copy())

    @property
    def name(self) -> str:
        return "Stalin Sort."

