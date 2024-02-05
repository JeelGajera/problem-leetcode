class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        arr = sorted(freq.keys(), key=freq.get, reverse=True)
        res = ""
        for i in arr:
            res += i*freq[i]

        return res