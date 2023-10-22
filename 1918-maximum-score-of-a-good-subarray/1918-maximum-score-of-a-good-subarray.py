class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = nums[k]
        mini = nums[k]
        i,j = (k,k)
        n = len(nums)
        while ( i > 0 or j < n-1):
            if i == 0:
                j += 1
            elif j == (n-1):
                i -= 1
            elif nums[i-1] < nums[j+1]:
                j += 1
            else:
                i -= 1
            mini = min(mini, min(nums[i], nums[j]))
            res = max(res, mini*(j-i+1))
        return res