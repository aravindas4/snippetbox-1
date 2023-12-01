class Solution:
    # @param A : integer
    # @param B : long
    # @return an integer
    def solve(self, A, B):
        return self.pprint(A, B)

    def pprint(self, A, B):
        if B == 0:
            return 0
        
        return self.pprint(A, B // 2) ^ 1

s = Solution()
A = 4
B = 6
print(s.solve(A, Bnext_permutation.py
))