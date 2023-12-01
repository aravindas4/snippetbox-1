class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        ans = 0
        power = 1
        while A > 0:
            rem = A % 10
            print(power * rem)
            ans += (power * rem)
            A = A // 10
            print("A: ", A)
            power *= B

        return ans

s = Solution()
print(s.solve(65, 9))