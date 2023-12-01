class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def maxSubarray(self, A, B, C):
        max_sum = 0
        for i in range(0, A):
            sub_sum = 0
            for j in range(i, A):
                sub_sum += C[j]
                print(sub_sum)
                if sub_sum <= B and sub_sum > max_sum:
                    max_sum = sub_sum

        return max_sum
    
s = Solution()
print(s.maxSubarray(1, 75, [4]))