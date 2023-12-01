class Solution:
	# @param A : list of list of integers
	# @return an integer
    def uniquePathsWithObstacles(self, A):
        N = len(A)
        M = len(A[0])
        dp = [[0 for _ in range(M)] for __ in range(N)]

        for i in range(N):
            for j in range(M):
                if A[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[N-1][M-1]
    
s = Solution()
A = [[1,0]]
print(s.uniquePathsWithObstacles(A))