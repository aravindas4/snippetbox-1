class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        # Carry forward
        count = 0
        N = len(A)

        def is_vowel(char):
            if char == 'a' or char == 'A':
                return True
            elif char == 'e' or char == 'E':
                return True
            elif char == 'i' or char == 'I':
                return True
            elif char == 'o' or char == 'O':
                return True
            elif char == 'u' or char == 'U':
                return True
            return False

        for ind in range(N-1, -1, -1):
            if is_vowel(A[ind]):
                count += N - 1 - ind + 1

        return count
    
s = Solution()

print(s.solve("kFbwEBGMTPcOVqenWEempRwOsjuxgMEhohXKqSxZWcqUuDHsRAGNTzwBYvVmTfPCwzFomjtTKLKjUCzHuNaAVoYoDysQWphGyexu"))