class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        p = s[::-1]
        prefix = ""
        n = len(s)
        for i in range(n):
            a = s[0:n-i]
            b = p[i:]
            if a != b:
                prefix += a[-1]
            else:
                break
        return prefix+s