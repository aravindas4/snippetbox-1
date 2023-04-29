class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        pre_sum = [0] * len(A)
        pre_sum[0] = A[0]

        for ind in range(1, len(A)):
            pre_sum[ind] = pre_sum[ind - 1] + A[ind]
        output = []
        for s_b in B:
            if s_b[0] == 0:
                s = pre_sum[s_b[1]]
            else:
                s = pre_sum[s_b[1]] - pre_sum[s_b[0] - 1]
            output.append(s)

        return output


s = Solution()

print(s.solve([ 6, 3, 3, 6 ], [[0, 3], [0, 2]]))