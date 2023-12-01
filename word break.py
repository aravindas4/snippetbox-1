class Solution:
	# @param A : string
	# @param B : list of strings
	# @return an integer
    def wordBreak(self, A, B):
        N = len(A)
        dp = [0 for _ in range(N+1)]
        # dp[N] = 1

        for i in range(N-1, -1, -1):
            for idx, word in enumerate(B):
                wn = i + len(word)
                if wn <= N and A[i:wn] == word:
                    # print(i, wn)
                    dp[i] = dp[wn]

                if dp[i]:
                    break
                
        return dp[0]
    
s = Solution()
A = 'bbabbabbbbbbbbaababbbababbaaaabaabbbbabbabbababbbabbbaababaaaaaabababbbabababbabbaabaabbbbabbbbbbabaabaaaabaabbaaabbabababbababaabbbbabaabababaaabbabbaaababaaabaaabaaabbbbaaaabbbaaabbbaabaaababbbabbbbababbbbaaaabbbbbbbbabaaabababbaababbbabbababbbababbaabaaababbbbaabaabbabbaabbbaaabbbbbabbaaababbabbbbbabbbabaaaaaaaaabaaaabbabaaaaaaabbabbabbabaaabaaaabaabbabbaaaababaaaaabaaabaabbaaaaaabaaabaabbbbbaabaaababbaa'
B = ["bb","ab","aabbaa","a","abab","b","abbabbba","ba","abbb","bbbaaaaaab","aaba","aaa","aabbbaaab","bbaab","bbbbbbaabb","baabbaa","abb","aaaaba","aaaab","abababba","b","bbbbbb","bbaaabbb","bbb","ababbba","ba","bb","bb","abaaaaa","babbab","aaab","abbaaab","abaababaa","aababaaaa","ababaabbbb","a","baaab","aba","babbaababb","bbbbba","babbbbba","b","aabaaab","abbaa","bbaabaab","baaaa","bbb","aaaaab","baaba","ababaaa","abbbbbbab","aab","aaaaaabbb","baaaabb","aaabaabba","aaabba","abbabababb","ababbaaaba","bbbaaabbb","bbaaaaaab","ba","bb","abaababb","abbbabaaa","baaababba","baba","a","abba","baaaba","b","aaaabbbba","baaaaa","aabb","baaa","bbaa","baaaaaaaab","bbbaa","ab","bb","b","ba","babaabab","bab","abbaaba","a","aababb","ab","abbbb","bbbbab","bb","aaab","bbbbaababb","abaaabab","abbbbaba","aab","baabb","baaaabaabb"]
# B = ["interview","my","trainer"]
print(s.wordBreak(A, B))
