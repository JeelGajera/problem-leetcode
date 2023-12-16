class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0]*cols
        dp[cols-1] = 1
        for i in reversed(range(rows)):
            for j in reversed(range(cols)):
                if obstacleGrid[i][j]:
                    dp[j] = 0
                elif j+1 < cols:
                    dp[j] = dp[j+1] + dp[j] 
        
        return dp[0]