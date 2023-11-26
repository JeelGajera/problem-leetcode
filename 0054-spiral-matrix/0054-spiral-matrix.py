class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        fill_num = 1
        def_val = "*"
        row, col = len(matrix), len(matrix[0])
        result = []

        # <-- Number of outer borders -->
        var_rc = min(col, row)
        num_border = 0
        if var_rc % 2 == 0:
            num_border = int(var_rc/2)
        else:
            num_border =  int(var_rc//2 + 1)

        # <-- Traverse Direction functions -->
        def toRight(col, vr_row=0):
            for i in range(col):
                if matrix[vr_row][i] != def_val:
                    result.append(matrix[vr_row][i])
                    matrix[vr_row][i] = def_val

        def toDown(row, vd_col=col-1):
            for i in range(row):
                if matrix[i][vd_col] != def_val:
                    result.append(matrix[i][vd_col])
                    matrix[i][vd_col] = def_val

        def toLeft(col, vl_row=row-1):
            for i in range(col-1, -1, -1):
                if matrix[vl_row][i] != def_val:
                    result.append(matrix[vl_row][i])
                    matrix[vl_row][i] = def_val

        def toUp(row, vu_col=0):
            for i in range(row-1, -1, -1):
                if matrix[i][vu_col] != def_val:
                    result.append(matrix[i][vu_col])
                    matrix[i][vu_col] = def_val
       

        # <-- Traverse Driver code -->
        vr_row, vd_col, vl_row, vu_col = 0, col-1, row-1, 0
        for t in range(num_border):
            toRight(col, vr_row)
            vr_row += 1
            toDown(row, vd_col)
            vd_col -= 1
            toLeft(col, vl_row)
            vl_row -= 1
            toUp(row, vu_col)
            vu_col += 1

        return result