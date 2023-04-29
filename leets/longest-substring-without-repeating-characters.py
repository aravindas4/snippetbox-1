# https://www.youtube.com/watch?v=wiGpQwVHdE0
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# O(n)

# Sliding window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        start = 0
        unique_chars = set()
        
        for end in range(len(s)):
            # Contraction
            while s[end] in unique_chars:
                unique_chars.remove(s[start])
                start += 1
            max_length = max(end - start + 1, max_length)
            unique_chars.add(s[end])

        return max_length

s = Solution()
print(s.lengthOfLongestSubstring(" "))
