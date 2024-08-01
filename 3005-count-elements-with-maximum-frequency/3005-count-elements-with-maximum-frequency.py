class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_freq = max(freq.values())
        val = list(freq.values()).count(max_freq)
        return val if count == 1 else val*max_freq