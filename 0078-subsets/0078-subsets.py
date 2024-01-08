class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        set_size = pow(2, len(nums))
        n = len(nums)

        for i in range(set_size):
            tmp = []
            for j in range(n):
                if (i & (1 << j)) > 0:
                    tmp.append(nums[j])

            res.append(tmp)

        return res