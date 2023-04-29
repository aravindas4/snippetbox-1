class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        # TC: N, SC: N
        N = len(A)
        prefix = [1] * N
        postfix = [1] * N 

        prefix[0] = A[0]
        for ind in range(1, N):
            prefix[ind] = prefix[ind-1] * A[ind]

        postfix[N-1] = A[N-1]
        for ind in range(N-2, -1, -1):
            postfix[ind] = postfix[ind+1] * A[ind]

        output = []
        for ind in range(0, N):
            if ind == 0:
                pr = 1
            else:
                pr = prefix[ind-1]

            if ind == N -1:
                po = 1
            else:
                po = postfix[ind+1]

            output.append(pr * po)

        return output
    
s = Solution()
print(s.solve([1, 2, 3, 4, 5]))
print(s.solve([5, 1, 10, 1]))