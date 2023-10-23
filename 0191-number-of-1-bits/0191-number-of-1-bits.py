class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(bin(n))
        bits = list(s)
        return bits.count('1')