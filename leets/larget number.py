from functools import cmp_to_key

class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        A = list(A)
        if max(A) == 0:
            return 0
        A.sort(key=cmp_to_key(self.cmpf))
        return "".join([str(i) for i in A])

    def cmpf(self, a, b):
        a_str = str(a)
        b_str = str(b)
        
        ab = int(a_str + b_str)
        ba = int(b_str + a_str)

        return ba - ab

s = Solution()
A = [12, 121]
print(s.largestNumber(A))