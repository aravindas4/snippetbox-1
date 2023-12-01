class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
    def kthsmallest(self, A, B):
        A = list(A)
        N = len(A)
        for i in range(B):
            mine = A[i]
            mini = i
            for j in range(i+1, N):
                if A[j] < mine:
                    mine = A[j]
                    mini = j
                    
            temp = A[i]
            # print(temp)
            # print(A[mini])
            A[i] = A[mini]
            A[mini] = temp

        return A[B-1]

s = Solution()
A = [74,90,85,58,69,77,90,85,18,36]
B = 1
print(s.kthsmallest(A, B))
        