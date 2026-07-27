class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if len(nums) == 2:
            return (nums[0]-1)*(nums[1]-1)

        mini_max, max_num = 0,0
        if nums[0] > nums[1]:
            max_num = nums[0]
            mini_max = nums[1]
        else:
            max_num = nums[1]
            mini_max = nums[0]

        for i in range(2,len(nums)):
            if nums[i] > max_num:
                mini_max = max_num
                max_num = nums[i]
            elif nums[i] > mini_max:
                mini_max = nums[i]

        return (mini_max-1)*(max_num-1)