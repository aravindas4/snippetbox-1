from typing import List
class Solution:
    def containsNearbyAlmostDuplicate(
        self, 
        nums: List[int], 
        k: int, 
        t: int
    ) -> bool:
        # Bucket size, +1 because t can be 0 and 
        # t's can take value between 0 and t (t+1 values)
        segment = t + 1 

        bucket = {} # dict

        for index, elem in enumerate(nums):
            # print(bucket)
            # print(elem)
            bucket_idx = elem // segment

            if bucket_idx in bucket:
                # print("In")
                # print(bucket)
                return True
            else:
                bucket[bucket_idx] = elem
                # print(bucket)

                low_idx = bucket_idx - 1
                high_idx = bucket_idx + 1

                # Neighbours
                if low_idx in bucket and elem - bucket[low_idx] <= t:
                    # print("Low")
                    # print(low_idx)
                    return True

                if high_idx in bucket and bucket[high_idx] - elem <= t:
                    # print("High")
                    # print(high_idx)
                    return True

            

            if index >= k: # K > 0 and index >= 0;
                # index - k in nums gives leftmost outer element wrt window of nums
                # so, the remove such key from bucket
                del bucket[nums[index - k] // segment]

        return False 


print(Solution().containsNearbyAlmostDuplicate(nums = [1,2,3,1], k = 3, t = 0))
print(Solution().containsNearbyAlmostDuplicate(nums = [1,0,1,1], k = 1, t = 2))
print(Solution().containsNearbyAlmostDuplicate(nums = [1,5,9,1,5,9], k = 2, t = 3))
