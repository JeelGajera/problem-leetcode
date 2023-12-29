class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        
        dp = [[float('inf')]*n for _ in range(d)]
        dp[0][0] = jobDifficulty[0]

        for i in range(1, n):
            dp[0][i] = max(dp[0][i-1], jobDifficulty[i])
        

        for day in range(1, d):
            for job in range(day, n):
                max_difficulty = jobDifficulty[job]
                for k in range(job, day - 1, -1):
                    max_difficulty = max(max_difficulty, jobDifficulty[k])
                    dp[day][job] = min(dp[day][job], dp[day-1][k-1] + max_difficulty)
        
        return dp[d-1][n-1] if dp[d-1][n-1] != float('inf') else -1