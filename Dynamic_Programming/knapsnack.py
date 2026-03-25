class KnapSnack:
    """
        Given a set of items, each with
            1. a weight and
            2. a value,
            3. determine which items to include in a knapsack so that
            4. the total weight does not exceed a given capacity, and
            5. the total value is as large as possible.
            6. Each item can be included at most once.
    """

    def __init__(self):
        pass

    def naive(self, weights:list, values:list, cap:int, n:int = None):
        if n is None:
            n = len(weights)
        if n == 0 or cap == 0:
            return 0
        if weights[n-1] > cap:
            return self.naive(weights, values, cap, n-1)
        return max(
            values[n-1] + self.naive(weights, values, cap - weights[n-1], n-1),
            self.naive(weights, values, cap, n-1)
        )
    
    def memoization(self, weights:list, values:list, cap:int):
        n = len(weights)
        memo = [[-1 for _ in range(cap + 1)] for _ in range(n + 1)]
        return self.__memo_helper__(weights, values, cap, n, memo)
    
    def __memo_helper__(self, weights:list, values:list, cap:int, n:int, memo):
        if n == 0 or cap == 0:
            return 0
        if memo[n][cap] != -1:
            return memo[n][cap]
        
        if weights[n-1] <= cap:
            memo[n][cap] = max(
                values[n-1] + self.__memo_helper__(weights, values, cap - weights[n-1], n-1, memo),
                self.__memo_helper__(weights, values, cap, n-1, memo)
            )
        else:
            memo[n][cap] = self.__memo_helper__(weights, values, cap, n-1, memo)
        
        return memo[n][cap]
    
    def tabulation(self, weights:list, values:list, capacity:int):
        n = len(weights)
        dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
        for i in range(1, n+1):
            for w in range(1, capacity + 1):
                if weights[i - 1] <= w:
                    dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
                else:
                    dp[i][w] = dp[i-1][w]
        return dp[n][capacity]
    
ks = KnapSnack()
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

print(f"Max Value (Naive): {ks.naive(weights, values, capacity)}")
print(f"Max Value (Memo): {ks.memoization(weights, values, capacity)}")
print(f"Max Value (Tabu): {ks.tabulation(weights, values, capacity)}")