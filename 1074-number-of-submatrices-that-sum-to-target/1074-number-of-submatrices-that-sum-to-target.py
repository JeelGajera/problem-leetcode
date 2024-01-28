class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        row = len(matrix)
        col = len(matrix[0])
        sub_sum = [[0]*col for _ in range(row)]

        for r in range(row):
            for c in range(col):
                top = sub_sum[r-1][c] if r > 0 else 0
                left = sub_sum[r][c-1] if c > 0 else 0
                top_left = sub_sum[r-1][c-1] if min(r, c) > 0 else 0
                sub_sum[r][c] = matrix[r][c] + top + left - top_left
        
        res = 0
        for r1 in range(row):
            for r2 in range(r1, row):
                count = defaultdict(int)
                count[0] = 1
                for c in range(col):
                    cur_sum = sub_sum[r2][c] - (
                        sub_sum[r1-1][c] if r1 > 0 else 0
                    )
                    diff = cur_sum - target
                    res += count[diff]
                    count[cur_sum] += 1
        return res