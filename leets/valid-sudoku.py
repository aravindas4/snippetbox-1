from typing import List,Set, Dict

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        fill = "."
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set) # key = (row//3, col//3)

        for row in range(9):
            for col in range(9):
                value = board[row][col]

                if value == fill:
                    continue

                if (
                    value in rows[row] 
                    or value in cols[col] 
                    or value in squares[(row // 3, col // 3)]
                ):
                    return False
        
                rows[row].add(value)
                cols[col].add(value)
                squares[(row // 3, col // 3)].add(value)

        return True

s = Solution()
board1 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(s.isValidSudoku(board1))

board2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(s.isValidSudoku(board2))