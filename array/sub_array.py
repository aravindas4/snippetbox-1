from typing import List


def sum_of_sub_arrays(nums: List[int], window: int):
    # Initial
    sub_array_sum = sum(nums[0:window])
    result = [sub_array_sum]

    if window > len(nums):
        return result

    for index in range(1, (len(nums)-window+1)):
        sub_array_sum = sub_array_sum - nums[index - 1]  # remove last element
        sub_array_sum = sub_array_sum + nums[index + window - 1]  # add new element

        result.append(sub_array_sum)

    return result


print(sum_of_sub_arrays([1,2,3,4,5,6], 2))