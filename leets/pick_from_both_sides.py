class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        psum = [0] * N
        psum[0] = A[0]

        for ind in range(1, N):
            psum[ind] = psum[ind-1] + A[ind]

        total = psum[N-1]
        final = 0   
        # print(total)


        si = 0
        ei = N - B - 1

        def get_sum(sii, eii):
            if si == 0:
                return psum[eii]
            else:
                return psum[eii] - psum[sii-1]

        while ei < N:
            current_sum = psum[N-1] - get_sum(si, ei)

            if current_sum > final:
                final = current_sum

            ei += 1
            si += 1

        return final

# A = [ -533, -666, -500, 169, 724, 478, 358, -38, -536, 705, -855, 281, -173, 961, -509, -5, 942, -173, 436, -609, -396, 902, -847, -708, -618, 421, -284, 718, 895, 447, 726, -229, 538, 869, 912, 667, -701, 35, 894, -297, 811, 322, -667, 673, -336, 141, 711, -747, -132, 547, 644, -338, -243, -963, -141, -277, 741, 529, -222, -684, 35 ]
# B = 48
# Ans = 6253

A = [5, -2, 3 , 1, 2]
B = 3
# Ans = 8

# A = [ 2, 3, -1, 4, 2, 1 ]
# B = 4
# Ans = 9
s = Solution()
print(s.solve(A, B))
