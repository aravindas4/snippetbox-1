from functools import cmp_to_key

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        self.A = A 
        self.B = B 
        ans = 0
        idxes = [i for i in range(len(A))]
        idxes = sorted(idxes, key=cmp_to_key(self.custom_key))

        # print(idxes)
        for idx in idxes:
            v = A[idx]
            w = B[idx]

            # print(v, w, C)
            if C > 0:
                if w <= C:
                    ans += v
                    C -= w
                else:
                    ans += (C * v) / w
                    C = 0

            print(ans)
        
        # return int(round(ans, 2) * 100)
        print(int(ans) * 100)
        return int(ans * 100)

    def custom_key(self, a, b):
        va = self.A[a]
        vb = self.A[b]
        wa = self.B[a]
        wb = self.B[b]

        # print(a, b)
        return (vb * wa) - (va * wb)

        # if v > 0:
        #     return 1
        # elif v < 0:
        #     return -1
        # return 0
s = Solution()
A = [16,3,3,6,7,8,17,13,7]
B = [3,10,9,18,17,17,6,16,13]
C = 11 
# A = [60, 100, 120]
# B = [10, 20, 30]
# C = 50

s.solve(A, B, C)
from functools import cmp_to_key

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        self.A = A 
        self.B = B 
        ans = 0
        idxes = [i for i in range(len(A))]
        idxes = sorted(idxes, key=cmp_to_key(self.custom_key))

        for idx in idxes:
            v = A[idx]
            w = B[idx]

            # print(v, w, C)
            if C > 0:
                if w <= C:
                    ans += v
                    C -= w
                else:
                    ans += (C * v) / w
                    C = 0

            print(ans)

        print(int(ans) * 100)
        return int(ans) * 100

    def custom_key(self, a, b):
        va = self.A[a]
        vb = self.A[b]
        wa = self.B[a]
        wb = self.B[b]
        return (vb * wa) - (va * wb)


s = Solution()
A = [16,3,3,6,7,8,17,13,7]
B = [3,10,9,18,17,17,6,16,13]
C = 11 
# A = [60, 100, 120]
# B = [10, 20, 30]
# C = 50
print('---------')
s.solve(A, B, C)
