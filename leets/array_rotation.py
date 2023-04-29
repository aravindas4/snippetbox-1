class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):

        N = len(A)

        B = B % N

        def reverse(A, si, ei):
            i = si 
            j = ei 

            while i < j:
                temp = A[i]
                A[i] = A[j]
                A[j] = temp 

                i += 1
                j -= 1

            return A 

        reverse(A, 0 , N -1)
        print(A)
        reverse(A, 0, B -1)
        print(A)
        reverse(A, B, N - 1)
        print(A)

        return A
    
s = Solution()

print(s.solve([ 1, 1, 4, 9, 4, 7, 1 ], 9))