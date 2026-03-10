class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[0]*n for n in range(1,numRows+1)]

        for j in range(numRows):
            for i in range(j+1):
                if i > 0 and i < j:
                    dp[j][i] = dp[j-1][i-1] + dp[j-1][i]
                else:
                    dp[j][i] = 1
        return dp