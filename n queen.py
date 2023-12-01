class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        self.N = A
        cols = []
        for _ in range(A):
            cols.append(-1)

        self.output = []
        self.solve(0, cols)
        final = []
        # print(self.output)
        for cols in self.output:
            mat = []
            for col in cols:
                out = ["."] * self.N
                out[col] = 'Q'
                mat.append(''.join(out))
            final.append(mat)
            # print("mat", mat)

        # print(self.output)
        # if len(final):
        return final

    def solve(self, r, cols):
        N = self.N
        # print(r, N)
        if r == N:
            self.output.append(cols)
            return

        for c in range(N):
            # print(r, c, cols, self.is_valid(r, c, cols))
            if self.is_valid(r, c, cols):
                cols[r] = c
                self.solve(r+1, cols)
                cols[r] = -1
                

    def is_valid(self, row, col, cols):
        for r in range(row):
            c = cols[r]

            if c == -1:
                continue

            if r == row or c == col or r+c == col+row or row-r == col-c:
                return False 
            
        return True

s = Solution()
A = 1
print(s.solveNQueens(A))
