import sys

sys.setrecursionlimit(10**6)

class Solution:
    # @param A : integer
    def solve(self, A):
        self.pprint(A)
        return ""

    def pprint(self, A):
        if A != 0:
            print(A, end=" ")
            self.pprint(A-1)

s = Solution()
print(s.solve(9))