class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        cnt, res = 0, 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                cnt += 1
            else:
                res += (cnt*(cnt + 1))//2
                cnt = 0

        return res + (cnt * (cnt + 1))//2