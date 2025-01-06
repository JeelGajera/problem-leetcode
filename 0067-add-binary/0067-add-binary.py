class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ans = ''
        a = a.zfill(max(len(a), len(b)))
        b = b.zfill(max(len(a), len(b)))

        for i in range(len(a) - 1, -1, -1):
            bin_sum = int(a[i]) + int(b[i]) + carry
            ans += str(bin_sum%2)
            carry = bin_sum // 2
        
        if carry:
            ans += '1'

        return ans[::-1]