class Solution:
    def maxScore(self, s: str) -> int:
        max_cnt = 0
        for i in range(1,len(s)):
            max_cnt = max(max_cnt, (s[0:i].count('0')+s[i:].count('1')))
        return max_cnt