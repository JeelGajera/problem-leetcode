class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        total = sum(nums)
        for i in reversed(range(len(nums))):
            if i >= 2:
                total -= nums[i]
                if nums[i] < total:
                    return total + nums[i]
        return -1