class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        res = set()
        
        for i in freq.keys():
            if freq[i] == 2:
                res.add(i)

        return list(res)