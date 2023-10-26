class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        dp = {x:1 for x in arr}
        for i in arr:
            for j in arr:
                if i == j:
                    break
                if i % j == 0 and i // j in dp:
                    dp[i] += dp[j] * dp[i // j]
        return sum(dp.values()) % (pow(10,9) + 7)        