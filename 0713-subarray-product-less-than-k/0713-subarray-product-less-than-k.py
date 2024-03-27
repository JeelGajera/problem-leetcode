class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        l, total = 0,1
        if k < 1: return 0
        for r, val in enumerate(nums):
            total *= val
            while total >= k and l <= r:
                total //= nums[l]
                l += 1
            res += r-l+1
        return res