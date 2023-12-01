class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()
        print(A)
        N = len(A)
        count = 0

        l = 0; r = 1
        while r < N:
            d = A[r] - A[l]

            if d == B:
                count += 1
                if A[r] == A[l]:
                    right = A[r]
                    # count = c * (c-1) // 2
                    while r < N and right == A[r]:
                        r += 1
                    l = r - 1
                else:
                    left = A[l]
                    lc = 0
                    right = A[r]
                    rc = 0

                    while l <= r and left == A[l]:
                        l += 1

                    while r < N and right == A[r]:
                        r += 1

                    # count += (rc * lc)
            elif d > B:
                l += 1
                if l == r:
                    r += 1
            else:
                r += 1
        return count

# A = [8,5,1,10,5,9,9,3,5,6,6,2,8,2,2,6,3,8,7,2,5,3,4,3,3,2,7,9,6,8,7,2,9,10,3,8,10,6,5,4,2,3]
A = [1,1,1,2,2]
s = Solution()
print(s.solve(A, 0))