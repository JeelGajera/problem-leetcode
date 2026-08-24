import math

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        nsum = 0
        nproduct = 1
        num = n
        while num > 0:
            dig = num%10
            nsum += dig
            nproduct *= dig
            num //= 10

        res = nsum + nproduct
        if n % res == 0:
            return True
        else:
            return False
        