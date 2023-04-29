import math

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        factors = []
        for num in range(1, int(math.sqrt(A))+1):
            if A % num == 0:
                if num == A:
                    continue
                elif A / num == num or int(A / num) == A:
                    factors.append(num)
                else:
                    factors.extend([num, int(A / num)])

        num_sum = 0
        for num in factors:
            num_sum += num 

        print(factors)
        if num_sum == A:
            return 1
        else:
            return 0

s = Solution()   
print(s.solve(6))