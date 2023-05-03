class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        imax = -1
        imin = -1
        leng = N

        maxe = A[0]
        mine = A[0]

        for num in A:
            if num > maxe:
                maxe = num
            elif num < mine:
                mine = num

        if maxe == mine:
            return 1
        
        for ind in range(N-1, -1, -1):
            if A[ind] == maxe:
                imax = ind 
                if imin != -1:
                    leng = min(leng, imin - imax + 1)
            elif A[ind] == mine:
                imin = ind
                if imax != -1:
                    leng = min(leng, imax - imin + 1)

        return leng

s = Solution()
# print(s.solve([1, 3, 2]))
# print(s.solve([2, 6, 1, 6, 9]))
print(s.solve([ 814, 761, 697, 483, 981 ]))