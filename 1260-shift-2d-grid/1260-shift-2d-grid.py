class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        for x in range(k):
            matrix = [[0 for _ in range(cols)] for _ in range(rows)]
            for i in range(rows):
                for j in range(cols):
                    if (j+1 == cols and i < rows-1):
                        matrix[i+1][0] = grid[i][j]
                    elif j < cols-1:
                        matrix[i][j+1] = grid[i][j]

            matrix[0][0] = grid[rows-1][cols-1]
            grid = matrix

        return grid
