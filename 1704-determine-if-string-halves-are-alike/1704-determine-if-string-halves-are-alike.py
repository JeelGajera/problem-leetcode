class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        cnt1, cnt2 = 0, 0
        n = len(s)
        a = s[:n//2]
        b = s[n//2:]
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in range(n//2):
            if a[i] in vowels:
                cnt1 += 1

            if b[i] in vowels:
                cnt2 += 1

        return cnt1 == cnt2
            