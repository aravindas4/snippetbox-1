class Solution:
    def solve(self, arr):
        N = len(arr)
        total = 0
        for i in range(N):
            ssum = 0
            for j in range(i, N):
                # print("i=", i, ", j=",j)
                ssum += arr[j]  
                total += ssum
            else:
                print("ssum=", ssum)
        return total
    

# A = [1, 2, 3]
A = [0, 1, 2]
# A = [6, 8, -1, 7]
s = Solution()
print(s.solve(A))