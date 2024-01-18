class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasks_freq = Counter(tasks)
        res = 0

        for freq in tasks_freq.values():
            if freq == 1:
                return -1
            
            res += math.ceil(freq/3)

        return res