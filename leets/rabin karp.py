class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def hashcode(self, S, start, end, mod):
        power = 1
        ans = 0
        print(start, end)
        for i in range(end, start-1, -1):
            print(power * ord(S[i]))
            ans = (ans + power * ord(S[i])) % mod
            power *= 26

        return ans % mod

    def solve(self, A, B):
        N = len(A)
        M = len(B)
        mod = (10 ** 9) + 7
        ans = 0

        hb = self.hashcode(B, 0, M-1, mod)
        ha = self.hashcode(A, 0, M-1, mod)
        print(hb, ha)
        if ha == hb:
            ans += 1

        p = 26
        lp = self.fastpower(p, M-1, mod)
        for i in range(M, N):
            ha = ((ha - (ord(A[i-M]) * lp)) * p + ord(A[i])) % mod

            if ha == hb:
                ans += 1

        return ans

    def fastpower(self, N, P, M):
        """(N ** P) % M"""

        if P == 0:
            return 1

        ir = self.fastpower(N, P//2, M)

        r = (ir * ir) % M 

        if P & 1:
            r = (r * N) % M 

        return r

s = Solution()
A = 'ccccba'
B = 'cc'
print(s.solve(A, B))