import sys

# sys.setrecursionlimit(10000000)
class Solution:
	# @param A : list of list of integers
	# @return an integer
    def adjacent(self, A):
        self.mem = {}
        self.arr = []
        N = len(A[0])
        self.N = N

        for i in range(N):
            self.arr.append(max(A[0][i], A[1][i]))
            
        r = max(self.solve(0, True), self.solve(0, False))
        print(self.mem)
        print(self.arr)
        return r

    def solve(self, pos, flag):
        # print(pos, flag)
        if pos == self.N:
            return 0
        
        key = str(pos) + '-' + str(flag)

        if key in self.mem:
            return self.mem[key]

        if flag:
            val = self.solve(pos+1, False) + self.arr[pos]
        else:
            val = max(self.solve(pos+1, True), self.solve(pos+1, False))

        self.mem[key] = val
        return val

s = Solution()
A = [   
        [1, 2, 3, 4],
        [2, 3, 4, 5]    
     ]
print(s.adjacent(A))