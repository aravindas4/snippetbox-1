class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        N = len(A)
        maxe = A[N-1]
        output = [A[N-1]]
        
        for ind in range(N-2, -1, -1):
             if A[ind] > maxe:
                 output.append(A[ind])
                 maxe = A[ind]

        return output

s = Solution()
print(s.solve([16, 17, 4, 3, 5, 2]))