class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        count = 0
        ans = 0
        N = len(A)

        for num in A:
            if int(num) == 1:
                count += 1

        if count == N:
            return count

        if count == 0:
            return 0

        for ind in range(N):
            left = 0
            right = 0

            if int(A[ind]) == 0:
                if ind > 0:
                    for j in range(ind-1, -1, -1):
                        if int(A[j]) == 1:
                            left += 1
                        else:
                            break
            
                if ind < N:
                    for j in range(ind+1, N):
                        if int(A[j]) == 1:
                            right += 1
                        else:
                            break

            k = left + right

            if k < count:
                k += 1

            ans = max(k, ans)

        return ans
    
s = Solution()
A = "111011101"
print(s.solve(A))