class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        N = len(A)

        output = [[ 0 for i in range(N)] for j in range (N * 2 - 1)]
        # print(output)
        rrow = 0
        for j in range(0, N):
            row = 0
            col = j
            rcol = 0
            while row < N and col >= 0:
                print("index=", (row, col))
                print("output=", (rrow, rcol))
                # print(output[rrow][rcol])
                output[rrow][rcol] = A[row][col]
                print(output)
                print("--------------")
                rcol += 1
                # print("rrow=", rrow, "rcol=", rcol)
                row += 1
                col -= 1
            rrow += 1

        for i in range(1, N):
            row = i
            col = N - 1
            rcol = 0
            while row < N and col >= 0:
                print("index=", (row, col))
                print("output=", (rrow, rcol))
                print(output)
                print("--------------")
                # print(A[row][col])
                output[rrow][rcol] = A[row][col]
                rcol += 1
                # print("rrow=", rrow, "rcol=", rcol)
                row += 1
                col -= 1
                # print(output)
            rrow +=1

        return output

A = [[1,2,3],[4,5,6],[7,8,9]] 
s = Solution()
print(s.diagonal(A))

