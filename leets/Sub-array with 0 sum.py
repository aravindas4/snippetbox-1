# Do not write code to include libraries, main() function or accept any input from the console.
# Initialization code is already written and hidden from you. Do not write code for it again.
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # Just write your code below to complete the function. Required input is available to you as the function arguments.
        # Do not print the result or any output. Just return the result via this function.
        psum = [0 for _ in range(len(A))]
        psum[0] = A[0]
        N = len(A)
        for ind in range(1, N):
            psum[ind] = psum[ind-1] + A[ind]

        nums = set()

        for ind in range(N):
            if psum[ind] == 0:
                return 1

            nums.add(psum[ind])

        print(len(psum))
        print(len(nums))
        if len(nums) != len(A):
            return 1
        return 0


A = [88,2,46,66,89,-79,36,72,30,60,89,23,60,26,-43,-14,20,92,-48,45,84,-22,65,-57,7]
s = Solution()
print(s.solve(A))