class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        pal = [x for x in words if x == x[::-1]]

        return pal[0] if len(pal) > 0 else ""