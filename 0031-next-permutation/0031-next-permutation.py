class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        lastInc = -1

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                lastInc = i

        if lastInc == -1:
            nums.reverse()
            return
        
        idx = lastInc
        for i in range(lastInc, n):
            if nums[i] > nums[lastInc-1] and nums[i]<nums[idx]:
                idx = i
                
        nums[lastInc-1], nums[idx] = nums[idx], nums[lastInc-1]
        nums[lastInc:] = sorted(nums[lastInc:])