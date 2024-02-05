class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        for i in s:
            if freq[i] == 1:
                return s.index(i)
        return -1