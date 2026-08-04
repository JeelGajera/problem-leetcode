class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        idx = 0
        res = []
        for i in range(nums[0],nums[-1]):
            if nums[idx] != i:
                res.append(i)
                idx -= 1
            idx += 1
        return res