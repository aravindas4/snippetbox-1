class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        return self.pprint(A, B, "0")

    def pprint(self, A, B, R):
        if A == 1:
            print(R)
            return R[B]

        new = ""
        for ind in range(len(R)):
            if R[ind] == "0":
                new += "01"
            else:
                new += "10"

        R = new
            
        return self.pprint(A-1, B, R)

A, B = 4, 3
s = Solution()
print(s.solve(A, B))