class CoinChange:
    """
    Given a set of coin denominations and a target amount, determine the fewest number of coins needed to make up that amount.
    If there is no combination that can achieve the amount, return -1
    """

    def __init__(self, n:int):
        self.amount = n
        self.memo = []

    def __memoization_helper__(self, coins:list, amount:int = None, memo:list = None):
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')
        
        if memo[amount] != -1:
            return memo[amount]
        
        min_coins = float('inf')
        for coin in coins:
            res = self.__memoization_helper__(coins, amount-coin, memo)
            if res != float('inf'):
                min_coins = min(min_coins, res + 1)
        
        memo[amount] = min_coins
        return memo[amount]
    
    def coinChange_memoization(self, coins:list, amount:int = None):
        if amount is None:
            amount = self.amount
        self.memo = [-1] * (amount + 1)
        result = self.__memoization_helper__(coins, amount, self.memo)
        return result if result != float('inf') else -1

    def tabulation(self, coins:list, amount:int = None):
        if amount is None:
            amount = self.amount
        
        numCoins = [float('inf')] * (amount + 1)
        numCoins[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    numCoins[i] = min(numCoins[i], numCoins[i - coin] + 1)
        
        return numCoins[amount] if numCoins[amount] != float('inf') else -1


c = CoinChange(11)
coins = [1,2,5]
print(c.coinChange_memoization(coins))
print(c.tabulation(coins))