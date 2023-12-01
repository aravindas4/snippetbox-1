import sys

sys.setrecursionlimit(10 ** 5)

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        nf = 1
        for i in range(1, A+1):
            nf = (nf * i) % C

        nmrf = 1
        for i in range(1, A - B+ 1):
            nmrf = (nmrf * i) % C 

        rf = 1
        for i in range(1, B+1):
            rf = (rf * i) % C 

        a = self.fast_power(nmrf, C-2, C)
        b = self.fast_power(rf, C-2, C)
        return (((b * a) % C) * nf) % C

    def fast_power(self, A, B, P):
        res = 1

        while B > 0:
            if B % 2 == 1:
                res = ((res % P) * (A % P)) % P

            A = ((A % P) * (A % P)) % P 
            B = B // 2

        return res

s = Solution()
print(s.solve(969139, 832819, 1000000007))