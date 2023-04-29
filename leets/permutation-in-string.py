# https://www.youtube.com/watch?v=UbyhOgBN834
# https://leetcode.com/problems/permutation-in-string/


# Sliding window technique

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # count chars in s1, s2[partially]
        s1_count, s2_count = [0] * 26, [0] * 26
        for ind in range(len(s1)):
            s1_count[ord(s1[ind]) - ord('a')] += 1
            s2_count[ord(s2[ind]) - ord('a')] += 1

        # count the matches
        matches = 0
        for ind in range(26):
            if s1_count[ind] == s2_count[ind]:
                matches += 1

        # iterate over rest of s2
        left = 0
        for right in range(len(s1), len(s2)):
            # There is possiblity that by first iteration itself matches may be 26
            if matches == 26:
                return True 

            # if matches == 26:
            #     return True 
            # right point is incremented
            index = ord(s2[right]) - ord('a')
            s2_count[index] += 1

            if s2_count[index] == s1_count[index]:
                matches += 1
            elif s2_count[index] == s1_count[index] + 1:
                matches -= 1

            # left pointer will be incremented
            index = ord(s2[left]) - ord('a')
            s2_count[index] -= 1
            if s2_count[index] == s1_count[index]:
                matches += 1 
            elif s2_count[index] == s1_count[index] - 1:
                matches -= 1
            
            left += 1
            
        return matches == 26 # to componsate last iteration
            
s = Solution()
print(s.checkInclusion("a", "ab"))