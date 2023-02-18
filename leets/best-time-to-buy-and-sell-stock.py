# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# https://www.youtube.com/watch?v=1pkOgXD63yU

from typing import List

# Two pointers

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0  # buy (low)
        right = 1 # sell (high)

        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                left = right
            right += 1
        return max_profit

s = Solution()
print(s.maxProfit([1,2,4,2,5,7,2,4,9,0,9]))