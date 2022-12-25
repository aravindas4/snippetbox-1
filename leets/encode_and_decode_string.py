class Solution:
    "https://www.lintcode.com/problem/659/"
    
    def encode(self, strs):
        """
        @param: strs: a list of strings
        @return: encodes a list of strings to a single string.
        """
        res_str: str = ""

        for word in strs:
            res_str += str(len(word)) + "#" + word

        return res_str

    def decode(self, str):
        """
        @param: str: A string
        @return: dcodes a single string to a list of strings
        """
        result = []; index = 0

        while index < len(str):
            # Get the length of string
            sub_index = index 
            while str[sub_index] != '#':
                sub_index += 1
            length = int(str[index:sub_index])
            # Get the string
            result.append(str[sub_index+1: sub_index+1+length])

            index = sub_index+1+length
        return result
