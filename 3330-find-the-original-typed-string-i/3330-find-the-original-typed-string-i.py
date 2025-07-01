class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 1
        freq = 1
        for i in range(len(word)-1):
            if word[i] == word[i+1]:
                freq += 1
            else:
                res += freq-1
                freq = 1
        return res + freq - 1


