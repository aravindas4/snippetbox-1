from typing import List


def piegon_hole_sort(nums: List[int]) -> List[int]:
    max_e = max(nums)
    min_e = min(nums)
    bucket_size = max_e - min_e + 1 # Bucket size or piegon holes count

    bucket = [0] * bucket_size  # The bucket or piegon holes

    # Count the frequency ie, filling the holes
    for elem in nums:
        bucket_index = elem - min_e
        bucket[bucket_index] += 1

    # Sorting
    final_array = nums
    final_arr_index = 0
    
    for index in range(bucket_size):
        while bucket[index] > 0: # freq
            bucket[index] -= 1 # we found an occurance
            final_array[final_arr_index] = index + min_e
            final_arr_index += 1
            
    return final_array


print(piegon_hole_sort([3,4,5,6,7,5]))
