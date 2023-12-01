class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        freq = [0 for _ in range(26)]

        for ind in range(len(A)):
            freq[ord(A[ind]) - ord('a')] += 1

        freq.sort()
        print(freq)
        for ind in range(26):
            if freq[ind] != 0 and B > 0:
                if freq[ind] > B:
                    freq[ind] -= B
                else:
                    print(ind)
                    B -= freq[ind]
                    freq[ind] = 0

        count = 0
        print(freq)
        for value in freq:
            if value != 0:
                count += 1
        return count

A = 'a'
B = 1
s = Solution()
print(s.solve(A, B))