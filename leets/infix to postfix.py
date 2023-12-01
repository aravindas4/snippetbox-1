from collections import deque

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        s = deque()
        ops = {"^": 3, "*": 2, "/": 2, "+": 1, "-": 1}
        op = ""

        for ele in A:
            if ele in ops.keys():
                if len(s) < 1 or s[-1] == "(":
                    s.append(ele)
                elif s[-1] in ops.keys():
                    while len(s) > 0 and s[-1] in ops.keys() and ops[s[-1]] >= ops[ele]:
                        op += s.pop()
                    s.append(ele)
            elif ele == '(':
                s.append(ele)
            elif ele == ')':
                while s[-1] != '(':
                    op += s.pop()
                s.pop()
            else:
                op += ele 

        while len(s) > 0:
            op += s.pop()

        return op

s = Solution()
print(s.solve("x^y/(a*z)+b"))
print(s.solve("a+b*(c^d-e)^(f+g*h)-i"))