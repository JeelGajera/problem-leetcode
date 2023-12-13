class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        r, c = len(mat), len(mat[0])
        trans_mat = [[mat[i][j] for i in range(r)] for j in range(c)]

        count = 0
        for i in range(r):
            for j in range(c):
                if sum(mat[i]) == 1 and sum(trans_mat[j]) == 1 and mat[i][j] == 1:
                    count += 1

        return count