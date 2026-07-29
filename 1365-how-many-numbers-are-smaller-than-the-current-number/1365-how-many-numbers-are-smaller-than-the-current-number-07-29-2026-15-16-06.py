class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num_map = {}
        idx = 0
        for i in sorted(nums):
            if num_map.get(i) is None:
                num_map[i] = idx
            idx += 1

        res = []
        for i in nums:
            res.append(num_map.get(i))
        return res