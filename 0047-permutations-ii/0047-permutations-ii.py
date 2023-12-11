class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def backtrack(i):
            if i == len(nums)-1:
                res.add(tuple(nums.copy()))
                return 
            
            seen = set()
            for idx in range(i,len(nums)):
                if nums[idx] in seen:
                    continue
                seen.add(nums[idx])

                nums[i], nums[idx] = nums[idx], nums[i]
                backtrack(i+1)
                nums[i], nums[idx] = nums[idx], nums[i]

        nums.sort()
        backtrack(0)
        return list(res)   