class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        ni = len(A)
        dp = [[0] * (C+1) for _ in range(ni+1)]

        for i in range(1, ni+1):
            for j in range(1, C+1):
                dp[i][j] = dp[i-1][j]
                if j - B[i-1] >= 0:
                    dp[i][j] = max(dp[i][j], A[i-1]+dp[i-1][j-B[i-1]])

        print(dp)
        return dp[ni][C]
    
A = [504,449,201,459,619,581,797,799,282,590,799,10,158,473,623]
B = [39,93,39,80,91,58,59,92,16,89,57,12,3,35,73]
C = 56
s = Solution()
print(s.solve(A, B, C))