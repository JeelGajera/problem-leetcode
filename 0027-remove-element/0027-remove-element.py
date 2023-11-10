class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = "_"
                
        for i in nums:
            if i == "_":
                nums.remove(i)
                nums.append(i)
                
        return int(len(nums) - nums.count("_"))