class Solution:
	# @param A : string
	# @return a strings
    def maxPalindrome(self, start, end, A):
        N = len(A)
        while start >= 0 and end < N and A[start] == A[end]:
            start -= 1
            end += 1
        return A[start+1:end]
    
    def longestPalindrome(self, A):
        ans = ""
        N = len(A)
        for ind in range(N):
            s = self.maxPalindrome(ind, ind, A)
            if len(s) > len(ans):
                ans = s

        for ind in range(N-1):
            s = self.maxPalindrome(ind, ind+1, A)
            if len(s) > len(ans):
                ans = s
        return ans
    
S = Solution()

A = 'abb'
print(S.longestPalindrome(A))