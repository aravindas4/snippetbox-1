class Solution:
	# @param A : list of integers
	# @return a list of integers
    def subUnsort(self, A):
        N = len(A)
        maxi = 0
        L = 0
        mini = N-1
        R = N -1

        while L <= R:
            if A[maxi] < A[L]:
                maxi = L 
            L += 1

            if A[mini] > A[R]:
                mini = R
            R -= 1

        if mini == 0:
            return [-1]
        return [maxi, mini]

s = Solution()
A = [3,3,4,5,5,9,11,13,14,15,15,16,15,20,16]
print(s.subUnsort(A))