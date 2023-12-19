class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        res = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                total, cnt = 0,0
                for i in range(max(0, r-1), min(rows, r+2)):
                    for j in range(max(0, c-1), min(cols, c+2)):
                        total += img[i][j]
                        cnt += 1
                res[r][c] = (total//cnt)
        return res