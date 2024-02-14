class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [x for x in nums if x >= 0]
        neg = [y for y in nums if y < 0]
        res = []
        for i in range(len(nums)//2):
            res.append(pos[i])
            res.append(neg[i])

        return res