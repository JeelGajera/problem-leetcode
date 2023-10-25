class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dic = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in num_dic:
                return [num_dic[comp],i]
            num_dic[num] = i
        return []