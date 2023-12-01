class Solution:
	# @param A : tuple of integers
	# @return an integer
    def solve(self, A):
        N = len(A)
        S = sum(A)

        class Pair:
            def __init__(self, sums, items):
                self.sums = sums
                self.items = items

        def compare(p1, p2):
            if p1.sums == p2.sums:
                if p1.items < p2.items:
                    return p1
                else:
                    return p2
            elif p1.sums > p2.sums:
                return p1
            else:
                return p2
        
        dp = [[Pair(0, 0) for _ in range((S//2)+1)] for _ in range(N+1)]
        
        for i in range(1, N+1):
            for j in range(1, (S//2)+1):
                dp[i][j] = dp[i-1][j]
                print(i)
                if j - A[i-1] >= 0:
                    p2 = dp[i-1][j-A[i-1]]
                    dp[i][j] = compare(dp[i][j], Pair(A[i-1]+p2.sums, 1+p2.items))

        return dp[-1][-1].items


s = Solution()
A = [8,4,5,7,6,2]
print(s.solve(A))