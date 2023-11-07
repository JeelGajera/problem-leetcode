class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = [dist[i] / speed[i] for i in range(len(dist))]
        time.sort()
        cum_time = 0
        count = 1
        for i in range(1, len(time)):
            t = time[i]
            if t > cum_time + 1:
                count += 1
                cum_time += 1
            else:
                return count
        return count