class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        freq = Counter(nums)
        sorted(freq, key=freq.get, reverse=True)
        for k, v in freq.items():
            if v > n/2:
                return k