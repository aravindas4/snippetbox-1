class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        ans = 0
        h = set()

        for i in range(N):
            h.add(str(A[i])+"-"+str(B[i]))

        print(h)
        for i in range(N):
            for j in range(i+1, N):
                print((A[i], B[i]), (A[j], B[j]))
                if A[i] == A[j] or B[i] == B[j]:
                    print('true', A[i] == B[i], A[j] == B[j])
                    continue
                
                p1 = str(A[i])+"-"+str(B[j])
                p2 = str(A[j])+"-"+str(B[i])
            
                if p1 in h and p2 in h:
                    print(p1, p2)
                    ans += 1

        return ans // 2
    
s = Solution()
A = [1,1,2,2]
B = [1,2,1,2]
print(s.solve(A, B))