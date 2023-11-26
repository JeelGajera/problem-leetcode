class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        area = 0
        n = len(heights)
        s = deque()
        for i in range(n):
            while(len(s) != 0 and heights[s[-1]] > heights[i]):
                popid = s.pop()
                if len(s) == 0:
                    area = heights[popid]*i
                else:
                    area = heights[popid]*(i - (s[-1]+1))

                result = max(result, area)

            s.append(i)
        
        while(len(s) != 0):
            popid = s.pop()
            if len(s) == 0:
                area = heights[popid]*n
            else:
                area = heights[popid]*(n - (s[-1]+1))

            result = max(result, area)

        return result