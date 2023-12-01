class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
    def convert_to_int(self, S):
        N = len(S)
        power = 1
        total = 0
        for ind in range(N-1, -1, -1):
            total += (power * int(S[ind]))
            power *= 10

        return total
    
    def addBinary(self, A, B):
        a = self.convert_to_int(A)
        b = self.convert_to_int(B)
        r = a + b
        print(r)

        R = ""
        while r > 0:
            rem = r % 10
            R = str(rem) + R
            r = r // 10

        return R

A =    '1010110111001101101000'
B = '1000011011000000111100110'

S = Solution()
print(S.addBinary(A, B))