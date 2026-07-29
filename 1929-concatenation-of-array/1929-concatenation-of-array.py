class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # return nums + nums
        n = len(nums)
        ans = [0 for _ in range(2*n)]
        for i in range(2*n):
            if i >= n:
                ans[i] = nums[i-n]
            else:
                ans[i] = nums[i]
        return ans 