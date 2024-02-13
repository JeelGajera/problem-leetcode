class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        def isPalindrom(s):
            return s == s[::-1]

        for s in words:
            if isPalindrom(s):
                return s

        return ""