from collections import deque

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        s = deque()
        l = len(A)
        ans = []

        for ind in range(l-1, -1, -1):
            while len(s) > 0 and s[-1] <= A[ind]:
                s.pop()

            if len(s) < 1:
                ans.insert(0, -1)
            else:
                ans.insert(0, s[-1])

            s.append(A[ind])

        return ans
    
s = Solution()
print(s.nextGreater([4, 5, 2, 10] ))