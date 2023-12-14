class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        i = 0
        while i < n-1:
            current_start, current_end = intervals[i]
            next_start, next_end = intervals[i + 1]
            if current_end >= next_start:
                intervals[i] = [current_start, max(current_end, next_end)]
                intervals.pop(i + 1)
                n -= 1
            else:
                i += 1
        return intervals
