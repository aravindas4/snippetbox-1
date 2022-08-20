# https://leetcode.com/problems/3sum/

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Idea: sort the array and use two approach"""

        # sort
        nums.sort()

        # Two sum approach
        tracker = set()
        result = []

        for index, elem in enumerate(nums):

            # if elem in tracker:
            #     continue # To evade duplicates
            # else:
            #     tracker.add(elem)

            if index > 0 and nums[index - 1] == nums[index]:
                continue

            front = index + 1
            rear = len(nums) - 1

            while front < rear:
                currentSum = nums[front] + nums[rear] + elem
                if currentSum == 0:
                    result.append([elem, nums[front], nums[rear]])
                    
                    # Ex: [-2, -2, 0, 0, 2, 2]
                    # front = 0, rear = 5
                    # Let's only update front. because else rear -= 1 gonna take
                    # care of rear

                    front += 1

                    # front -1 becaue we just came from there and
                    # front should never pass rear
                    while nums[front] == nums[front -1 ] and front < rear:
                        front += 1
                    
                elif currentSum < 0:
                    front += 1
                else:
                    rear -= 1

        return result

s = Solution()
print(s.threeSum([0,1,1]))
print(s.threeSum([0,0,0]))