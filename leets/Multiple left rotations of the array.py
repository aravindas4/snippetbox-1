class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        N = len(A)

        def rotate(AA, left, right):
            print(left, right)
            while left < right:
                temp = AA[left]
                AA[left] = AA[right]
                AA[right] = temp

                left += 1
                right -= 1

            return AA

        A = rotate(A, 0, N-1)

        output = []
        for R in B:
            R = R % N
            C = [c for c in A]
            C = rotate(C, 0, N - R -1)
            C = rotate(C, N - R, N -1)
            output.append(C)
            print(C)

        return output

s = Solution()
A = [4,74,35,16,100,77,50,51,31,29,67,12,43,31,83,2,85,85,39,27,64,86,5]
B = [73,70,47,19,46,25,46,4,33,33,6,31,23,19,44,53,69,30,69,89,59,25,38,82,26,8,36,3]

print(s.solve(A, B))