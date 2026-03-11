def countsort(arr:list) -> list:
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

# arr = [2, 5, 3, 0, 2, 2, 3, 0, 3]
# ans = countsort(arr)
# print(ans)
