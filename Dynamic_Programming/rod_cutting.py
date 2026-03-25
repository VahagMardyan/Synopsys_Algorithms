class RodCutting:
    """
    Given
        1. a rod of length n and
        2. an array of prices where i-th entry represents a price of a rod of length i+1.
        3. Find the maximum revenue obtainable by cutting up the rod and selling the pieces.
    """

    def __init__(self):
        self.memo = []

    def naive(self, length:int, prices:list):
        if length <= 0:
            return 0
        max_val = float('-inf')
        for i in range(1, length + 1):
            if i <= len(prices):
                res = prices[i-1] + self.naive(length - i, prices)
                if res > max_val:
                    max_val = res
        return max_val if max_val != float('-inf') else 0

    def __memoization_helper__(self, length:int, prices:list, memo:list = None):
        if length <= 0:
            return 0
        if self.memo[length] != -1:
            return self.memo[length]
        
        max_val = 0
        for i in range(1, length + 1):
            if i <= len(prices):
                max_val = max(max_val, prices[i - 1] + self.__memoization_helper__(length - i, prices))
        
        self.memo[length] = max_val
        return max_val

    def memoization(self, length:int, prices:list):
        self.memo = [-1] * (length + 1)
        self.memo[0] = 0
        return self.__memoization_helper__(length, prices, self.memo)

    def tabulation(self, length:int, prices:list):
        dp = [0] * (length + 1)

        for i in range(1, length + 1):
            max_val = 0
            for j in range(1, i+1):
                if j <= len(prices):
                    max_val = max(max_val, prices[j - 1] + dp[i - j])
            dp[i] = max_val

        return dp[length]
    

rc = RodCutting()
length = 5
prices = [1,5,8,9,10]

n = rc.naive(length, prices)
m = rc.memoization(length, prices)
t = rc.tabulation(length, prices)

print(f"naive: {n}", f"memoization: {m}", f"tabulation: {t}")