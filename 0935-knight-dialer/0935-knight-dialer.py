class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [1]*10 #initial one move possible for each num
        MOD = 10**9+7

        for i in range(n-1):
            tmp = dp.copy()

            dp[0] = tmp[4] + tmp[6]
            dp[1] = tmp[6] + tmp[8]
            dp[2] = tmp[7] + tmp[9]
            dp[3] = tmp[4] + tmp[8]
            dp[4] = tmp[3] + tmp[9] + tmp[0]
            dp[5] = 0 # no possible moves
            dp[6] = tmp[1] + tmp[7] + tmp[0]
            dp[7] = tmp[2] + tmp[6]
            dp[8] = tmp[1] + tmp[3]
            dp[9] = tmp[2] + tmp[4]

        res = sum(dp) % MOD
        return res 