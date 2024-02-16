class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        res = len(freq)

        for i in sorted(freq.values()):
            if k >= i:
                k -= i
                res -= 1
            else:
                break

        return res
