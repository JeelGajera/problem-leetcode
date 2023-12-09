class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posdiag = set()
        negdiag = set()
        q_pos = []
        result = []

        def bord(pos):
            pattern = []
            for r in range(n):
                row = ""
                for c in range(n):
                    if [r,c] in pos:
                        row += "Q"
                    else:
                        row += "."
                pattern.append(row)
            return pattern


        def backtrack(r):
            if r == n:
                result.append(bord(q_pos))
                return 
            
            for c in range(n):
                if c in col or (r+c) in posdiag or (r-c) in negdiag:
                    continue
                col.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
                q_pos.append([r,c])
                backtrack(r+1)
                col.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
                q_pos.remove([r,c])

        backtrack(0)
        return result
