class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of integers
    def dNums(self, A, B):
        H = {}
        N = len(A)

        R = []
        for i in range(B):
            if A[i] in H:
                H[A[i]] += 1
            else:
                H[A[i]] = 1

        R.append(len(H))

        start = 1
        end = B

        while end < N:
            if H[A[start-1]] == 1:
                H.pop(A[start-1])
            else:
                H[A[start-1]] -= 1

            print(end)
            if A[end] in H:
                H[A[end]] += 1
            else:
                H[A[end]] = 1

            R.append(len(H))

            start += 1
            end += 1

        return R

A = [1,2,1,3,4,3]
B = 3

s = Solution()
print(s.dNums(A, B))