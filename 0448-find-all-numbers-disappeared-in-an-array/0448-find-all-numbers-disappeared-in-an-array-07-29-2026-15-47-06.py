class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = set([x for x in range(1, len(nums)+1)])
        for i in nums:
            if i in res:
                res.remove(i)
        return [*res]