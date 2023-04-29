# https://leetcode.com/problems/longest-repeating-character-replacement/
# https://www.youtube.com/watch?v=gqXU1UyA8pk&t=959s

# Sliding window
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        counter = {}

        result = 0

        for right in range(len(s)):
            counter[s[right]] = 1+ counter.get(s[right], 0)

            # (current lenght of string - most occurance) > k
            if (right - left + 1) - max(counter.values()) > k:
                # contraction
                counter[s[left]] -= 1
                left += 1
            else:
                result = max(result, right - left + 1)
        return result

        
    
s = Solution()
print(s.characterReplacement("ABAA", 0))
print(s.characterReplacement("ABAB", 2))
