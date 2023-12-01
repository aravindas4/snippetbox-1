class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        dp = [0 for _ in range(N+1)]
        print(dp)

        for i in range(1, N+1):
            for j in range(1, i+1):
                print(i, j)
                dp[i] = max(dp[i], A[j-1]+dp[i-j])

        return dp[N]
    
s = Solution()
A = [3, 4, 1, 6, 2]
print(s.solve(A))