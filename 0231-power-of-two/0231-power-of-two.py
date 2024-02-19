class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 0
        a = 0
        while True:
            a = 2**x
            if a == n:
                return True
            elif a > n:
                return False
            x += 1