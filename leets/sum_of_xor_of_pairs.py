import math

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        ans = 0
        N = len(A)
        last_bit = int(math.log(max(A), 2)) + 1
        # print(max(A), last_bit)
        for i in range(last_bit+1):
            count = 0
            for num in A:
                if (1 << i) & num:
                    count += 1

            print(num, count)
            print((count * (N - count)))
            ans += ((count * (N - count)) * (1 << i))

        return ans

A = [28,7,3,6,23,16,5,29,23]
S = Solution()
print(S.solve(A))