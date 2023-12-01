import math

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        R = int(math.sqrt(2 * A)) + 1
        print("R", R)
        count = 0
        
        for i in range(1, R):
            r = ((2 * A) - (i * (i-1)) )
            print(r)
            if r > 0 and r % (2* i) == 0:
                count += 1

        return count
    
s = Solution()
print(s.solve(1))