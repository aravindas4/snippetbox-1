class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        psume = [0 for _ in range(N)]
        psumo = [0 for _ in range(N)]

        psume[0] = A[0]
        for idx in range(1, N):
            if idx % 2 == 0:
                psume[idx] = psume[idx-1] + A[idx]
            else:
                psume[idx] = psume[idx-1]

        psumo[0] = 0
        
        for idx in range(1, N):
            if idx % 2 == 1:
                psumo[idx] = psumo[idx-1] + A[idx]
            else:
                psumo[idx] = psumo[idx-1]

        print("psume: ", psume, "psumo: ", psumo)
        count = 0
        for idx in range(N):
            se = psumo[N-1] - psumo[idx]
            if idx != 0:
                se += psume[idx-1]

            so = psume[N-1] - psume[idx]
            if idx != 0:
                so += psumo[idx-1]

            if se == so:
                count += 1

        return count
    
s = Solution()
print(s.solve([2, 1, 6, 4]))