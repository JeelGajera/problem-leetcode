class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq_hash = defaultdict(int)
        res = []       
        for i in nums:
            freq_hash[i] = nums.count(i)

        rows = max(freq_hash.values())

        for _ in range(rows):
            row = []
            for num, freq in freq_hash.items():
                if freq > 0:
                    row.append(num)
                    freq_hash[num] -= 1
            res.append(row)
            
        return res