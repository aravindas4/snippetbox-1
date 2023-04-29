class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        psum = [0] * N
        psum[0] = A[0]

        for ind in range(1, N):
            psum[ind] = psum[ind-1] + A[0]

        for ind in range(0, N):
            if ind == 0:
                if 0 == (psum[N-1] - psum[ind]):
                    return ind
            else:
                if psum[ind - 1] ==  (psum[N-1] - psum[ind]):
                    return ind 
                
        return -1

s = Solution()
print(s.solve([ 1, 2, 3, 7, 1, 2, 3 ]))