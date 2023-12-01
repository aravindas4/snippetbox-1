class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):
        l = 1
        r = 0
        mod = 10000003

        for i in C:
            r += i

        r = r * B

        ans = r

        while l <= r:
            mid = l + (r-l) // 2
            pmid = self.check_painters(mid, B, C)
            print(l, r, mid, pmid)

            if pmid == A:
                ans = mid
                r = mid - 1
            elif pmid == -1:
                l = mid + 1
            elif pmid < A:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans % mod

    def check_painters(self, X, T, A):
        count = 1
        TL = X

        for i in A:
            TR = i * T
            if TR > X:
                return -1

            if TR <= TL:
                TL -= TR
            else:
                count += 1
                TL = X - TR

        return count
    

s = Solution()
A = 4
B = 10
C = [884,228,442,889]
# A = 2
# B = 2
# C = [5,3,6,1,9]
print(s.paint(A, B, C))