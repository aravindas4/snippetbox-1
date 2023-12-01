class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
    def isMatch(self, A, B):
        N = len(A)
        M = len(B)

        dp = [[0] * (M+1) for _ in range(N+1)]
        pstar = [0 for _ in range(M)]

        for i in range(M):
            val = 0

            if B[i] == '*':
                val = 1

            if i != 0:
                val += pstar[i-1]

            pstar[i] = val

        print(pstar)
        for i in range(N+1):
            for j in range(M+1):
                # print(A[i-1], B[j-1])
                if i < 1:
                    a = "-"
                else:
                    a = A[i-1]
                
                if j < 1:
                    b = "-"
                else:
                    b = B[j-1]
                
                prev = dp[i-1][j-1]
                print(dp[i][j])
                if i == 0 and j == 0:
                    dp[i][j] = 1
                    print("1")
                elif i == 0 and j != 0 and B[j-1] == '*' and pstar[j-1] == j:
                    dp[i][j] = 1
                    print("2")
                elif i != 0 and j == 0:
                    dp[i][j] = 0
                elif A[i-1] == B[j-1] or B[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                    print("3")
                elif B[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                    print("4")
                print(a, b, dp[i][j], f"i={i}", f"j={j}", prev)

        # print(dp, pstar, N, M)
        return dp[N][M]
 
s = Solution()
# A = 'aa'
# B = 'a****'
# A = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
# B = 'a**************************************************************************************'
# A = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
# B = '*'
# A = 'aabbaaabbbaa'
# B = 'a*bbb*aaa'
# A = 'bcaccbabaa'
# B = 'bb*c?c*?'
A = 'cabbbac'
B = 'b*a*?*'
print(s.isMatch(A, B))