class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort(key=lambda x:x[1])
        n = len(rides)
        dp = [0]*n
        for i in range(n):
            fair = rides[i][1] - rides[i][0] + rides[i][2]
            dp[i] = fair
            if i == 0:
                continue
            
            prev_fair = 0
            lo, hi = 0, i-1
            while lo <= hi:
                mid = (lo+hi)//2
                if rides[mid][1] <= rides[i][0]:
                    prev_fair = dp[mid]
                    lo = mid + 1
                else:
                    hi = mid - 1

            dp[i] = max(dp[i], dp[i-1], prev_fair + fair)

        return max(dp)