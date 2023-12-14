class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # O(n2) solution :)
        # res = 0
        # for i in range(1, max(nums)+1):
        #     print(i)
        #     if i not in nums:
        #         res = i
        #         break
        #     else:
        #         res = i+1
        # return res            

        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1