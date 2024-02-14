class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        cols = n//rows
        grid = [[0]*cols for _ in range(rows)]
        i = 0
        for r in range(rows):
            for c in range(cols):
                grid[r][c] = encodedText[i]
                i += 1

        res = ""
        i, row, col = 0, 0, 0
        for _ in range(n):
            if row == rows:
                i += 1
                row = 0
                col = i

            res += grid[row][col] if row < rows and col < cols else ""
            row += 1
            col += 1
        
        return res.rstrip()