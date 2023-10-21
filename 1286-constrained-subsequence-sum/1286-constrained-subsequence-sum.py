class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import deque

        n = len(nums)
        
        dq = deque()
        maxSum = float('-inf')
        for i in range(n):
            while dq and dq[0][1] < i - k:
                dq.popleft()

            currentMax = 0 if not dq else dq[0][0]
            
            dp = max(currentMax, 0) + nums[i]
            
            maxSum = max(maxSum, dp)
            
            while dq and dp >= dq[-1][0]:
                dq.pop()
            
            dq.append((dp, i))
        
        return maxSum