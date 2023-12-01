class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        last_i = 0 

        for i in range(30):
            if (1 << i) & A:
                last_i = i

        print(last_i)
        X = 1 << (last_i + 1)
        Y = 0
        print(X)
        for i in range(last_i+1):
            if (1 << i) & A == 0:
                Y = (1 << i) | Y
        print(Y)
        return X ^ Y
    
S = Solution()
print(S.solve(1))