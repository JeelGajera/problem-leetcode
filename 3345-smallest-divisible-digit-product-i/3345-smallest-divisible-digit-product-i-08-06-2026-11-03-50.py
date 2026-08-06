class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def getProductOfDigit(x: int) -> int:
            res  = 1
            while x != 0:
                res = res * (x % 10)
                x = x // 10
            return res

        while n <= 100:
            if getProductOfDigit(n) % t  == 0:
                break
            n += 1
        
        return n