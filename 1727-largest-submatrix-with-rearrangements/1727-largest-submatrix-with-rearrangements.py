class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        row, column = len(matrix), len(matrix[0])
        area = 0

        # create prefix sum of histogram
        for r in range(1,row):
            for c in range(column):
                matrix[r][c] += matrix[r-1][c] if matrix[r][c] else 0

        # calculate area
        for r in range(row):
            matrix[r].sort(reverse=True)
            for c in range(column):
                area = max(area, (c+1)*matrix[r][c])
                
        return area