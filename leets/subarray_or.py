class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        total_sub_array = N * (N+1) // 2
        mod = (10 ** 9) + 7

        ans = 0

        for i in range(0, 3):
            count_of_zero_sub = 0
            count_of_zero = 0

            for num in A:
                print(num, (1 << i) & num)
                if (1 << i) & num == 0:
                    count_of_zero += 1
                elif count_of_zero != 0:
                    count_of_zero_sub += ((count_of_zero* (count_of_zero+1) // 2) % mod)
                    count_of_zero = 0
            # print(count_of_zero_sub)
            if count_of_zero != 0:
                count_of_zero_sub += ((count_of_zero* (count_of_zero+1) // 2) % mod)

            ans += (((total_sub_array - count_of_zero_sub) * (2 ** i)) % mod)

        return ans % mod
    
s = Solution()
A = [1, 2, 3, 4, 5]
print(s.solve(A))