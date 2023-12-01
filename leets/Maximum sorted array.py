class Solution:
	# @param A : list of integers
	# @return a list of integers
    def subUnsort(self, A):
        N = len(A)
        print(A)
        
        i = -1
        for i in range(0, N-1):
            if A[i] <= A[i+1]:
                continue
            else:
                break

        if i == (N-2):
            return [-1]

        j = -1
        for j in range(N-1, 0, -1):
            if A[j] >= A[j-1]:
                continue
            else:
                break

        maxe = A[i]
        mine = A[j]

        print(N, i, j)
        for k in range(i, j+1):
            if A[k] > maxe:
                maxe = A[k]
            
            if A[k] < mine:
                mine = A[k]

        ans1 = 0
        ans2 = N-1
        print(mine, maxe)
        for k in range(i+1):
            if A[k] <= mine:
                continue
            else:
                 ans1 = k
                 break

        for k1 in range(N-1, j-1, -1):
            # print(A[k1], k1)
            if A[k1] >= maxe:
                continue
            else:
                ans2 = k1
                break
        
        return [ans1, ans2]

s = Solution()
# A = [3,3,4,5,5,9,11,13,14,15,15,16,15,20,16]
# A = [2, 3, 5, 7, 10, 6, 11, 15, 18, 20]
A = [1,1,4,6,8,8,13,13,13,14,17,18,14]
A = [16,15,16,20]
A = [1,2,3]
print(s.subUnsort(A))