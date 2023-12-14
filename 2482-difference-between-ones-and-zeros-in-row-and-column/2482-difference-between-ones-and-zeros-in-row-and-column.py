class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        trans = [[0]*rows for x in range(cols)]
        for i in range(rows):
            for  j in range(cols):
                trans[j][i] = grid[i][j]

        bin_row = [[grid[r].count(0), grid[r].count(1)] for r in range(rows)]
        bin_col = [[trans[c].count(0), trans[c].count(1)] for c in range(cols)]
        diff = [[0]*cols for x in range(rows)]
        for i in range(rows):
            for  j in range(cols):
                diff[i][j] = bin_row[i][1] + bin_col[j][1] - bin_row[i][0] - bin_col[j][0]

        return diff