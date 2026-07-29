class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = pt = 0
        for i in nums:
            if i == 1:
                pt+=1
            else:
                res = max(res, pt)
                pt = 0
        return max(res, pt)