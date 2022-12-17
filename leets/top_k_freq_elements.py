from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequencies
        freq = {}

        for num in nums:
            if num in freq.keys():
                freq[num] += 1
            else:
                freq[num] = 1
        
        # Reverse the frequencies
        r_freq = {
            ind: [] for ind in range(len(nums), 0, -1)
        }

        for key, v in freq.items():
            r_freq[v].append(key)
        
        print(r_freq)
        result = []
        for _, counts in r_freq.items():
            for count in counts:
                result.append(count)

                if len(result) == k:
                    return result

s = Solution()
print(s.topKFrequent([-1, -1],1))