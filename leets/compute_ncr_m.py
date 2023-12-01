class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        n = A 
        r = B
        m = C 

        ncr = [[0 for _ in range(r+1)] for __ in range(n+1)]

        for i in range(n+1):
            ncr[i][0] = 1

        # print(ncr)
        for i in range(1, n+1):
            for j in range(1, r+1):
                # print(ncr[i-1][j], ncr[i-1][r-1])
                ncr[i][j] = (ncr[i-1][j] + ncr[i-1][j-1]) % m

        print(ncr)
        return ncr[n][r]
    
s = Solution()
print(s.solve(5, 2, 13))