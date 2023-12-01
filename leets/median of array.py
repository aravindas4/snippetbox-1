import sys

max_size = sys.maxsize

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        n1 = len(A)
        n2 = len(B)

        n_min = min(n1, n2)
        n_max = max(n1, n2)

        if n_min == 0:
            mid = n_max // 2

            if n1 > n2:
                arr = A
            else:
                arr = B
            
            if n_max & 1:
                return arr[mid] / 1
            else:
                return (arr[mid-1] + arr[mid]) / 2

            
        if n1 > n2:
            return self.findMedianSortedArrays(B, A)

        lhalf = (n1 + n2 + 1) // 2
        l = 0
        r = lhalf

        while l <= r:
            mid = (l + r) // 2

            c1 = min(mid, n1)
            c2 = lhalf - c1
            print(c1, c2, n1, n2)
            if c1 > 0:
                l1 = A[c1-1]
            else:
                l1 = -1 * max_size

            if c1 < n1:
                r1 = A[c1]
            else:
                r1 = max_size

            if c2 > 0:
                l2 = B[c2-1]
            else:
                l2 = -1 * max_size

            if c2 < n2:
                r2 = B[c2]
            else:
                r2 = max_size

            if l1 <= r2 and l2 <= r1:
                if (n1 + n2) & 1 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1, l2) / 1
            elif l1 > r2:
                r = mid - 1
            else:
                l = mid + 1

s = Solution()
A = [ -49, 33, 35, 42 ]
B = [-26]
# A = [ -43, -25, -18, -15, -10, 9, 39, 40 ]
# B = [-2]

print(s.findMedianSortedArrays(B, A))
