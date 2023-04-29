class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        # N = len(A), Q = len(Q)
        # TC: N + Q, SC: N + Q
        N = len(A)
        psum = [0] * N
        if A[0] % 2 == 0:
            psum[0] = 1

        for ind in range(1, N):
            if A[ind] % 2 == 0:
                psum[ind] = psum[ind - 1] + 1
            else:
                psum[ind] = psum[ind - 1]

        output = []
        for sub_arr in B:
            if sub_arr[0] == 0:
                count = psum[sub_arr[1]]
            else:
                count = psum[sub_arr[1]] - psum[sub_arr[0] - 1]

            output.append(count)

        return output
    
s = Solution()

print(s.solve([1, 2, 3, 4, 5], [[0, 2], [2, 4],[1, 4]]))
print(s.solve([2, 1, 8, 3, 9, 6], [[0, 3],[3, 5],[3, 5],[2, 4]]))