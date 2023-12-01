class Solution:
    # @param A : string
    # @return a strings

    def solve(self, A):
        N = len(A)
        S = ""
        temp = ""
        for ind in range(N-1, -1, -1):
            if A[ind] != " ":
                temp = A[ind] + temp
            else:
                if len(temp) > 0:
                    S += temp
                    temp = ""

        return S

a = "hv xdq op qoddptokkz vemmoxrgf ombt gg crulgzfkif"
S = Solution()
print(S.solve(a))
