class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        power = []
        x = 0
        while x < n:
            a = 2**x
            if a <= n:
                power.append(a)
            else:
                break
            x += 1
        return n in power