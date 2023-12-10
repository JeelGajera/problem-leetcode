class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r = len(matrix)
        c = len(matrix[0])
        trans = [[0]*r for x in range(c)]
        for i in range(r):
            for  j in range(c):
                trans[j][i] = matrix[i][j]

        return trans