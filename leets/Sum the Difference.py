class Solution:
	# @param A : list of integers
	# @return an integer
    def solve(self, A):
        A.sort()
        ans = 0
        N = len(A)
        m = 1000000007

        print(A)
        for i in range(N):
            e = A[i]
            a = self.power(2, N-i-1, m)
            b = self.power(2, i, m)
            d = b- a
            
            # print(2, N-i-1, i)
            print(ans, a, b, d, e)
            ans = ans + (d * e)
            # print(ans)

        return ans

    def power(self, a, b , m):
        if b == 0:
            return 1

        if b == 1:
            return a

        ir = self.power(a, b//2, m)
        r = (ir * ir) % m
        # print(r)
        if b & 1:
            r = (r * a) % m

        return r

s = Solution()
A = [5,4,2]
print(s.solve(A))
# print(s.power(2, 5, 5))
