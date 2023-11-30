import math

class Solution:
    def mySqrt(self, x: int) -> int:
        # res = n^1/2
        # log(res) = 1/2*(lon(n))
        # res = Antilog(1/2*(lon(n))) --> 10**1/2*(lon(n))
        if x == 0 or x == 1:
            return x
        return int(10**((math.log10(x))/2))