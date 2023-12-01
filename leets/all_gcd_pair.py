class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        O = []
        H = {}
        A.sort(reverse=True)

        for num in A:
            if H.get(num, 0) > 0:
                H[num] -= 1
            else:
                for ele in O:
                    G = self.gcd(num, ele)
                    
                    if G in H:
                        H[G] += 2
                    else:
                        H[G] = 2

                O.append(num)
        return O


    def gcd(self, A, B):
        if B == 0:
            return A 

        return self.gcd(B, A % B)
    
S = Solution()
A = [1,31,1,1,1,1,14,2,1,1,1,2,22,1,11,1,1,1,1,23,1,1,11,1,11]
print(S.solve(A))