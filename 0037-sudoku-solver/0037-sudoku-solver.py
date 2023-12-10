class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    num = int(board[r][c])
                    rows[r].add(num)
                    cols[c].add(num)
                    grids[r//3 * 3 + c//3].add(num)

        def backtrack(r,c):
            nonlocal solved
            if r == 9:
                solved = True
                return

            new_r = r + (c+1)//9
            new_c = (c+1) % 9

            if board[r][c] != ".":
                backtrack(new_r, new_c)
            else:
                grid_idx = r//3 * 3 + c//3
                for num in range(1,10):
                    if (num not in rows[r]) and (num not in cols[c]) and (num not in grids[grid_idx]):
                        rows[r].add(num)
                        cols[c].add(num)
                        grids[grid_idx].add(num)
                        board[r][c] = str(num)

                        backtrack(new_r, new_c)

                        if not solved:
                            rows[r].remove(num)
                            cols[c].remove(num)
                            grids[grid_idx].remove(num)
                            board[r][c] = "."

        solved = False
        backtrack(0,0)