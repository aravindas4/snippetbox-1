class Solution:
    # @param A : list of list of integers
    def solve(self, A):
        N = len(A)
        for i in range(0, N-1):
            for j in range(i+1, N):
                temp = A[i][j]
                A[i][j] = A[j][i]
                A[j][i] = temp

        for i in range(0, N):
            left = 0
            right = N-1
            while left < right:
                temp = A[i][right]
                A[i][right] = A[i][left]
                A[i][left] = temp
                left += 1
                right -= 1
            
        return A

A = [[1,2],[3,4]]
s = Solution()
print(s.solve(A))