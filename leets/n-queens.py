from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        columns = set()
        negative_diagonals = set() # row + column
        positive_diagonals = set() # row -column

        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 

            for column in range(n):
                if (
                    column in columns 
                    or (row + column) in negative_diagonals 
                    or (row - column) in positive_diagonals
                ):
                    continue

                board[row][column] = "Q"
                columns.add(column)
                positive_diagonals.add(row - column)
                negative_diagonals.add(row + column)

                backtrack(row+1)

                # actual back tracking
                board[row][column] = "."
                columns.remove(column)
                positive_diagonals.remove(row - column)
                negative_diagonals.remove(row + column)

        backtrack(0)
        return res 

s = Solution()
print(s.solveNQueens(4))
