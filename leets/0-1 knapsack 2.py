import sys

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        N = len(A)
        max_val = sum(A)
        dp = [sys.maxsize for _ in range(max_val+1)]
        dp[0] = 0
        
        for i in range(N):
            for j in range(max_val, A[i]-1, -1):
                print(i, j, A[i], dp[j], B[i]+dp[j-A[i]])
                dp[j] = min(dp[j], B[i]+dp[j-A[i]])

        # print(dp)
        for idx in range(max_val, -1, -1):
            if dp[idx] <= C:
                break

        print(dp)
        return idx
    
s = Solution()
# A = [1, 3, 2, 4]
# B = [12, 13, 15, 19]
# C = 10
A = [6, 10, 12]
B = [10, 20, 30]
C = 50
print(s.solve(A, B, C))