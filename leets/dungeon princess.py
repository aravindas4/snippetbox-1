class Solution:
	# @param A : list of list of integers
	# @return an integer
    def calculateMinimumHP(self, A):
        N = len(A)
        M = len(A[0])
        dp = [[0 for _ in range(M)] for __ in range(N)]

        for i in range(N-1, -1, -1):
            for j in range(M-1, -1, -1):
                if i == N-1 and j == M-1:
                    x = 1
                elif i == N-1:
                    x = dp[i][j+1]
                elif j == N-1:
                    x = dp[i+1][j]
                else:
                    x = min(dp[i][j+1], dp[i+1][j])

                dp[i][j] = max(1, x - A[i][j])

        print(dp)
        return dp[0][0]

s = Solution()
A = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
print(s.calculateMinimumHP(A))
