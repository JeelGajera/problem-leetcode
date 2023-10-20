class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        def counter(b):
            c = 0
            for i in str(b):
                if i == '1':
                    c += 1
            return c

        for i in range(0,n+1):
            b = bin(i)
            res.append(counter(b))

        return res