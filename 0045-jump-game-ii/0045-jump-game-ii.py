class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        jump = 0
        cur = 0
        next = 0

        for i in range(n-1):
            next = max(next, i+nums[i])
            if i == cur:
                jump += 1
                cur = next
        
        return jump