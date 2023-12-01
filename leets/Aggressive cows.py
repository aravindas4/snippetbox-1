class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()
        l = 1 
        N = len(A)
        r = A[N-1] - A[0]
        ans = r

        while l <= r:
            mid = l + (r - l) // 2
            print(l, r, mid)

            if self.check(A, B, mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans

    def check(self, A, C, D):
        cows = 1
        lp = A[0]
        N = len(A)

        for i in range(1, N):
            if A[i] - lp >= D:
                cows += 1
                lp = A[i]

                if cows == C:
                    return True

        return False
    
s = Solution()
A = [5,17,100,11]
B = 2
print(s.solve(A, B))