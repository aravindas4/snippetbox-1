import copy

class Solution:
	# @param A : list of integers
	# @return a list of list of integers
    def subsets(self, A):
        a_set = set()

        for e in A:
            a_set.add(e)

        self.A = list(a_set)
        self.A.sort()
        self.N = len(self.A)
        self.final = [[]]
        self.solve(0)

    def solve(self, idx):
        if idx == self.N:
            return
        
        result = [self.A[idx]]
        self.final.append(copy.deepcopy(result))

        for i in range(idx, self.N):
            print(self.A, i, self.N)
            result.append(self.A[i])
            self.final.append(copy.deepcopy(result))

        self.solve(idx+1)

s = Solution()
A = [9,-20,-11,-8,-4,2,-12,14,1,-18]
print(s.subsets(A))