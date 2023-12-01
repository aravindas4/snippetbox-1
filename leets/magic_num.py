class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        d = 0
        power = 1
        while A > 0:
            rem = A % 2
            A = A // 2
            d += (rem * power)
            power *= 10

        power = 5
        ans = 0
        while d > 0:
            rem = d % 10
            ans += (power * rem)
            power *= 5
            d = d // 10

        return ans

s = Solution()
print(s.solve(3))