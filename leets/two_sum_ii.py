from typing import List

class Solution:
    # The array is sorted. so we can use the two pointers. No need of 
    # hashmaps.
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front = 0
        rear = len(numbers) - 1

        while front < rear:
            value = numbers[front] + numbers[rear]
            if value == target:
                return [front+1, rear+1] 

            if  value < target:
                front += 1 # front element is small
            else:
                rear -= 1  # rear element is larger

        return []

s= Solution()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([2, 3, 4], 6))
print(s.twoSum([-1, 0], -1))
