# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {} # map of previous elements, value: index
        
        for index, elem in enumerate(nums):
            
            other_index = hash_map.get(target - elem)
            # print(other_index)
            # print(elem)

            if other_index is None:  # Other element does not exists
                hash_map[elem] = index
            else:
                return [index, other_index]

s = Solution()


print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([3,2,4], 6))
print(s.twoSum([3,3], 6))
print(s.twoSum([0,4,3,0], 0))
print(s.twoSum([-1,-2,-3,-4,-5], -8))
