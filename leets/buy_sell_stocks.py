class Solution:
	# @param A : tuple of integers
	# @return an integer
    def maxProfit(self, A):
        # Carry forward
        N = len(A)
        maxe = A[N-1]
        ans = 0
	
        for ind in range(N-2, -1, -1):
            if A[ind] > maxe:
                maxe = A[ind]
            else:
                ans = max(ans, maxe - A[ind])

        return ans
    
s = Solution()
print(s.maxProfit([1, 2]))