from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length == 0:
            return 0

        # Pointers
        left = 0
        right = length - 1

        max_right = height[right]
        max_left = height[left]

        water = 0

        while left < right:
            if max_left < max_right:
                left += 1
                max_left = max(max_left, height[left])
                water += max_left - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                water += max_right - height[right]
        return water

s = Solution()
print(s.trap([5,4,1,2]))
