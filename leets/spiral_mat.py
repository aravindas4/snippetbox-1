class Solution:
	# @param A : integer
	# @return a list of list of integers
    def generateMatrix(self, A):
        mat = [[0 for _ in range(A)] for _ in range(A)]
        C = 1
        N = A
        i = 0; j= 0
        while N > 1:
            for _ in range(1, N):
                mat[i][j] = C 
                C += 1
                j += 1
            for _ in range(1, N):
                mat[i][j] = C 
                C += 1
                i += 1
            for _ in range(1, N):
                mat[i][j] = C 
                C += 1
                j -= 1
            for _ in range(1, N):
                mat[i][j] = C 
                C += 1
                i -= 1
            
            i += 1
            j += 1
            N -= 2

        if N == 1:
            mat[i][j] = C 

        return mat
A = 5
s = Solution()
print(s.generateMatrix(A))