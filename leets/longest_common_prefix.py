class Solution:
	# @param A : list of strings
	# @return a strings
    def longestCommonPrefix(self, A):
        s = ""
        for word in A:
            if len(s) == 0:
                s = word
            elif len(s) > len(word):
                s = word

        R = ""
        for ind in range(len(s)):
            for word in A:
                if word[ind] == s[ind]:
                    continue
                else:
                    break
            else:
                R += s[ind]

        return R

A = ["abcd","aze"]
s = Solution()
print(s.longestCommonPrefix(A))