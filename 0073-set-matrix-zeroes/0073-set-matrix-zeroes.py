class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows=set()
        cols=set()
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col]==0:
                    rows.add(row)
                    cols.add(col)

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if row in rows or col in cols:
                    matrix[row][col]=0
                

        