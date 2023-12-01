import sys


# sys.setrecursionlimit(10**4)

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        self.xx = [0, 0, 1, -1]
        self.yy = [1, -1, 0, 0]
        self.A = A

        self.N = len(A)
        self.M = len(A[0])
        r_1 = None
        c_1 = None
        zeros = 0
        self.count = 0

        for i in range(self.N):
            for j in range(self.M):
                if A[i][j] == 1:
                    r_1 = i
                    c_1 = j
                elif A[i][j] == 0:
                    zeros += 1
        
        print(r_1, c_1, zeros)
        self.recur(r_1, c_1, zeros)
        return self.count

    def is_valid(self, r, c):
        if 0 <= r < self.N and 0 <= c < self.M and self.A[r][c] != -1:
            return True

        return False

    def recur(self, r, c, zeros):
        if self.A[r][c] == 2:
            print(r, c, zeros)
            if zeros == -1:
                self.count += 1
            return

        self.A[r][c] = -1

        for i in range(4):
            if self.is_valid(r+self.xx[i], c+self.yy[i]):
                # print(r+self.xx[i], c+self.yy[i], zeros-1)
                self.recur(r+self.xx[i], c+self.yy[i], zeros-1)
        
        self.A[r][c] = 0


s = Solution()
A = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
print(s.solve(A))