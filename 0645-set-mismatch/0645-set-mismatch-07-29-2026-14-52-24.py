class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        duplicate = missing = -1
        for i in nums:
            if i in seen:
                duplicate = i
                break
            seen.add(i)

        for i in range(1, len(nums) + 1):
            if i not in nums:
                missing = i
                break
        return [duplicate, missing]
