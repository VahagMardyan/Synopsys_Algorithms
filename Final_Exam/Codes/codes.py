from collections import deque
# BFS / DFS
def bfs(graph, start_node):
    """
        Time Complexity: O(V + E)
        Space Complexity: O(V)
    """
    visited = set() # Այցելված գագաթները պահելու համար
    queue = deque([start_node]) # Հերթ, որը սկսվում է մեկնարկային գագաթից

    visited.add(start_node)

    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result

def dfs(graph, node, visited=None, result=None):
    """
        Time Complexity: O(V + E)
        Space Complexity: O(V)
    """
    if visited is None:
        visited = set()
    if result is None:
        result = []

    # 1. Մտնում ենք գագաթ, նշում որպես այցելված ու ավելացնում արդյունքին
    visited.add(node)
    result.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, result)

    return result

# ###################################

# Heap Sort
# Time complexity: O(nlogn)
# Space complexity: O(1)

def heapify(arr, n, i):
    while True:
        largest = i # Assuming that the root is the largest element
        left = 2*i + 1 # Left Child
        right = 2*i + 2 # Right Child

        # Check the left child
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Check the right child
        if right < n and arr[right] > arr[largest]:
            largest = right

        # if the largest one is not the root then swap
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            i = largest
        else:
            break

def heap_sort(arr):
    n = len(arr)

    # Step 1: Buld Max Heap
    # Starting from the last parent down to root

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Sorting (the deletion process)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# ###################################

# Merge Sort
# Time Complexity: O(nlogn)
# Space Complexity: O(n)
def merge(arr1:list, arr2:list):
    n1 = len(arr1)
    n2 = len(arr2)

    merged_array = [0] * (n1 + n2)

    i = 0; j  = 0; k = 0

    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            merged_array[k] = arr1[i]
            i += 1
        else:
            merged_array[k] = arr2[j]
            j += 1
        k += 1

    while i < n1:
        merged_array[k] = arr1[i]
        i += 1
        k += 1

    while j < n2:
        merged_array[k] = arr2[j]
        j += 1
        k += 1

    return merged_array

def merge_sort(arr:list):
    n = len(arr)
    if n <= 1:
        return arr

    mid = n // 2

    left_half = []
    right_half = []

    for i in range(0, mid):
        left_half.append(arr[i])

    for j in range(mid, n):
        right_half.append(arr[j])

    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    return merge(sorted_left, sorted_right)

# ###################################

# Bubble Sort
# Time Complexity: O(n^2) - Worst/Average Case, O(n) - Best Case
# Space Complexity: O(1)

def bubble_sort(arr:list):
    n = len(arr)

    for i in range(0, n):
        swapped = False
        for j in range(0, n - i -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

# ###################################

# Insertion Sort
# Time Complexity: Worst and average cases - O(n^2), best case - O(n)
# Space Complexity: O(1)

def insertion_sort(arr:list):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]

        # Move elements of arr[0,..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

# ###################################

# Quick Sort

# Time complexity of partition is O(n)
# Space complexity of partition is O(1)

def partition(arr:list, low:int, high:int):
    pivot = arr[high] # The last element as pivot
    i = low - 1 # bound of less elements

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Put pivot to its right place
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Time complexity of quick sort for best and average cases is O(nlogn), for worst case is: O(n^2)
# Space complexity of quick sort for best case is O(logn), for worst case is: O(n)

def quick_sort(arr:list, low:int, high:int):
    if low < high:
        pivot_idx = partition(arr, low, high)

        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)

# ###################################

import heapq
# Huffman Coding
class Node:
    def __init__(self, char:str, freq:int):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text:str):
    frequencies = {}
    for char in text:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1

    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        parent = Node(None, left.freq + right.freq)
        parent.left = left
        parent.right = right

        heapq.heappush(heap, parent)

    return heap[0]


def generate_codes(root:Node, current_code = "", codes = None):
    if codes is None:
        codes = {}

    if root is None:
        return codes

    if root.char is not None:
        codes[root.char] = current_code
        return codes

    generate_codes(root.left, current_code + '0', codes)
    generate_codes(root.right, current_code + '1', codes)

    return codes


def huffman_encode(text:str, codes:dict):
    return "".join(codes[char] for char in text)

def huffman_decode(encoded_text:str, root:Node):
    decoded_text = []
    current_node = root

    for bit in encoded_text:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_text.append(current_node.char)
            current_node = root

    return "".join(decoded_text)

############################################################

# Naive method: O(2^n)
def fib_rec(n:int):
    if n <= 1:
        return n
    return fib_rec(n - 2) + fib_rec(n - 1)

# Memoization method: top-down: O(n)
def fib_mem(n:int, memo:dict = None):
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n in memo:
        return memo[n]

    memo[n] = fib_mem(n - 2, memo) + fib_mem(n - 1, memo)
    return memo[n]

# Tabulation method: bottom-up: O(n)
def fib_tab(n:int):
    if n <= 1:
        return n
    F = [-1] * (n + 1)
    print(F)
    F[0] = 0
    F[1] = 1
    for i in range(2, n+1):
        F[i] = F[i - 2] + F[i - 1]
    return F[n]

# Optimized tabulation method: Space Complexity is O(1)
def fib_tab_optimized(n:int):
    if n <= 1:
        return n
    prev2 = 0
    prev1 = 1
    for i in range(2, n + 1):
        current = prev2 + prev1
        prev2 = prev1
        prev1 = current
    return prev1

###########################################################

# Time Complexity: O(n*m) 
# Space Complexity: O(n*m)

def knapsack_01(weights:list[int], prices:list[int], m:int) -> int:
    n = len(weights)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, m + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + prices[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][m]

##############################################################

# Coin Change Problem
# Time Complexity: O(n*m)
# Space Complexity: O(n*m)

def coin_change(coins:list[int], amount:int) -> int:
    # amount + 1 չափանի զանգված, որի բոլոր տարրերը սկզբում անվերջություններ են
    dp = [float('inf')] * (amount + 1)

    # amount = 0 ստանալու համար մեզ պետք է 0 մետաղադրամ
    dp[0] = 0

    for n in range(1, amount + 1):
        # Փորձարկում ենք մեր ունեցած բոլոր մանրադրամները ընթացիկ n գումարի համար
        for coin in coins:
            # Եթե մանրադրամը մեծ չէ ընթացիկ n գումարից, այն կարող ենք օգտագործել
            if n >= coin:
                # Օպտիմալ ընտրություն. համեմատում ենք եղած տարբերակը նոր այլընտրանքի հետ (dp[n-coin] + 1)
                dp[n] = min(dp[n], dp[n - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

#############################################################

# Rod Cutting Problem (bottom-up)
# Time: O(n^2)
# Space: O(n)

def rod_cutting(prices:list[int]) -> int:
    n = len(prices) - 1
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i] = max(dp[i], prices[j] + dp[i - j])

    return dp[n]

###############################################################

# Activity Selector
def activity_selector(activities:list[tuple]) -> list[tuple]:
    """
    Ընտրում է առավելագույն քանակությամբ իրար չհամընկնող գործողություններ։
    activities: list of tuples -> [(սկիզբ, ավարտ), ...]
    """
    sorted_activities = sorted(activities, key=lambda x:x[1])

    selected_activities = [sorted_activities[0]]

    last_finish_time = sorted_activities[0][1]

    for i in range(1, len(sorted_activities)):
        current_start = sorted_activities[i][0]
        current_finish = sorted_activities[i][1]

        if current_start >= last_finish_time:
            selected_activities.append(sorted_activities[i])
            last_finish_time = current_finish

    return selected_activities

#########################################################################

def findLCA(root, p, q):
    # Base case: եթե հասել ենք դատարկ հանգույցի կամ գտել ենք տարրերից մեկը
    if root is None or root == p or root == q:
        return root

    # Փնտրում ենք ձախ և աջ ենթածառերում
    left = findLCA(root.left, p, q)
    right = findLCA(root.right, p, q)

    # Եթե երկու կողմից էլ ոչ-դատարկ արժեք է վերադարձել, 
    # նշանակում է ընթացիկ root-ը հենց մեր LCA-ն է
    if left and right:
        return root

    # Հակառակ դեպքում վերադարձնում ենք այն կողմը, որտեղ ինչ-որ բան գտնվել է
    return left if left is not None else right

#####################################################3