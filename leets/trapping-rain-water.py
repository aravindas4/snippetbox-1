from typing import List

# https://www.youtube.com/watch?v=ZI2z5pq0TqA&t=882s
# https://leetcode.com/problems/trapping-rain-water/

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
                delta = max_left - height[left]
                if delta > 0:
                    water += delta
                max_left = max(max_left, height[left])
            else:
                right -= 1
                delta = max_right - height[right]
                if delta:
                    water += delta
                max_right = max(max_right, height[right])
        return water

s = Solution()
print(s.trap([4,2,0,3,2,5]))
