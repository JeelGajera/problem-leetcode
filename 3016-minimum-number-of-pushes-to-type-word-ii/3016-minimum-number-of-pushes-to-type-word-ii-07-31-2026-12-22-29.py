class Solution:
    def minimumPushes(self, word: str) -> int:
        freq_map = {}
        for i in word:
            if i not in freq_map:
                freq_map[i] = 1
            else:
                freq_map[i] += 1

        ops = sorted(freq_map.values(),reverse=True)
        res = 0
        for i in range(len(ops)):
            res += ops[i] * (i//8 + 1)
        
        return res