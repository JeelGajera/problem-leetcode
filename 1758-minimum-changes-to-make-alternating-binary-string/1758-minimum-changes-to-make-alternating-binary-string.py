class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        if n < 2: return 0
        res = 0
        for i in range(n):
            char = "0" if i % 2 == 0 else "1"
            if s[i] != char:
                res += 1
        return min(res, n-res)