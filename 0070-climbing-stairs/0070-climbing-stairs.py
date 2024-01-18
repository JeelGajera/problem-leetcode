class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 2] + [0]*(n-1)
        if n == 1:
            return 1
        if n == 2:
            return 2

        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]

        print(dp)
        return dp[n-1]