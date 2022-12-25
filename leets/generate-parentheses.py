from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Add ( if open < n
        # Add ) if closed < open
        # return if open = closed = n
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN=openN + 1, closedN=closedN)
                stack.pop() # backtracking

            if closedN < openN:
                stack.append(")")
                backtrack(openN=openN, closedN=closedN + 1)
                stack.pop() #backtracking

        backtrack(openN=0, closedN=0)
        return res

s = Solution()
print(len(s.generateParenthesis(n=6)))