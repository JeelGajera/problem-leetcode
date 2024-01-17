class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)

        for i in freq.values():
            if list(freq.values()).count(i) > 1:
                return False

        return True