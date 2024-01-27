class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD =  10**9 + 7
        prev = [0]*(k+1)
        prev[0] = 1
        
        for i in range(1, n+1):
            cur = [0]*(k+1)
            total = 0
            for j in range(0,k+1):
                if j >= i:
                    total -= prev[j-i]
                total = (total + prev[j]) % MOD
                cur[j] = total
            prev = cur
        return prev[k]