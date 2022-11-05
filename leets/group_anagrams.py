import string

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Steps
        # 0: Counter the frequency of letter
        # 1. maintain the map of the such frequency
        # 2. Group them

        counter: dict = {}
        for word in strs:  # times the input
            word_counter= {
                char: 0 for char in string.ascii_lowercase
            }
            
            for char in word: # size of lenthy word
                word_counter[char] += 1

            char_list = [ f"{k}{v}" for k, v in word_counter.items()]

            word_map = "".join(char_list)

            if word_map in counter:
                counter[word_map].append(word)
            else:
                counter[word_map] = [word]


        return list(counter.values())

solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
