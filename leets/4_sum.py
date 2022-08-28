# https://leetcode.com/problems/4sum/

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """Idea: sort the array , Ksum and 2 sum approach"""
        # sort
        nums.sort()

        result = []
        quad = []

        def kSum(k, start, target):
            if k != 2:  # It's K sum, K != 2
                for ind in range(start, len(nums) - k + 1): # for each try to find a quadplet

                    if ind > start and nums[ind] == nums[ind - 1]: # duplicates
                        continue

                    quad.append(nums[ind])
                    kSum(k-1, ind+1, target - nums[ind])
                    quad.pop() # last element, which has been appended

            else: # It's two sum
                front = start
                rear = len(nums) -1

                while front < rear:
                    if nums[front] + nums[rear] < target:
                        front += 1
                    elif nums[front] + nums[rear] > target:
                        rear -= 1
                    else: # equals target
                        result.append(quad + [nums[front]] + [nums[rear]])
                        front += 1

                        while front < rear and nums[front] == nums[front - 1]: # duplciates
                            front += 1 # keep moving

        kSum(4, 0, target)
        return result

s = Solution()

print(s.fourSum([1,0,-1,0,-2,2], 0))
