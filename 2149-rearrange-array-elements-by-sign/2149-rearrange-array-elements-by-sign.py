class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        pos = 0
        neg = 1
        for i in range(n):
            if nums[i]<0:
                res[neg]=nums[i]
                neg +=2
            else:
                res[pos]=nums[i]
                pos +=2

        return res