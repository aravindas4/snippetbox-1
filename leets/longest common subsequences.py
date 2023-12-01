import sys

sys.setrecursionlimit = 10**9

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        M = len(B)
        s1 = A 
        s2 = B
        dp = [[0] * (M+1) for _ in range(N+1)]

        for i in range(N+1):
            for j in range(M+1):
                ans = 0

                if i > 0 and j > 0:
                    if s1[i-1] == s2[j-1]:
                        ans = 1 + dp[i-1][j-1]
                    else:
                        v1 = dp[i-1][j]
                        v2 = dp[i][j-1]
                        ans = max(v1, v2)
                
                dp[i][j] = ans 

        print(dp)
        return dp[N][M]

A = 'bebdeeedaddecebbbbbabebedc'
B = 'abaaddaabbedeedeacbcdcaaed'
s = Solution()
print(s.solve(A, B))