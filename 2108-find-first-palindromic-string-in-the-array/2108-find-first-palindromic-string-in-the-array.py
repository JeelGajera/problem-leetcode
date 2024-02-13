class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        pal = [x for x in words if x == x[::-1]]

        for s in words:
            if s in pal:
                return s

        return ""