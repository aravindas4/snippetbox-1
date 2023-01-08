from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        result = 0

        while left < right:
            # Compute the area
            area = (right - left) * min(height[left], height[right])
            if area > result:
                result = area
            
            # Shift the pointer
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1

        return result

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
print(s.maxArea([1,1]))