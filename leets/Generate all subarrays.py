class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def solve(self, A):
        output = []
        N = len(A)
        for i in range(0, N):
            sub = []
            for j in range(i, N):
                sub.append(A[j])
            output.append(sub)
        print(len(output))
        return output
    
s = Solution()

# A= [36,63,63,26,87,28,77,93,7]
A =  [1, 2, 3]
print(s.solve(A))