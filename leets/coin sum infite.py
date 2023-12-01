class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
    def coinchange2(self, A, B):
        dp = [0 for _ in range(B+1)]
        dp[0] = 1
        N = len(A)

        for i in range(1, B+1):
            for j in range(N):
                if i >= A[j]:
                    print(i, A[j], dp[i-A[j]], dp[i])
                    dp[i] = dp[i] + dp[i-A[j]]
                    print(dp)

        print(dp)
        return dp[B]

s = Solution()
A = [1,2,3]
B = 4
# A = [10]
# B = 10
print(s.coinchange2(A, B))