class Solution:
    def romanToInt(self, s: str) -> int:
        table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        for i,char in enumerate(s):
            tmp = table[char]
            if i + 1 < len(s) and table[s[i+1]] > tmp:
                res -= tmp
            else:
                res += tmp
        return res