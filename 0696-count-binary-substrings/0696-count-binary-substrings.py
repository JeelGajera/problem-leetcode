class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        if n < 2 : return 0
        prev_group = 0
        curr_group = 1
        total = 0
        for i in range(1,n):
            if s[i] == s[i-1]:
                curr_group += 1
            else:
                total += min(prev_group, curr_group)
                prev_group = curr_group
                curr_group = 1
        
        total += min(prev_group, curr_group)
        return total
        