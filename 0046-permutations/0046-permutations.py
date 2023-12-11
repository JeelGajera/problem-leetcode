class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def backtrack(i):
            if i == len(nums)-1:
                res.add(tuple(nums.copy()))
                return 
            
            for idx in range(len(nums)):
                nums[i], nums[idx] = nums[idx], nums[i]
                backtrack(i+1)
                nums[i], nums[idx] = nums[idx], nums[i]

        backtrack(0)
        return list(res)       