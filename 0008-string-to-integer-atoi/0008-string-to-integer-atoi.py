class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        import re 

        pattern = r'^[+-]?\d+'
        match = re.search(pattern, s.strip())
        
        if match:
            result = int(match.group(0))
            INT_MIN, INT_MAX = -2**31, 2**31 - 1
            return max(min(result, INT_MAX), INT_MIN)
        else:
            return 0