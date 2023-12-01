class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        N = len(A)
        row = N
        col = len(A[0])
        R = [[0 for _ in range(row)] for __ in range(col)]
    
        for i in range(row):
            for j in range(col):
                R[j][i] = A[i][j]

        return R

# A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
A = [[2,3,6,7],[2,3,4,5]]
s = Solution()
print(s.solve(A))