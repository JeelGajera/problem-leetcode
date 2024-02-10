class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)

        def helper(l,r):
            while l >= 0 and r < n and (s[l] == s[r]):
                nonlocal res
                res += 1
                l -= 1
                r += 1

        for i in range(len(s)):
            helper(i,i) #odd str
            helper(i,i+1) #even str

        return res