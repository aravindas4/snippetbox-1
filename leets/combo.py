class Solution:
	# @param A : integer
	# @param B : integer
	# @return a list of list of integers
    def combine(self, A, B):
        o = []
        if A >= B:
            self.combo(1, A, B, [], o)
        return o

    def combo(self, i, N, K, cur, O):
        print(i, N, K, cur, O)
        if K == 0:
            O.append(cur)
            return 
        if i > N:
            return
        
        self.combo(i+1, N, K-1, cur[:] + [i], O)
        self.combo(i+1, N, K, cur[:], O)

s = Solution()
print(s.combine(4, 3))