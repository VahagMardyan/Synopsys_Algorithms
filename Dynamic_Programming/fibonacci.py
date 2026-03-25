class Fib:
    def __init__(self, item:int):
        self.n = item
        self.memo = {}
        self.memo_list = []
    
    def naive(self, n:int = None) -> int:
        """
            Time complexity: O(2^n)\n
            Memory usage: O(1)
        """
        if n is None:
            n = self.n
        
        if n <= 1:
            return n
        
        return self.naive(n - 1) + self.naive(n - 2)
    
    def __memoization_helper__(self, n:int = None, memo:list = None) -> int:
        if n is None:
            n = self.n
        
        if memo is None:
            memo = self.memo_list

        if n <= 1:
            return n
        
        if memo[n] != -1:
            return memo[n]
        
        memo[n] = self.__memoization_helper__(n-1, memo) + self.__memoization_helper__(n-2, memo)
        return memo[n]

    def memoization(self, n:int = None):
        """
            Time complexity: O(n)
            Memory usage: O(n)
        """
        if n is None:
            n = self.n
            
        memo = [-1] * (n+1)
        return self.__memoization_helper__(n, memo)

    def tabulation(self, n:int = None):
        """
            Time complexity: O(n)\n
            Memory usage: O(n)
        """
        if n is None:
            n = self.n

        if n <= 1:
            return n
        self.memo_list = [-1] * (n+1)
        self.memo_list[0] = 0
        self.memo_list[1] = 1
        for i in range(2,n+1):
            self.memo_list[i] = self.memo_list[i-1] + self.memo_list[i-2]
        return self.memo_list[n]
    
    def __fast_doubling_helper__(self, n:int):
        if n == 0:
            return (0,1) # F(0), F(1)
        
        if n in self.memo:
            return self.memo[n]
        
        k = n // 2
        a, b = self.__fast_doubling_helper__(k)

        c = a * (2*b - a)
        d = a**2 + b**2

        if n % 2 == 0:
            self.memo[n] = (c,d)
            return (c,d)
        else:
            self.memo[n] = (d, c + d)
            return (d, c + d)
        
    def fast_doubling(self, n:int = None):
        """
            Time complexity: O(log(n))\n
            Memory usage: O(log(n))
        """
        if n is None:
            n = self.n

        res, _ = self.__fast_doubling_helper__(n)
        return res

    def is_fib(self, N:int) -> bool:
        n1 = (5 * N**2 + 4)**0.5
        n2 = (5 * N**2 - 4)**0.5

        return (n1 % 1 == 0) or (n2 % 1 == 0)

f = Fib(8)
print(f.naive())
print(f.memoization())
print(f.tabulation())
print(f.fast_doubling())