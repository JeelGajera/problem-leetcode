class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(1,n-1,3):
            prev, curr, next = nums[i-1], nums[i], nums[i+1]
            if abs(prev - curr) <= k and abs(curr - next) <= k and abs(prev - next) <= k:
                res.append([prev, curr, next])
        
        return res if len(res) == n//3 else []
