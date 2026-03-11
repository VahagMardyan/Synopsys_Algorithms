def radixsort(arr:list) -> list:
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

