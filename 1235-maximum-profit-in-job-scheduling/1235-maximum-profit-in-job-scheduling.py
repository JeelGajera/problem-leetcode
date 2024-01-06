class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n = len(jobs)
        dp = [0]*n

        for i in range(n):
            dp[i] = jobs[i][2]
            if i == 0:
                continue
            
            prev_profit = 0
            low, high = 0, i - 1

            while low <= high:
                mid = (low + high) // 2
                if jobs[mid][1] <= jobs[i][0]:
                    prev_profit = dp[mid]
                    low = mid + 1
                else:
                    high = mid - 1

            dp[i] = max(dp[i], dp[i - 1], prev_profit + jobs[i][2])

            
        return max(dp)