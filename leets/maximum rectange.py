from collections import deque

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        m = len(A[0])
        print(n, m)

        for i in range(1, n):
            for j in range(m):
                if A[i][j] != 0:
                    A[i][j] += A[i-1][j]

        nsl = []
        nsr = []

        for i in range(n):
            ls = deque()
            nsl_row = []
            rs = deque()
            nsr_row = []

            for j in range(m):
                while len(ls) > 0 and A[i][ls[-1]] >= A[i][j]:
                    ls.pop()

                if len(ls) < 1:
                    nsl_row.append(-1)
                else:
                    nsl_row.append(ls[-1])

                ls.append(j)

            nsl.append(nsl_row)

            for j in range(m-1, -1, -1):
                while len(rs) > 0 and A[i][rs[-1]] >= A[i][j]:
                    rs.pop()

                if len(rs) < 1:
                    nsr_row.insert(0, m)
                else:
                    nsr_row.insert(0, rs[-1])

                rs.append(j)

            nsr.append(nsr_row)

        ans = -1
        print(A)
        print(nsl)
        print(nsr)
        for i in range(n):
            for j in range(m):
                ans = max(ans, A[i][j] * (nsr[i][j] - nsl[i][j]- 1))

        return ans

s = Solution()
A = [[0,1,1],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,1,1],[0,1,0]]
print(s.solve(A))