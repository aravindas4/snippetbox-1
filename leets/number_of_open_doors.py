class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        low = 1
        high = A
        
        while low <= high:
            mid = (high + low) // 2
            print(low, high, mid)
            if mid * mid < A:
                low = mid + 1
            elif mid * mid > A:
                high = mid - 1
            else:
                break
            
        return (high + low) // 2
    
S = Solution()
print(S.solve(10))