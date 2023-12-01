class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        mod = (10 ** 9) + 7

        freq = {}
        for num in A:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        count = 0
    
        for ind in range(1, N):
            num = A[ind]
            k1 = A[ind] - B
            k2 = A[ind] + B

            if k1 in freq and freq[k1] > 0 and freq[num] > 0:
                count += ((freq[k1] * freq[num]) % mod)
            
            if k2 in freq and freq[k2] > 0 and freq[num] > 0:
                count += ((freq[k2] * freq[num]) % mod)

        return count
        

s = Solution()
A = [18,26,17,30,13,30,20,13]
B = 10
print(s.solve(A, B))