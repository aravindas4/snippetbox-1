from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        answer = []

        # calculate prefixes
        prefix = 1
        for num in nums:
            answer.append(prefix)
            prefix *= num 

        # Calculate postfix
        postfix = 1
        for ind in range(size - 1, -1, -1):
            answer[ind] *= postfix
            postfix *= nums[ind]

        return answer

s = Solution()
print(s.productExceptSelf([1,2,3,4]))